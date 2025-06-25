
Μετατροπή RIAD σε DBDAT (σε DAT, σε BED)
========================================

Προγραμματισμένη Εκτέλεση
-------------------------

Η διαδικασία πραγματοποιείται κάθε εργάσιμη μέρα στις 05:00:00.


Εντοπισμός Οντοτήτων Ενδιαφέροντος
----------------------------------

Οι οντότητες εντοπίζονται στους πίνακες `REF.ORG_DYNMC (ID)`, `REF.ORG2ORG (LID, RID)`, `REF.ORG2SHR (LID)`, και `REF.ORG2DBT (LID)` του BED. Επιλέγονται όλα τα μοναδικά `ORG_IDS` με `TIMESTAMP` μετά τις 5μμ της προηγούμενης εργάσιμης μέρας.

**Σημείωση**: Κατά την πρώτη εκτέλεση επιλέγονται όλες οι εγγραφές.

Για σκοπούς της επεξήγησης υποθέτουμε ότι το σύνολο των ORG_IDS που εντοπίστηκαν είναι τo ακόλουθo:
{TFI00180910,B0018091-0,BAU149 440 291,EGRAEAAP005,L213800XML1JT6Y7RV779}



Εύρεση και Αντικατάσταση με ESCB_ID
-----------------------------------

Για όσα `ORG_IDS` δεν έχουν πρόθεμα "Ε", αντλείται η τελευταία AUTH έκδοση με LID=ORG_IDS χωρίς πρόθεμα "Ε" και ALIAS_OF=TRUE από τον πίνακα DAT:REF.ORG_ALIAS.  Τα RIDs που εντοπίζονται αποτελούν τα ESCB_IDS και χρησιμοποιούνται για να αντικαταστήσουν τα ORG_IDS χωρίς το πρόθεμα "E" με το ESCB_ID που βρέθηκε.

Για παράδειγμα: 

.. csv-table::
   :header: "LID", "RID", "ALIAS_OF"
   :widths: 25, 30, 12

   L213800XML1JT6Y7RV779, EGRAK01049, T 

Τότε το νέο σύνολο των ORG_IDS είναι το ακόλουθο:

{TFI00180910,B0018091-0,BAU149 440 291,EGRAEAAP005,EGRAK01049}

Για τα ORG_IDS που παραμένουν χωρίς πρόθεμα E και χωρίς το πρόθεμα P αναζητείται ο ESCB_ID στο
ESCB RIAD RESTful web service κάνοντας χρήση του παρακάτω πίνακα για να μετατραπεί το ORG_ID σε `typ_entty_cd/entty_cd`:

.. csv-table::
   :file: /_static/conversions/RIAD_TRIPLETS.csv
   :header-rows: 1
   :widths: auto

Από το σύνολο των ORG_IDS οι περιπτώσεις που μας ενδιαφέρουν είναι οι ακόλουθοι:

{TFI00180910,B0018091-0,BAU149 440 291}

Περίπτωση 1:
~~~~~~~~~~~~

Κωδικός: `TFI00180910`

- Τύπος: *tax-id* (αρχικό: `T`)
- Χώρα: Φινλανδία (FI)

.. code-block:: text

    TYPE               COUNTRY             DAT_PREFIX        INCLUDE_CC
    FI_ALV_CD          FI                  T                 T

**Ερώτημα στο RIAD RESTful web service:**

.. code-block:: text

    rp=entty_riad_cd&fe.identifier.entityIdentifier.in=FI_ALV_CD/FI00180910


Περίπτωση 2:
~~~~~~~~~~~~

Κωδικός: `ΒFI0018091-0`

- Τύπος: *business-id* (αρχικό: `B`)
- Χώρα: Φινλανδία (FI)

.. code-block:: text

    TYPE               COUNTRY             DAT_PREFIX        INCLUDE_CC
    FI_Y_CD            FI                  B                 FALSE

**Ερώτημα στο RIAD RESTful web service:**

.. code-block:: text

    rp=entty_riad_cd&fe.identifier.entityIdentifier.in=FI_Y_CD/0018091-0


Περίπτωση 3:
~~~~~~~~~~~~
Κωδικός: `ΒAU 149 440 291`.

- Τύπος: *business-id* (αρχικό: `B`)
- Χώρα: Αυστραλία (AU)

.. code-block:: text

    TYPE               COUNTRY             DAT_PREFIX        INCLUDE_CC
    AU_ABN_CD          AU                  B                 FALSE
    AU_ACN_CD          AU                  B                 FALSE

**Ερώτημα στο RIAD RESTful web service:**

.. code-block:: text

    rp=entty_riad_cd&fe.identifier.entityIdentifier.in=AU_ABN_CD/149 440 291,AU_ACN_CD/149 440 291


Ολοκληρωμένο QUERY
------------------

Το ακόλουθο RIAD ερώτημα ενσωματώνει όλες τις περιπτώσεις:

.. code-block:: text

    https://<host>/wsrest/orgunits/sdd/extended/4.7/full?rp=entty_riad_cd&fe.identifier.entityIdentifier.in=FI_ALV_CD/FI00180910,FI_Y_CD/0018091-0,AU_ABN_CD/149 440 291,AU_ACN_CD/149 440 291

Επιστρέφει το ακόλουθο (pretty-printed) απόσπασμα:

.. literalinclude:: /_static/conversions/aliases.xml
   :language: XML

Το οποίο μετατρέπεται σε DBDAT ως εξής:

.. literalinclude:: /_static/conversions/aliases.json
   :language: JSON

Το DBDAT αρχείο μετατρέπεται σε DAT με βάση τους κανόνες μετατροπής από DBDAT σε DAT για να φορτωθεί στη BED.

Τελικό σύνολο ORG_IDS
---------------------
Μετά την κλήση στο RIAD RESTful web service το σύνολο των ORG_IDS διαμορφώνεται ως εξής αφού αφαιρεθεί το πρόθεμα "E":

RIAD_CODES = {FI00180910,AUECBM876961,GRAEAAP005,GRAK01049}

Άντληση στοιχείων αναφοράς ORG και ORG_DYNMC
--------------------------------------------
Για τα RIAD_CODES αντλούμαι τα παρακάτω στοιχεία αναφοράς από το ORGUNITS/EXTENDED/4.7/ORG_DYNMC endpoint: entty_riad_cd, bsnss_vld_frm, bsnss_vld_t, dt_brth, dt_cls, instttnl_sctr, nm_entty, cntry.  Επιλέγεται το variant=updates εκτός της πρώτης κλήσης που επιλέγεται το variant=full. 

**Σημείωση**: Προσθέτουμε στα bsnss_vld_t και dt_cls πάντα μία μέρα στην μετατροπή σε DBDAT εκτός αν είναι ίσα με 9999-12-31 και στην περίπτωση αυτή οι μεταβλητές VLD_T και DT_CLS δεν συμπληρώνονται. 

Παράδειγμα κλήσης:
~~~~~~~~~~~~~~~~~~

.. code-block:: text

    https://<host>/wsrest/orgunits/sdd/extended/4.7/full?rp=entty_riad_cd,bsnss_vld_frm,bsnss_vld_t,dt_brth,dt_cls,instttnl_sctr,nm_entty,cntry&fe.entty_riad_cd.in=FI00180910,AUECBM876961,GRAEAAP005,GRAK01049

Επιστρέφει το ακόλουθο (pretty-printed) απόσπασμα:

.. literalinclude:: /_static/conversions/output.xml
   :language: XML

Το οποίο μετατρέπεται σε αρχείο DBDAT ως εξής (incomplete conversion):

.. literalinclude:: /_static/conversions/aliases.json
   :language: JSON

Το DBDAT αρχείο μετατρέπεται σε DAT με βάση τους κανόνες μετατροπής από DBDAT σε DAT για να φορτωθεί στη BED.


Άντληση εταιρικών πράξεων για συμπλήρωση του πίνακα DBDAT:REF.ORG 
------------------------------------------------------------------
Από την προηγούμενη κλήση γίνεται αντιστοίχηση μεταξύ entty_riad_cd και entty_riad_id και δημιουργείται το ακόλουθο σύνολο:

RIAD_IDS={21974339,106072,23249498,18061578}


Για τα RIAD_IDS αντλούμαι τα παρακάτω στοιχεία αναφοράς από το events/sdd endpoint: ακόλουθες μεταβλητές: src_entty_riad_id, trgt_entty_riad_id, dt_evnt, typ_evnt.  Επιλέγεται το variant=updates/{PREVIOUS_BUSINESS_DAY} εκτός της πρώτης κλήσης που επιλέγεται το variant=full.  Γίνονται δύο κλήσεις μία με filter το src_entty_riad_id και μία με filter το trgt_entty_riad_id.


Παράδειγμα κλήσης με φίλτρο src_entty_riad_id:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    https://<host>/wsrest/events/sdd/full?rp=src_entty_riad_id,trgt_entty_riad_id,dt_evnt,typ_evnt&f.src_entty_riad_id.in=21974339,106072,23249498,18061578

Επιστρέφει το ακόλουθο (pretty-printed) απόσπασμα:

.. literalinclude:: /_static/conversions/events_src.xml
   :language: XML


To σύνολο των trgt_entty_riad_id που προκύπτει είναι το ακόλουθο: {762198}.  Γίνεται κλήση για να επιστραφεί το trgt_entty_riad_cd ως εξής:

.. code-block:: text

    https://<host>/wsrest/orgunits/sdd/extended/4.7/full?rp=entty_riad_cd,entty_riad_id&f.entty_riad_id.in=762198

Επιστρέφει το ακόλουθο (pretty-printed) απόσπασμα:

.. literalinclude:: /_static/conversions/events_ids.xml
   :language: XML

Συνδυάζοντας τα δύο αρχεία γίνεται η μετατροπή σε DBDAT ως εξής:

.. literalinclude:: /_static/conversions/events.json
   :language: JSON

Το DBDAT αρχείο μετατρέπεται σε DAT με βάση τους κανόνες μετατροπής από DBDAT σε DAT για να φορτωθεί στη BED.


Παράδειγμα κλήσης με φίλτρο trgt_entty_riad_id:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    https://<host>/wsrest/events/sdd/full?rp=src_entty_riad_id,trgt_entty_riad_id,dt_evnt,typ_evnt&f.trgt_entty_riad_id.in=21974339,106072,23249498,18061578

Επιστρέφει το ακόλουθο (pretty-printed) απόσπασμα:

.. literalinclude:: /_static/conversions/events_trgt.xml
   :language: XML


To σύνολο των trgt_entty_riad_id που προκύπτει είναι κενό και άρα η επεξεργασία σταματάει και η μετατροπή ολοκληρώνεται.
