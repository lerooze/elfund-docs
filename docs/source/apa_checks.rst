Έλεγχοι Αρχείου
===============

Σε περίπτωση που τα εισερχόμενα αρχεία είναι δομής IFDAT ή DBDAT δημιουργείται αρχείο
επικύρωσης ανά υποβαλλόμενο αρχείο.  Αν ένα αρχείο ικανοποιεί τους
ελέγχους επικύρωσης τότε θεωρείται έγκυρο και εισάγεται στην BED.

Η διαδικασία για την παραγωγή του αρχείο περιλαμβάνει τους ακόλουθους ελέγχους:


Έλεγχος Τύπου Αρχείου (FILE_TYPE_CHECK)
---------------------------------------

Ο έλεγχος αποτυγχάνει αν το extension του αρχείου δεν είναι .xlsx ή .json καθώς και αν το είδος του αρχείου δεν είναι EXCEL είτε JSON.


Έλεγχοι EXCEL Αρχείου
---------------------

Εάν το αρχείο είναι μορφής xlsx ακολουθούνται τα παρακάτω βήματα:

Έλεγχος Υπάρξης Φύλλου HEADER (EXCEL_HEADER_EXISTENCE_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν δεν υπάρχει το φύλλο HEADER


Έλεγχος Ύπαρξης Άλλων Λαθών Φύλλου HEADER (EXCEL_HEADER_OTHER_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει εάν εμφανιστεί κάποιο άλλο λάθος στην επεξεργασία του HEADER.


Έλεγχος Συνέπειας Φύλλου CONTENT (EXCEL_CONTENT_CONSISTENCY_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει εάν στο φύλλο CONTENTS εμφανίζεται ένδειξη ότι κάποιο
φύλλο περιέχει στοιχεία αλλά το αντίστοιχο φύλλο είναι κενό.  Σημειώνεται ότι
επεξεργάζονται μόνο τα φύλλα με συμπληρωμένη την ένδειξη στο φύλλο CONTENTS.


Έλεγχος Μετατροπής σε JSON (JSON_CONVERSTION_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει εάν δεν είναι εφικτή η  μετατροπή σε μορφή json. Δηλαδή
για κάθε ένδειξη στο φύλλο CONTENTS επεξεργάζεται το αντίστοιχο φύλλο και
μετατρέπεται σε json με βάση το IFDat/DBDat json schema.  


Έλεγχοι JSON Αρχείου
--------------------

Εάν το αρχείο είναι μορφής json (είτε το υποβαλλόμενο, είτε αν το EXCEL έχει
μετατραπεί σε JSON) ακολουθούνται τα παρακάτω βήματα:

    
Έλεγχος Υπάρξης HEADER (JSON_HEADER_EXISTENCE_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν δεν υπάρχει το κλειδί HEADER.


Έλεγχος Συνέπειας USERNAME (JSON_USERNAME_CONSISTENCY_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ο έλεγχος αποτυγχάνει εάν το USERNAME στο HEADER του αρχείου είναι διαφορετικό σε σχέση
με το USERNAME στο IRIS.


Έλεγχος Συνέπειας DOMAIN (JSON_DOMAIN_CONSISTENCY_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ο έλεγχος αποτυγχάνει εάν το DOMAIN στο HEADER δεν είναι IFDat για τα IFDAT αρχεία
και DBDAT για τα DBDAT αρχεία.  


Έλεγχος Συνέπειας με το SCHEMA (JSON_SCHEMA_VALIDATION_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ο έλεγχος αποτυγχάνει εάν το αρχείο δεν έχει δομηθεί με βάση το JSON schema και
καταχωρούνται στο ΑΠΑ όλα τα λάθη.

Έλεγχος Δομής Αναγνωριστικών Κωδικών
------------------------------------
Γίνονται οι παρακάτω έλεγχοι για τους αναγνωωριστικούς κωδικούς:

Έλεγχος ESCB_ID (ESCB_ID_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν για τις τιμες στα πεδία τύπου ESCB_ID ο δεύτερος και ο τρίτος χαρακτήρας δεν ανήκουν στη λίστα GEN_CNTRY_ENUM ή αν δεν είναι Ε$ ή Ν$.


Έλεγχος χώρας στο TAX_ID (TAX_ID_COYNTRY_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν τα δύο πρώτα ψηφία των μεταβλητών TAX_ID δεν ανήκουν στη λίστα GEN_CNTRY_ENUM και καταχωρούνται στο ΑΠΑ όλα τα λάθη.
Ο έλεγχος αποτυγχάνει αν ο δεύτερος και ο τρίτος χαρακτήρας των πεδίων μορφής ORG_ID που ξεκινάνε με το πρόθεμα Τ δεν ανήκουν στη λίστα GEN_CNTRY_ENUM και καταχωρούνται στο ΑΠΑ όλα τα λάθη.


Έλεγχος εγκυρότητας ΑΦΜ (GREEK_AFM_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν για τις μεταβλητές του προηγούμενου ελέγχου οι Τ κωδικοί με χώρα GR δεν έχουν έγκυρο ΑΦΜ και καταχωρούνται στο ΑΠΑ όλες οι περιπτώσεις.

Έλεγχος χώρας στο NBR_ID (NBR_ID_COYNTRY_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν τα δύο πρώτα ψηφία των μεταβλητών NBR_ID δεν ανήκουν στη λίστα GEN_CNTRY_ENUM και καταχωρούνται στο ΑΠΑ όλα τα λάθη.
Ο έλεγχος αποτυγχάνει αν ο δεύτερος και ο τρίτος χαρακτήρας των πεδίων μορφής ORG_ID που ξεκινάνε με το πρόθεμα B δεν ανήκουν στη λίστα GEN_CNTRY_ENUM και καταχωρούνται στο ΑΠΑ όλα τα λάθη.


Έλεγχος εγκυρότητας ΓΕΜΗ (GEMI_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν για τις μεταβλητές του προηγούμενου ελέγχου οι B κωδικοί με χώρα GR δεν έχουν έγκυρο ΓΕΜΗ και καταχωρούνται στο ΑΠΑ όλες οι περιπτώσεις.


Έλεγχος εγκυρότητας LEI (LEI_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει αν για τις μεταβλητές LEI_ID ή μεταβλητές τύπου ORG_ID και ALIAS_ORG_ID (αφαιρείται από την τιμή το πρόθεμα L) δεν ικανοποιούν τον αλγόριθμο LEI και καταχωρούνται στο ΑΠΑ όλες οι περιπτώσεις.

Έλεγχος Μοναδικής ΜΠΣ για κάθε ΠΜ (UNIQUE_RA2OA_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ο έλεγχος απαιτεί επικοινωνία με τη BED.

Ο έλεγχος αποτυγχάνει εάν επιχειρείται σύνδεση της ΠΜ με δεύτερη ΜΠΣ το επίμαχο διάστημα και καταχωρούνται στο ΑΠΑ όλες οι περιπτώσεις.


Έλεγχος Συσχέτισης Αναγνωριστικών Κωδικών (ALIAS_IDS_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ο έλεγχος απαιτεί επικοινωνία με τη BED.

Ο έλεγχος αποτυγχάνει εάν επιχειρείται σύνδεση των LEI_ID, TAX_ID, NBR_ID με πάνω από ένα ESCB_ID και καταχωρούνται στο ΑΠΑ όλες οι περιπτώσεις.


Έλεγχοι Δομής IFDAT
-------------------

Οι έλεγχοι αυτοί πραγματοποιούνται μόνο σε αρχεία IFDAT.

Έλεγχος Δικαιώματος Υποβολλής Εγγραφής (RECORD_SUBMISSION_RIGHTS_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ο έλεγχος απαιτεί επικοινωνία με τη BED.

Ο έλεγχος αποτυγχάνει εάν ο ΕΟ που αφορά η εγγραφή δεν ανήκει στη ΜΠΣ την ημερομηνία υποβολής του αρχείου και καταχωρούνται στο ΑΠΑ όλες οι περιπτώσεις.

Ο έλεγχος αποτυγχάνει εάν η ΜΠΣ που αφορά η εγγραφή δεν είναι η ίδια με τη ΜΠΣ του IRIS και καταχωρούνται στο ΑΠΑ όλες οι περιπτώσεις. 


Έλεγχος Ξεχωριστής Υποβολλής RPRTD_BY (RPRTD_BY_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Ο έλεγχος αποτυγχάνει εάν η μέτρηση RPRTD_BY δεν υποβάλλεται σε ξεχωριστό
αρχείο χωρίς να έχει συμπληρωθεί οποιαδήποτε άλλη μεταβλητή στον πίνακα
FND_DYNMC ή στους υπόλοιπους πίνακες.


Έλεγχοι Δομής DBDAT
-------------------

Οι έλεγχοι αυτοί πραγματοποιούνται μόνο σε αρχεία DBDAT.


Έλεγχος Δικαιώματος Υποβολλής Πινάκων ACC (ACC_RIGHTS_CHECK)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ο έλεγχος αποτυγχάνει εάν έχουν συμπληρωθεί πίνακες ACC με SOURCE=SDR.
