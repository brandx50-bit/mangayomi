"""Verify that a MangaNest APK includes its identity, licenses and native engine."""

import os
from pathlib import Path
import re
import struct
import subprocess
import sys
import zipfile

apk = Path(sys.argv[1])
with zipfile.ZipFile(apk) as archive:
    names = set(archive.namelist())
    abis = {name.split('/')[1] for name in names if name.endswith('/libflutter.so')}
    assert abis, 'APK has no Flutter engine'
    machines = {'arm64-v8a': 183, 'armeabi-v7a': 40, 'x86_64': 62}
    for abi in sorted(abis):
        library = f'lib/{abi}/librust_lib_mangayomi.so'
        assert library in names, f'Missing required Rust engine: {library}'
        header = archive.read(library)[:20]
        assert header[:4] == b'\x7fELF', f'Invalid native library: {library}'
        assert struct.unpack_from('<H', header, 18)[0] == machines[abi], library
    for name in ['manganest_LICENSE.txt', 'manganest_NOTICE.txt']:
        assert f'assets/flutter_assets/assets/{name}' in names, f'Missing {name}'

sdk = Path(os.environ.get('ANDROID_HOME') or os.environ['ANDROID_SDK_ROOT'])
tools = list((sdk / 'build-tools').glob('*/aapt'))
assert tools, 'Android aapt is unavailable'
badging = subprocess.check_output([str(tools[-1]), 'dump', 'badging', str(apk)], text=True)
assert "package: name='com.brandx50.manganest'" in badging, 'Unexpected Android package'
assert re.search(r"application-label(?:-en)?:'MangaNest'", badging), 'Unexpected app name'
print(f'Verified MangaNest APK, license assets, and Rust engine for {", ".join(sorted(abis))}.')
