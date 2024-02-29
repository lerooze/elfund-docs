import os
from pathlib import Path
from typing import cast
import shutil
import glob

src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_METADATA")))
    .joinpath("test")
    .joinpath("structure")
)
dst_root = Path(os.path.abspath(__file__)).parent
static_root = dst_root.joinpath("source/_static")
dst_dir = static_root.joinpath("structure")
try:
    shutil.rmtree(static_root)
except FileNotFoundError:
    os.makedirs(static_root)
shutil.copytree(src_dir, dst_dir)
