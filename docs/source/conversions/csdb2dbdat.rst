
Μετατροπή CSDB σε DBDAT (σε DAT, σε BED)
========================================

Προγραμματισμένη Εκτέλεση
-------------------------

Η διαδικασία πραγματοποιείται κάθε φορά που ανεβαίνουν στο \\srv-041-as1\exdi_csdb τα μηνιαία extraction files της CSDB καθώς και τα delta extraction files και η διαδικασία ξεκινάει να τρέχει στις 23:00.  Στο header του DBDAT αρχείου συμπληρώνεται:

* PARTNER = 'CSDB'
* USERNAME = 'CSDB_USER'
* SOURCE = 'REG'
* DOMAIN = 'DBDAT'


Εντοπισμός Τίτλων Ενδιαφέροντος
-------------------------------

Οι τίτλοι εντοπίζονται στους πίνακες `REF.SHR_ALIAS (RID), REF.DBT_ALIAS (RID), ACC.ASST_SHR (IID)`, `ACC.HLDR (IID)`, `ACC.ASST_DBT(IID)`, και `ACC.ASST_LBLTY (IID)` του BED.  Διατηρούνται μόνο οι μοναδικοί κωδικοί με πρόθεμα Ι και το σύνολο των κωδικών ονομάζεται ως ISIN_IDS. 



Διατήρηση εγγραφής
------------------

Η διαδικασία αυτή τρέχει για κάθε σειρά-εγγραφή του CSDB zip-csv Extraction FILE ανεξάρτητα αν το αρχείο είναι τύπου DBT ή SHR όπου ως ΧΧΧ αναφερεται το είδος του αρχείου.

Η εγγραφή του αρχείου επεξεργάζεται αν το πεδίo `ISIN code` (με πρόθεμα Ι) είτε ξεκινάει με GR ή ανήκει στο σύνολο ISIN_IDS.  

*Σημείωση*:  Για τη συνέχεια όπου αναφέρεται ISIN εννοείται η τιμή του πεδίου `ISIN code` με πρόθεμα το 'I'.

*Σημείωση*:  Τα πεδία με ημερομηνίες μετατρέπονται σε datetime ημερομηνίες με την ώρα να ορίζεται ως 00:00:00Z.


Εύρεση ESCB_ID και προσθήκη στον πίνακα DBDAT:REF.ORG2ΧΧΧ
---------------------------------------------------------

Αντλείται το `RIAD code` και δεν είναι κενό προστίθεται στον πίνακα DBDAT:REF.ORG2XXX με LID=RIAD code (με πρόθεμα "Ε"), RID=ISIN και ISSR_OF=T.


Διαδικασία επεξεργασίας DBT αρχείου
-----------------------------------

Συμπληρωση του πίνακα DBDAT:REF.DBT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλούνται αν δεν είναι κενά τα πεδία `Issue date` και `Maturity date` μετονομάζονται σε DT_BRTH, DT_CLS, ORGNL_MTRTY=DT_CLS και εισάγονται στον πίνακα DBDAT:REF.DBT με ID=ISIΝ.


Συμπληρωση του πίνακα DBDAT:REF.DBT_DYNMC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλούνται αν δεν είναι κενά τα πεδία `Short name`, `CFI classification`, `Nominal currency`, `Primary asset classification 2`, `Security Status`, `Maturity date`, `Issue price`, `Redemption price`, `Accrual start date`, `Price value type`, `Amount Outstanding type` μετατρέπονται σε NM_SHRT, CFI, CRRNCY, TYP (TODO MAP RULES), STTS (TODO MAP RULES), MTRTY_DT, ISS_PRC, RDMPTN_PRC, ACCRL_STRTDT, PRC_TYP, AMNT_OTSTDNG_TYP και εισάγονται στον πίνακα DBDAT:REF.DBT_DYNCM με ID=ISIN και VLD_FRM=`Extraction date`.


Συμπληρωση του πίνακα DBDAT:REF.DBT_PRC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλούνται αν δεν είναι κενά τα πεδία `Price date`, `Price value`, `Quotation basis`, `Accrued interest`, `Amount Outstanding`. Δημιουργούνται μία ή δύο εγγραφές στον πίνακα DAT:REF.DBT_PRC ανάλογα με τις παρακάτω περιπτώσεις. 

* Περίπτωση Α: `Extraction date`=`Price date` μία εγγραφή:

  1. ID=ISIN, DT=Price date, PRC=Price value, ACCRD_INTRST=Accrued interest, OTSTDNG=Amount Outstanding, PRC.STATUS=Quotation basis(TODO MAP RULES)

* Περίπτωση B: `Extraction date`!=`Price date` δύο εγγραφές:

  1. ID=ISIN, DT=Price date, PRC=Price value, PRC.STATUS=Quotation basis(TODO MAP RULES)
  2. ID=ISIN, DT=Extraction date, ACCRD_INTRST=Accrued interest, OTSTDNG=Amount Outstanding

Διαδικασία επεξεργασίας SHR αρχείου
-----------------------------------

Συμπληρωση του πίνακα DBDAT:REF.SHR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλείται αν δεν είναι κενό το `Issue date` μετονομάζεται σε DT_BRTH και εισάγεται στον πίνακα DBDAT:REF.SHR με ID=ISIΝ.


Συμπληρωση του πίνακα DBDAT:REF.SHR_DYNMC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλούνται αν δεν είναι κενά τα πεδία `Short name`, `CFI classification`, `Nominal currency`, `Primary asset classification 2`, `Security Status`, `Issue price`, `Price value type`, `Amount Outstanding type`, `Instrument ESA 2010 class - value type` μετατρέπονται σε NM_SHRT, CFI, CRRNCY, TYP (TODO MAP RULES), STTS (TODO MAP RULES), ISS_PRC, PRC_TYP, AMNT_OTSTDNG_TYP, ESA_TYP (TODO MAP RULES) και εισάγονται στον πίνακα DBDAT:REF.DBT_DYNCM με ID=ISIN και VLD_FRM=`Extraction date`.


Συμπληρωση του πίνακα DBDAT:REF.SHR_DVDND
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλούνται αν δεν είναι κενά τα πεδία `Dividend settlement date`, `Ex Dividend Date`, `Dividend frequency`, `Dividend currency`, `Dividend_income amount type`, `Dividend amount` μετατρέπονται σε DT, EX_DT, FRQNCY, AMNT, CRRNCY, TYP, AMNT και εισάγονται στον πίνακα DBDAT:REF.SHR_DVDND με ID=ISIN.

Συμπληρωση του πίνακα DBDAT:REF.SHR_SPLT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλούνται αν δεν είναι κενά τα πεδία `Last split date`, `Last split factor` μετατρέπονται σε DT, FCTRκαι εισάγονται στον πίνακα DBDAT:REF.SHR_SPLT με ID=ISIN.


Συμπληρωση του πίνακα DBDAT:REF.SHR_PRC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Αντλούνται αν δεν είναι κενά τα πεδία `Price date`, `Price value`, `Quotation basis`, `Amount Outstanding` και δημιουργείται εγγραφή στον πίνακα DAT:REF.SHR_PRC ως εξής: 

ID=ISIN, DT=Price date, PRC=Price value, OTSTDNG=Amount Outstanding, PRC.STATUS=Quotation basis (TODO MAP RULES)
