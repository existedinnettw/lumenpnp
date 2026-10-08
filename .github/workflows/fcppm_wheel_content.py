"""Fail unless the wheel ships the assembly, its parts and the package metadata FreeCAD reads."""

import sys
import zipfile

WANT = [
    "lumenpnp/package.xml",
    "lumenpnp/pyproject.toml",
    "lumenpnp/LICENSE",
    "lumenpnp/assembly.FCStd",
    "lumenpnp/FDM/z-gantry.FCStd",
    "lumenpnp/FDM/squaring-bracket.FCStd",
    "lumenpnp/MISC/MGN12H-linear-rail-carriage.FCStd",
]

(wheel,) = sys.argv[1:]
names = set(zipfile.ZipFile(wheel).namelist())
missing = [w for w in WANT if w not in names]
parts = sum(1 for n in names if n.startswith("lumenpnp/FDM/") and n.endswith(".FCStd"))
print(f"{wheel}: {len(names)} files, {parts} printed parts")
if missing or parts == 0:
    sys.exit(f"missing from the wheel: {missing or 'FDM/*.FCStd'}")
