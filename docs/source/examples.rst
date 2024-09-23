TEST Data
=========

The following file inputs are loaded sequentially into the database.  After the last scenario is loaded reports are generated.  The database report is an exhaustive report of all data loaded into the database.  The IFDat report is a summary report for Investment Fund of the latest valid authoritative data.


FILE INPUTS
-----------


File Input 1
~~~~~~~~~~~~
Partner EGRJOURNEY and user juser submits INIT source_type DBDat data.

Data are uploaded into the database using log=1 for user "juser" and log=2 for user="AUTH".

Five entities are created using REF.ORG table.

Details of the five entities are entered using REF.ORG_DYNMC table.

ORG to ORG associations are created using REF.ORG2ORG table.

Identification aliases are created using REF.ORG_ALIAS table.

Share reference data are provided in the REF.SHR and REF.SHR_DYNMC table.  The associations with ORG entities are provided in the ORG2SHR table.

juser details are provided in REF.USR_DYNMC and the association in the REF.USR2ORG table

Acquisition: :download:`F_000000001_DBDAT_JUSER_0.json </_static/data/acq/F_000000001_DBDAT_JUSER_0.json>`

Acknowledgement: :download:`ACK_000000001_juser.json </_static/data/ack/ACK_000000001_juser.json>`


File Input 2 
~~~~~~~~~~~~~
Partner EGRJOURNEY and user juser submits INIT source_type DBDat data.

Data are uploaded into the database using log=3 for user "juser" and log=4 for user="AUTH".

A correction is made to the REF.ORG_ALIAS table.

Acquisition: :download:`F_000000002_DBDAT_JUSER_1.json </_static/data/acq/F_000000002_DBDAT_JUSER_1.json>`

Acknowledgement: :download:`ACK_000000003_juser.json </_static/data/ack/ACK_000000003_juser.json>`


File Input 2 
~~~~~~~~~~~~~
Partner EGRJOURNEY and user juser submits INIT source_type DBDat data.

Data are uploaded into the database using log=3 for user "juser" and log=4 for user="AUTH".

A correction is made to the REF.ORG_ALIAS table.

Acquisition: :download:`F_000000003_DBDAT_JUSER_2.json </_static/data/acq/F_000000003_DBDAT_JUSER_2.json>`

Acknowledgement: :download:`ACK_000000005_juser.json </_static/data/ack/ACK_000000005_juser.json>`


File Input 3 
~~~~~~~~~~~~~
Raise submitter inconsistency error 

Acquisition: :download:`F_000000003_DBDAT_JUSER_2.json </_static/data/acq/F_000000002_DBDAT_JUSER_1.json>`

Acknowledgement: :download:`ACK_000000003_juser.json </_static/data/ack/ACK_000000003_juser.json>`


File Input 4 
~~~~~~~~~~~~
Partner EGRCDRJOURNEY and user jcduser submits CDR source_type DBDat data.

Data are uploaded into the database using log=6 for user "jcduser" and log=7 for user="AUTH".

New org alias info is uploaded.

Acquisition: :download:`F_000000004_DBDAT_JCDRUSER_3.json </_static/data/acq/F_000000004_DBDAT_JCDRUSER_3.json>`

Acknowledgement: :download:`ACK_000000006_jcdruser.json </_static/data/ack/ACK_000000006_jcdruser.json>`


File Input 5
~~~~~~~~~~~~
Partner EGRJOURNEY and user juser submits INIT source_type DBDat data.

Data are uploaded into the database using log=8 for user "juser" and log=9 for user="AUTH".

Name updates in the ORG_DYNMC table are entered.

Acquisition: :download:`F_000000005_DBDAT_JUSER_4.json </_static/data/acq/F_000000005_DBDAT_JUSER_4.json>`

Acknowledgement: :download:`ACK_000000008_juser.json </_static/data/ack/ACK_000000008_juser.json>`


File Input 6 
~~~~~~~~~~~~
Partner EGRJOURNEY and user jcduser submits CDR source_type DBDat data.

Data are uploaded into the database using log=10 for user "juser" and log=11 for user="AUTH".

Name updates in the ORG_DYNMC table are entered.

Acquisition: :download:`F_000000006_DBDAT_JCDRUSER_5.json </_static/data/acq/F_000000006_DBDAT_JCDRUSER_5.json>`

Acknowledgement: :download:`ACK_000000010_jcdruser.json </_static/data/ack/ACK_000000010_jcdruser.json>`


File Input 7 
~~~~~~~~~~~~~
Partner EGRJM1 and user sdruser submits IFDat data.

IFDat Acquisition: :download:`ifdat_sdruser_6.json </_static/acq/raw/ifdat_sdruser_6.json>`

IFData is converted to DBDat Acquisition: :download:`F_000000007_DBDAT_SDRUSER_6.json </_static/data/acq/F_000000007_DBDAT_SDRUSER_6.json>`

Aliases updates are entered

Data are uploaded into the database using log=12 for user "juser" and log=13 for user="AUTH".

Acknowledgement: :download:`ACK_000000012_sdruser.json </_static/data/ack/ACK_000000012_sdruser.json>`


File Input 8 
~~~~~~~~~~~~~
Partner EGRJM1 and user sdruser submits IFDat data.

IFDat Acquisition: :download:`ifdat_sdruser_7.json </_static/acq/raw/ifdat_sdruser_7.json>`

IFData is converted to DBDat Acquisition: :download:`F_000000008_DBDAT_SDRUSER_7.json </_static/data/acq/F_000000008_DBDAT_SDRUSER_7.json>`

Entity is merged.

Data are uploaded into the database using log=14 for user "juser" and log=15 for user="AUTH".

Acknowledgement: :download:`ACK_000000014_sdruser.json </_static/data/ack/ACK_000000014_sdruser.json>`


File Input 9
~~~~~~~~~~~~
Partner EGRJM2 and user sdrm2usr submits IFDat data.

IFDat Acquisition: :download:`ifdat_sdrm2user_8.json </_static/acq/raw/ifdat_sdrm2user_8.json>`

IFData is converted to DBDat Acquisition: :download:`F_000000009_DBDAT_SDRM2USER.json </_static/data/acq/F_000000009_DBDAT_SDRM2USER_8.json>`

New management company is created, new investment fund is created, change of management occurs, alias and dynamic tables are updated.

Data are uploaded into the database using log=16 for user "juser" and log=17 for user="AUTH".

Acknowledgement: :download:`ACK_000000016_sdrm2user.json </_static/data/ack/ACK_000000016_sdrm2user.json>`


REPORTS
-------

DATABASE REPORT
~~~~~~~~~~~~~~~

A report that provides the full provided data in the DBDat Database

:download:`Database Report </_static/data/reports/DATABASE_REPORT.xlsx>`


IFDat REPORT
~~~~~~~~~~~~

A report that provides an Investment Fund type report of the latest valid authoritative data.

:download:`IFDat Report </_static/data/reports/IFDAT_REPORT.xlsx>`
