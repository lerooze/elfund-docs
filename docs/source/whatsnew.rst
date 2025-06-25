:tocdepth: 2

What's new?
===========

.. contents::
   :local:
   :backlinks: none
   :depth: 1

.. Next release
.. ============
.. Next release
.. ============

v0.9.6 (2025-06-12)
-------------------
* Enriched transition rules from DAT to BED
* Described access rules to BED
* Removed rvsn_rsn measure from every accounting table
* Removed comment table
* Minor restructuring of the ELFUND documentation
* Updated schemas, data models, templates and examples

v0.9.5 (2025-06-02)
-------------------
* Added riad to dbdat transformation and workflow
* Added csdb to dbdat transformation and workflow
* Enriched APA checks
* Added rvsn_rsn measure to every accounting table
* Added comment table
* Added FM and EXR tables in DBDAT
* Refactor ELFUND documentation structure
* Removed TIMESTAMP variable in DAT (will be added in DAT to BED transfromation)
* New version of IFDAT to DAT transformation
* Regenerated schemas, datamodels, structure, examples

v0.9.4 (2025-05-26)
-------------------
* Improve regex for identifiers
* Rename OA to OAID in DAT:REF.DPST and DAT:REF.LN 
* Fix max_length for string vars
* Forbid extra variables in json schemas
* Enrich examples

v0.9.3 (2025-05-19)
-------------------
* Fix max_length for string vars
* Reintroduce Reports: Database report, IFDATFULL report, IFDAT_SNAPSHOT report
* Enrich examples
* Introduce acq (for incoming files) and ack (for validation reports - APA)
* Jump to v0.9.3 to allign with IFDAT versions

v0.6.0 (2025-05-16)
-------------------
* Update data models and json schemas to not allow reseting IFDAT variables that will cause calls to the BED database
* Fix bugs in schemas
* Remove checks in the transformation from IFDAT and DBDAT to DAT

v0.5.0 (2025-05-01)
-------------------
* Describe transformations between IFDAT and DBDAT to DAT

v0.4.1 (2025-01-31)
-------------------
* Update IFDAT schema based on IFDAT version 0.9.1

v0.4.0 (2025-01-15)
-------------------
* Refactor acknowledgment schema (ΑΠΑ)
* Improve validation documentation
* DBDAT and IFDAT schemas based on IFDAT version 0.9.0

v0.3.7 (2024-10-08)
-------------------
* Improve regex patterns
* Improve data model and thus update json datamodel schemas
* Json schemas modified due to the above
* Improve IFDAT documentation

v0.3.6 (2024-09-23)
-------------------

* Enhance examples and reports 

v0.3.5 (2024-07-25)
-------------------

* Use datatime format rather than date format 
* Improve test data 
* Introduce reports based on test data

v0.3.4 (2024-07-08)
-------------------

* Modified json schema according to discussions with IT department

v0.3.3 (2024-05-20)
-------------------
* Created compact json schemas
* Collapse categories into tables
* Improve excel data structure
* Modified examples to be used with the compact json schemas
* Other fixes
* ReadTheDocs Documentation not yet changed to reflect the above changes 

v0.3.2 (2024-04-24)
-------------------

* Modified json schema so that anyof does not appear.

v0.3.1 (2024-04-24)
-------------------

* Added DBDat documentation
* Refactored index page
* Added test data
* Added validation section

v0.3.0 (2024-02-29)
-------------------

* Update DBDat model
* Refactored excel data models and improved the json schemas
* Added acknowledgment schema
* Added openapi backend schema
* Other improvements

v0.2.0 (2023-09-21)
-------------------

* Update DBDat and IFDat models after extensive consultations (see also respective changes in IFDat documentation).
* Build documentation in pdf, epub and word
* Minor fixes

v0.1.2 (2023-04-25)
-------------------

* Merge static string tables in ref category of DBDat

v0.1.1 (2023-04-21)
-------------------

* Small fix to initial release

v0.1.0 (2023-04-21)
-------------------

* Initial release
