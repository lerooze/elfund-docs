import os
from pathlib import Path
from typing import cast
import shutil
import glob

src_root = Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("prod")
src_dir_structure = src_root.joinpath("structure")
dst_root = Path(os.path.abspath(__file__)).parent
static_root = dst_root.joinpath("source/_static")
try:
    shutil.rmtree(static_root)
except FileNotFoundError:
    os.makedirs(static_root)
structure_path = static_root.joinpath("structure")
os.makedirs(structure_path)
for f in glob.glob(str(src_dir_structure.joinpath("*"))):
    pf = Path(f)
    if pf.name.startswith("codelists"):
        continue
    shutil.copyfile(pf, structure_path.joinpath(pf.name))
