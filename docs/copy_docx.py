from pathlib import Path
import os
import shutil

root = Path(os.path.abspath(__file__)).parent
src = root.joinpath("_build/html/docx/ELFund-docs.docx")
dst = root.joinpath("source/_static/ELFund-Docs.docx")
shutil.copyfile(src, dst)
