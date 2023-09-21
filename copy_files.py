from pathlib import Path
import shutil

cwd = Path(__file__).parent
src = cwd.parent.joinpath("journey/docs/docs/source/_files/dbdat")
ifdatsrc = cwd.parent.joinpath("journey/docs/docs/source/_files/ifdat")
dst_base = src.glob("DBDAT*")
ifdatdst_base = ifdatsrc.glob("IFDAT*")


for f in dst_base:
    shutil.copy2(f, cwd.joinpath("docs/source/_files/dbdat"))
for f in ifdatdst_base:
    shutil.copy2(f, cwd.joinpath("docs/source/_files/ifdat"))
docx_from = cwd.joinpath("docs/_build/docx/ELFund-docs-.docx")
shutil.copy2(docx_from, cwd.joinpath("docs/source/_files/"))
