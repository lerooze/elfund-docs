import os
from pathlib import Path
from typing import cast
import shutil

dst_root = Path(os.path.abspath(__file__)).parent
static_root = dst_root.joinpath("source/_static")
try:
    shutil.rmtree(static_root)
except FileNotFoundError:
    os.makedirs(static_root)
src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_METADATA")))
    .joinpath("test")
    .joinpath("structure")
)
dst_dir = static_root.joinpath("structure")
shutil.copytree(src_dir, dst_dir)
src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_METADATA"))).joinpath("test").joinpath("acq")
)
dst_dir = static_root.joinpath("data/acq")
os.makedirs(dst_dir)
shutil.copytree(src_dir, dst_dir)

src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_METADATA"))).joinpath("test").joinpath("ack")
)
dst_dir = static_root.joinpath("data/ack")
os.makedirs(dst_dir)
shutil.copytree(src_dir, dst_dir)
