import os
from pathlib import Path
from typing import cast
import shutil
import glob

cwd = Path(__file__).parent
dst_root = Path(os.path.abspath(__file__)).parent
static_root = dst_root.joinpath("source/_static")
try:
    shutil.rmtree(static_root)
except FileNotFoundError:
    os.makedirs(static_root)
src_dir = cwd.parent.parent.joinpath("journey/tests/metaresources/structure")
dst_dir = static_root.joinpath("structure")
shutil.copytree(src_dir, dst_dir)
src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_METADATA")))
    .joinpath("test")
    .joinpath("data")
    .joinpath("*.*")
)
dst_dir = static_root.joinpath("acq/raw")
dst_dir.mkdir(parents=True, exist_ok=True)
for filename in glob.glob(str(src_dir)):
    shutil.copy(filename, dst_dir)

src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("test").joinpath("acq")
)
dst_dir = static_root.joinpath("data/acq")
shutil.copytree(src_dir, dst_dir)

src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("test").joinpath("ack")
)
dst_dir = static_root.joinpath("data/ack")
shutil.copytree(src_dir, dst_dir)
src_dir = (
    Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("test").joinpath("reports")
)
dst_dir = static_root.joinpath("data/reports")
shutil.copytree(src_dir, dst_dir)
