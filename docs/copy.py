import os
from pathlib import Path
from typing import cast
import shutil

src_root = Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("test")
src_dir_structure = src_root.joinpath("structure")
dst_root = Path(os.path.abspath(__file__)).parent
static_root = dst_root.joinpath("source/_static")
paths = ["acq", "ack", "examples", "reports", "structure"]
for p in paths:
    dst_path = static_root.joinpath(p)
    try:
        shutil.rmtree(dst_path)
    except FileNotFoundError:
        pass
dst_structure = static_root.joinpath("structure")
shutil.copytree(src_dir_structure, dst_structure)
paths = ["acq", "ack", "examples", "reports"]
for p in paths:
    src_path = src_root.joinpath(p)
    dst_path = static_root.joinpath(p)
    shutil.copytree(src_path, dst_path)

ifdat_list_src = (
    Path(cast(str, os.environ.get("JOURNEY_DATA")))
    .joinpath("prod")
    .joinpath("reports")
    .joinpath("IFDAT-LIST.xlsx")
)
ifdat_list_dst = (
    static_root.joinpath("reports").joinpath("prod").joinpath("IFDAT-LIST.xlsx")
)
ifdat_list_dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copy(ifdat_list_src, ifdat_list_dst)
