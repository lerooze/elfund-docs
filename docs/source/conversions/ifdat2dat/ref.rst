Κανόνες μετατροπής πινάκων REF του IFDAT σε πίνακες REF του DAT
===============================================================

Οι παρακάτω κανόνες δίνονται με τρόπο ώστε να είναι σαφής η περιγραφή τους.  Η
υλοποίηση των κανόνων μπορεί να διαφέρει από τη σειρά και τον τρόπο που
παρουσιάζονται οι κανόνες αφού κάποιοι κανόνες που παρουσιάζονται σειριακά
μπορούν να υλοποιηθούν και παράλληλα.

IFDAT:REF.RA
------------

ΒΑΣΙΚΕΣ ΜΕΤΡΗΣΕΙΣ
~~~~~~~~~~~~~~~~~

Διαγράφονται οι μετρήσεις LEI_ID, TAX_ID, NBR_ID και αν το αποτέλεσμα περιέχει συμπληρωμένες *μετρήσεις* μεταφέρεται στον πίνακα DAT:REF.ORG.


ΑΝΑΓΝΩΡΙΣΤΙΚΟΙ ΚΩΔΙΚΟΙ
~~~~~~~~~~~~~~~~~~~~~~

Διατηρείται η διάσταση ID και οι μετρήσεις LEI_ID, TAX_ID, NBR_ID. Αν στις τιμές των μετρήσεων δεν περιλαμβάνονται συμπληρωμένες τιμές η επεξεργασία σταματάει.  Αν υπάρχουν συμπληρωμένες μετρήσεις τότε στην τιμή προστίθεται το πρόθεμα 'L', 'T', 'B' για τις μετρήσεις LEI_ID, TAX_ID, NBR_ID αντίστοιχα.

Η παρακάτω διαδικασία ακολουθείται για κάθε μέτρηση LEI_ID, TAX_ID, NBR_ID όπου ως P ορίζεται το πρόθεμα του αναγνωριστικού κωδικού και ως OID το όνομα της μέτρησης:

H μεταβλητή OID μετονομάζεται σε LID, η μεταβλητή RID μετονομάζεται σε ID και προστίθεται η τιμή ALIAS_OF='T' και μεταφέρονται στον πίνακα DAT.ORG_ALIAS. 

Ακολουθεί παράδειγμα από IFDAT σε DAT:

.. csv-table:: 
   :header: "ID", "DT_BRTH", "DT_CLS", "LEI_ID", "TAX_ID", "NBR_ID", "SPLT_FRM", "MRGD_WTH"
   :widths: 15, 12, 12, 25, 12, 20, 12, 12

   EGR123456789, 2024-09-01, , 987600ED3C2BA1B01C23, , GR987654321000, , 

.. csv-table:: 
   :header: "LID", "RID", "ALIAS_OF", "ALIAS_OF.STATUS"
   :widths: 30, 20, 15, 20

   L987600ED3C2BA1B01C23, EGR123456789, T, 
   BGR987654321000, EGR123456789, T, 


IFDAT:REF.RA_DYNMC
------------------
Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.ORG_DYNMC.


IFDAT:REF.FND
-------------
Ακολουθούνται οι οδηγίες του πίνακα REF.RA.


IFDAT:REF.FND_DYNMC
-------------------

ΒΑΣΙΚΕΣ ΜΕΤΡΗΣΕΙΣ
~~~~~~~~~~~~~~~~~

Διαγράφονται οι μεταβλητές RPRTD_BY, MNGD_BY, UNDR_UMBRLL_BY. Μετονομάζονται οι μεταβλητές LGL_TYP, INVSTMNT_PLCY, DSTRBTN_PLCY, INVSTR_TYP, GRN_TYP, STRTGY, GGRPHCL_FCS, BND_FCS, RL_ESTT_TYP προσθέτοντας το πρόθεμα FND\_.  Η μεταβλητή IFDAT:REF.FND_DYNMC.EQT_TYP μετατρέπεται σε DAT:REF.ORG_DYNMC.INSTTNL_SCTR_DTL ως εξής: OPEN=S124_A, CLOSE=S124_B και η τιμή της αρχικοποίησης δεν αλλάζει.  Η μεταβλητή DAT:REF.ORG_DYNMC.INSTTTNL_SCTR συμπληρώνεται από τη μεταβλητή IFDAT:REF.FND_DYNMC.INVSTMNT_PLCY ως εξής: λαμβάνει την τιμή S124 εκτός αν INVSTMNT_PLCY=MMF όπου λαμβάνει την τιμή S123 ή αν έχει την τιμή της αρχικοποίησης οπότε τη διατηρεί. Το αποτέλεσμα μεταφέρεται στον πίνακα DAT:REF.ORG_DYNMC.

ΜΕΤΡΗΣΕΙΣ ΣΧΕΣΕΩΝ
~~~~~~~~~~~~~~~~~
Η παρακάτω διαδικασία ακολουθείται για κάθε μεταβλητή RPRTD_BY, MNGD_BY, UNDR_UMBRLL_BY και οι διαστάσεις (ID, VLD_FRM, VLD_T) πάντα παραμένουν.  Για τη διευκόλυνση της επεξήγησης τη μεταβλητή της σχέσης την ονομάζουμε LINK_ID.  Οι μεταβλητές αυτές αντίστοιχα στον πίνακα DAT:REF.ORG2ORG είναι οι IFDAT_RPRTR_OF, MNGMNT_OF, UMBRELL_OF και για διευκόλυνση της επεξήγησης θα την ονομάσουμε DAT_LINK_ID (Παράδειγμα 3).  Υπάρχουν τρεις περιπτώσεις μετατροπής.  Στους πίνακες των παραδειγμάτων που ακολουθούν δεν περιλαμβάνονται οι βασικές μεταβλητές (SRC_TYP, SRC_ORG, SRC_USR, TIMESTAMP) των πινάκων DAT.


Περίπτωση 1
"""""""""""
Αν για συμπληρωμένο ID και LINK_ID, έχω VLD_FRM=ΚΕΝΟ και VLD_Τ=ΚΕΝΟ τότε δημιουργείται μια εγγραφή:

LID=LINK_ID, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=ΚΕΝΟ, DAT_LINK_ID=T 

και μεταφέρεται στο πίνακα DAT:REF.ORG2ORG.  Ακολουθεί παράδειγμα από IFDAT σε DAT:

Αρχικός IFDAT πίνακας:

.. csv-table::
   :header: "ID", "VLD_FRM", "VLD_T", "RPRTD_BY"
   :widths: 30, 12, 12, 20

   PEGR123456789_AKES, , , EGR123456789

Μετασχηματισμένος Πίνακας DAT:

.. csv-table::
   :header: "LID", "RID", "VLD_FRM", "VLD_T", "MNGMNT_OF", "UMBRLL_OF", "IFDAT_RPRTR_OF"
   :widths: 25, 30, 12, 12, 12, 12, 18

   EGR123456789, PEGR123456789_AKES, , , , , T

.. csv-table::
   :header: "ID", "VLD_FRM", "VLD_T", "RPRTD_BY"
   :widths: 30, 12, 12, 20

   PEGR123456789_AKES2, 2024-06-15, 2025-04-10, EGR123456789

Μετασχηματισμένος Πίνακας (DAT:REF.ORG2ORG):

.. csv-table::
   :header: "LID", "RID", "VLD_FRM", "VLD_T", "MNGMNT_OF", "UMBRLL_OF", "IFDAT_RPRTR_OF"
   :widths: 25, 30, 12, 12, 12, 12, 18

   EGR123456789, L787600ED3C2BA1B01C45, , 2025-02-01, , , T
   EGR123456789, L787600ED3C2BA1B01C45, 2025-02-01, , , , F
   EGR123456789, PEGR123456789_AKES2, 2024-06-15, 2025-04-10, , , T
   EGR123456789, PEGR123456789_AKES2, , 2024-06-15, , , F
   EGR123456789, PEGR123456789_AKES2, 2025-04-10, , , , F


Περίπτωση 2
"""""""""""
Αν για συμπληρωμένο ID και LINK_ID, έχω VLD_FRM=YYYY-MM-DD και VLD_Τ=ΚΕΝΟ τότε δημιουργούνται δύο εγγραφές:

* LID=LINK_ID, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, DAT_LINK_ID=F
* LID=LINK_ID, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ=ΚΕΝΟ, DAT_LINK_ID=T

και μεταφέρεται στο πίνακα DAT:REF.ORG2ORG.  Ακολουθεί παράδειγμα από IFDAT σε DAT:

Αρχικός IFDAT πίνακας:

.. csv-table::
   :header: "ID", "VLD_FRM", "VLD_T", "RPRTD_BY"
   :widths: 30, 12, 12, 20

   L887600ED3C2BA1B01C34, 2025-01-01, , EGR123456789

Μετασχηματισμένος Πίνακας DAT:

.. csv-table::
   :header: "LID", "RID", "VLD_FRM", "VLD_T", "MNGMNT_OF", "UMBRLL_OF", "IFDAT_RPRTR_OF"
   :widths: 25, 30, 12, 12, 12, 12, 18

   EGR123456789, L887600ED3C2BA1B01C34, , 2025-01-01, , , F
   EGR123456789, L887600ED3C2BA1B01C34, 2025-01-01, , , , T

Περίπτωση 3
"""""""""""
Αν για συμπληρωμένο ID και LINK_ID, έχω VLD_FRM=ΚΕΝΟ και VLD_Τ=YYYY-MM-DD τότε δημιουργούνται δύο εγγραφές:

* LID=LINK_ID, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, DAT_LINK_ID=T
* LID=LINK_ID, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ=ΚΕΝΟ, DAT_LINK_ID=F

και μεταφέρεται στο πίνακα DAT:REF.ORG2ORG.  Ακολουθεί παράδειγμα από IFDAT σε DAT:

Αρχικός IFDAT πίνακας:

.. csv-table::
   :header: "ID", "VLD_FRM", "VLD_T", "RPRTD_BY"
   :widths: 30, 12, 12, 20

   L787600ED3C2BA1B01C45, , 2025-02-01, EGR123456789

Μετασχηματισμένος Πίνακας DAT:

.. csv-table::
   :header: "LID", "RID", "VLD_FRM", "VLD_T", "MNGMNT_OF", "UMBRLL_OF", "IFDAT_RPRTR_OF"
   :widths: 25, 30, 12, 12, 12, 12, 18

   EGR123456789, L787600ED3C2BA1B01C45, , 2025-02-01, , , T
   EGR123456789, L787600ED3C2BA1B01C45, 2025-02-01, , , , F

Περίπτωση 4 
"""""""""""
Αν για συμπληρωμένο ID και LINK_ID, έχω VLD_FRM=YYYY-MM-DD και VLD_Τ=ΕΕΕΕ-ΜΜ-ΗΗ τότε δημιουργούνται τρεις εγγραφές:

* LID=LINK_ID, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ=ΕΕΕΕ-ΜΜ-ΗΗ, DAT_LINK_ID=T
* LID=LINK_ID, RID=ID, VLD_FRM=ΕΕΕΕ-ΜΜ-ΗΗ, VLD_Τ=ΚΕΝΟ, DAT_LINK_ID=F
* LID=LINK_ID, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, DAT_LINK_ID=F

και μεταφέρεται στο πίνακα DAT:REF.ORG2ORG.  Ακολουθεί παράδειγμα από IFDAT σε DAT:

Αρχικός IFDAT πίνακας:

.. csv-table::
   :header: "ID", "VLD_FRM", "VLD_T", "RPRTD_BY"
   :widths: 30, 12, 12, 20

   PEGR123456789_AKES2, 2024-06-15, 2025-04-10, EGR123456789

Μετασχηματισμένος Πίνακας DAT:

.. csv-table::
   :header: "LID", "RID", "VLD_FRM", "VLD_T", "MNGMNT_OF", "UMBRLL_OF", "IFDAT_RPRTR_OF"
   :widths: 25, 30, 12, 12, 12, 12, 18

   EGR123456789, PEGR123456789_AKES2, 2024-06-15, 2025-04-10, , , T
   EGR123456789, PEGR123456789_AKES2, , 2024-06-15, , , F
   EGR123456789, PEGR123456789_AKES2, 2025-04-10, , , , F


IFDAT:REF.SELF_DBT
------------------

Διατηρούνται οι μετρήσεις DT_BRTH, DT_CLS, ORGNL_MTRTY, UNDRLYNG, RSTRCTRD_T, RSTRCTRD_FRM και αν έχουν συμπληρωμένες τιμές μεταφέρονται μαζί με τη διάσταση ID στον πίνακα DAT:REF.DBT

Διαγράφονται οι μετρήσεις DT_BRTH, DT_CLS, ORGNL_MTRTY, UNDRLYNG, RSTRCTRD_T, RSTRCTRD_FRM και αν έχουν συμπληρωμένες τιμές μεταφέρονται μαζί με τη διάσταση ID στον πίνακα DAT:REF.DBT_DYNMC


IFDAT:REF.SELF_DBT_DYNMC
------------------------

Διαγράφεται η μέτρηση ISSD_BY και αν υπάρχουν συμπληρωμένες παρατηρήσεις μεταφέρονται στον πίνακα DAT:REF.DBT_DYNMC.

Διατηρείται η μέτρηση ISSD_BY και αν είναι συμπληρωμένη για την μετατροπή του ισχύουν οι παρακάτω περιπτώσεις:


Περίπτωση 1
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=ΚΕΝΟ και VLD_Τ=ΚΕΝΟ τότε δημιουργείται μια εγγραφή: 

LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=ΚΕΝΟ, ISSR_OF=T 

και μεταφέρεται στο πίνακα DAT:REF.ORG2DBT.


Περίπτωση 2
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=YYYY-MM-DD και VLD_Τ=ΚΕΝΟ τότε δημιουργούνται δύο εγγραφές:

LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, ISSR_OF=F
LID=ISSD_BY, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ=ΚΕΝΟ, ISSR_OF=T

και μεταφέρεται στο πίνακα DAT:REF.ORG2DBT.


Περίπτωση 3
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=ΚΕΝΟ και VLD_Τ=YYYY-MM-DD τότε δημιουργούνται δύο εγγραφές:

LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, ISSR_OF=T
LID=ISSD_BY, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ= ΚΕΝΟ, ISSR_OF=F

και μεταφέρεται στο πίνακα DAT:REF.ORG2DBT.


Περίπτωση 4
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=YYYY-MM-DD και VLD_Τ=ΕΕΕΕ-ΜΜ-ΗΗ τότε δημιουργούνται τρεις εγγραφές:

LID=ISSD_BY, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ=ΕΕΕΕ-ΜΜ-ΗΗ, ISSR_OF=T
LID=ISSD_BY, RID=ID, VLD_FRM=ΕΕΕΕ-ΜΜ-ΗΗ, VLD_Τ=ΚΕΝΟ, ISSR_OF=F
LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, ISSR_OF=F

και μεταφέρεται στο πίνακα DAT:REF.ORG2DBT.



IFDAT:REF.SELF_DBT_OUTSTNDNG_CHNG
---------------------------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.DBT_OUTSTNDNG_CHNG 


IFDAT:REF.SELF_DBT_CPN
----------------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.DBT_CPN

IFDAT:REF.SELF_SHR
------------------

Διατηρούνται οι μετρήσεις DT_BRTH, DT_CLS, RSTRCTRD_T και αν έχουν συμπληρωμένες τιμές μεταφέρονται μαζί με τη διάσταση ID στον πίνακα DAT:REF.SHR

Διαγράφονται οι μετρήσεις DT_BRTH, DT_CLS, RSTRCTRD_T και αν έχουν συμπληρωμένες τιμές μεταφέρονται μαζί με τη διάσταση ID στον πίνακα DAT:REF.SHR_DYNMC


IFDAT:REF.SELF_SHR_DYNMC
------------------------

Διαγράφεται η μέτρηση ISSD_BY και αν υπάρχουν συμπληρωμένες παρατηρήσεις μεταφέρονται στον πίνακα DAT:REF.SHR_DYNMC.

Διατηρείται η μέτρηση ISSD_BY και αν είναι συμπληρωμένη για την μετατροπή του ισχύουν οι παρακάτω περιπτώσεις:


Περίπτωση 1
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=ΚΕΝΟ και VLD_Τ=ΚΕΝΟ τότε δημιουργείται μια εγγραφή: 

LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=ΚΕΝΟ, ISSR_OF=T 

και μεταφέρεται στο πίνακα DAT:REF.ORG2SHR.


Περίπτωση 2
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=YYYY-MM-DD και VLD_Τ=ΚΕΝΟ τότε δημιουργούνται δύο εγγραφές:

LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, ISSR_OF=F
LID=ISSD_BY, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ=ΚΕΝΟ, ISSR_OF=T

και μεταφέρεται στο πίνακα DAT:REF.ORG2SHR.


Περίπτωση 3
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=ΚΕΝΟ και VLD_Τ=YYYY-MM-DD τότε δημιουργούνται δύο εγγραφές:

LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, ISSR_OF=T
LID=ISSD_BY, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ= ΚΕΝΟ, ISSR_OF=F

και μεταφέρεται στο πίνακα DAT:REF.ORG2SHR.


Περίπτωση 4
~~~~~~~~~~~

Αν για συμπληρωμένο ID και ISSD_BY, έχω VLD_FRM=YYYY-MM-DD και VLD_Τ=ΕΕΕΕ-ΜΜ-ΗΗ τότε δημιουργούνται τρεις εγγραφές:

LID=ISSD_BY, RID=ID, VLD_FRM=YYYY-MM-DD, VLD_Τ=ΕΕΕΕ-ΜΜ-ΗΗ, ISSR_OF=T
LID=ISSD_BY, RID=ID, VLD_FRM=ΕΕΕΕ-ΜΜ-ΗΗ, VLD_Τ=ΚΕΝΟ, ISSR_OF=F
LID=ISSD_BY, RID=ID, VLD_FRM=ΚΕΝΟ, VLD_Τ=YYYY-MM-DD, ISSR_OF=F

και μεταφέρεται στο πίνακα DAT:REF.ORG2SHR.

IFDAT:REF.SELF_SHR_DVDND
------------------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.SHR_DVDND


IFDAT:REF.SELF_SHR_SPLT
-----------------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.SHR_SPLT

IFDAT:REF.CNTRPRTY
------------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.ORG_DYNMC


IFDAT:REF.DPST
--------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.DPST

IFDAT:REF.LN
------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.LN


IFDAT:REF.DBT
-------------

Διαγράφεται η μέτρηση ISSD_BY και αν υπάρχουν συμπληρωμένες παρατηρήσεις μεταφέρονται στον πίνακα DAT:REF.DBT_DYNMC

Διατηρείται η μέτρηση ISSD_BY και αν είναι συμπληρωμένη μετονομάζεται σε LID, το ID μετονομάζεται σε RID και προσθέτεται ISSR_OF=T και όλες οι μεταβλητές μεταφέρονται στο πίνακα DAT:REF.ORG2DBT όπου το VLD_FRM=KENO και το VLD_TO=KENO.

IFDAT:REF.SHR
-------------

Διαγράφεται η μέτρηση ISSD_BY, μετονομάζεται η μεταβλητή TYP σε ESA_TYP και αν υπάρχουν συμπληρωμένες παρατηρήσεις μεταφέρονται στον πίνακα DAT:REF.SHR_DYNMC

Διατηρείται η μέτρηση ISSD_BY και αν είναι συμπληρωμένη μετονομάζεται σε LID, το ID μετονομάζεται σε RID και προσθέτεται ISSR_OF=T και όλες οι μεταβλητές μεταφέρονται στο πίνακα DAT:REF.ORG2SHR όπου το VLD_FRM=KENO και το VLD_TO=KENO.

IFDAT:REF.DER
-------------

Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.DER

IFDAT:REF.DRGTN
---------------
H μεταβλητή DRGTN_TYPE μετονομάζεται σε IFDAT_DRGTN_TYPE και ο πίνακας μεταφέρεται στο DAT:REF.DRGTN

IFDAT:REF.CMMNT
---------------
Μεταφέρεται αυτούσιος στον πίνακα DAT:REF.CMMNT
