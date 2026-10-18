#!/usr/bin/env python3
"""Build and verify a deterministic, allowlisted skill ZIP using only the stdlib."""
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile, ZipInfo
import argparse
import hashlib
import sys

from check_skill import NAME, ROOT, SKILL_FILES, check

VERSION = '0.1.0'
OUT = ROOT / 'dist' / f'{NAME}-v{VERSION}.zip'
CHECKSUMS = OUT.parent / 'SHA256SUMS'


def verify(archive: Path = OUT) -> None:
    expected = {f'{NAME}/{name}': name for name in SKILL_FILES}
    with ZipFile(archive) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or set(names) != set(expected):
            raise ValueError('ZIP must contain exactly the allowlisted skill files')
        if z.testzip() is not None:
            raise ValueError('ZIP integrity check failed')
        for item in z.infolist():
            if item.create_system != 3 or item.external_attr >> 16 != 0o100644:
                raise ValueError('ZIP entries must be non-executable regular files')
            if item.flag_bits & 1:
                raise ValueError('Encrypted ZIP entries are not supported')
            if z.read(item) != (ROOT / expected[item.filename]).read_bytes():
                raise ValueError(f'ZIP differs from source: {item.filename}')
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    if CHECKSUMS.read_text(encoding='utf-8') != f'{digest}  {archive.name}\n':
        raise ValueError('SHA256SUMS does not match the ZIP')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='verify existing ZIP and checksum without rebuilding')
    args = parser.parse_args()
    errors = check()
    if errors:
        raise ValueError('\n'.join(errors))
    if not args.check:
        OUT.parent.mkdir(exist_ok=True)
        temporary = OUT.with_suffix('.zip.tmp')
        try:
            with ZipFile(temporary, 'w', compression=ZIP_STORED) as z:
                for name in sorted(SKILL_FILES):
                    source = ROOT / name
                    if source.is_symlink() or not source.resolve().is_relative_to(ROOT.resolve()):
                        raise ValueError(f'Package source must stay inside repository: {name}')
                    item = ZipInfo(f'{NAME}/{name}', date_time=(2026, 1, 1, 0, 0, 0))
                    item.create_system = 3
                    item.external_attr = 0o100644 << 16
                    z.writestr(item, source.read_bytes())
            temporary.replace(OUT)
        finally:
            temporary.unlink(missing_ok=True)
        digest = hashlib.sha256(OUT.read_bytes()).hexdigest()
        CHECKSUMS.write_text(f'{digest}  {OUT.name}\n', encoding='utf-8')
    verify()
    print(f'PASS: {OUT.name}, {len(SKILL_FILES)} allowlisted files, source bytes, ZIP integrity, SHA-256')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        sys.exit(1)
