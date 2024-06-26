DBDat
=====

Το **DBDat** αποτελεί τη δομή δεδομένων μέσω της οποίας όλα τα υποβαλλόμενα
στοιχεία εισάγονται στη **Backend Database** με την προϋπόθεση ότι πληρούν
κρίσιμους ελέγχους.  Αποτελεί επίσης τη δομή δεδομένων με την οποία αρμόδιοι υπάλληλοι
της ΤτΕ θα μπορούν να φορτώνουν απευθείας στοιχεία.

Στο :download:`DATA_MODEL </_static/structure/DBDAT_DATAMODEL.xlsx>` παρουσιάζεται η δομή του σχήματος δεδομένων **DBDat**.

Το :download:`JSON_SCHEMA </_static/structure/DBDAT_SCHEMA.json>` σχήμα για την
υποβολή αρχείων με βάση το **DATA_MODEL** σε μορφή **json** έχει αναπτυχθεί
σύμφωνα με τα πρότυπα :xref:`json_schema_core` και :xref:`json_schema_validation`.  

Με το αρχείο :download:`EXCEL_TEMPLATE
</_static/structure/DBDAT_TEMPLATE.xlsx>` γίνεται η υποβολή στοιχείων **DBDat**
σε μορφή **Excel**.


Τρόπος υποβολής των αρχείων από αρμόδιους χρήστες της ΤτΕ
---------------------------------------------------------

Τα αρχεία υποβάλλονται μέσω του πληροφοριακού συστήματος :xref:`iris` είτε μέσω
API είτε μέσω GUI.  Για κάθε αρχείο που υποβάλλει ένας χρήστης θα λαμβάνει ένα
απαντητικό αρχείο σχετικά με το αν το αρχείο παρελήφθη καθώς επίσης και την
ονομασία του αρχείου που χρησιμοποίησε η Τράπεζα της Ελλάδος για να το
αποθηκεύσει. Η ονομασία του αρχείου ακολουθεί τον ακόλουθο μορφότυπο
``F{ID}DBDAT_{USER}_{NAME}`` όπου: 

* ID είναι ένας μοναδικός ακέραιος αριθμός εισερχόμενου αρχείου μάκρους δέκα
  χαρακτήρων με πρόθεμα το 0 ο οποίος ξεκινάει από το τον αριθμό 1 και
  αυξάνεται κατά ένα κάθε φορά που υποβάλλεται νέο αρχείο.

* NAME είναι η αρχική ονομασία του εισερχόμενου αρχείου
* USER είναι ο αναγνωριστικός κωδικός του χρήστη στην ΤτΕ.  

Για παράδειγμα ένα εισερχόμενο αρχείο με ονομασία **data_submission.xlsx** από
τον χρήστη **aloumiotis** με ID 5 μετονομάζεται σε
``F0000000005DBDAT_aloumiotis_data_submission.xlsx``.

Οι μορφότυποι των εισερχόμενων αρχείων της δομής **DBDat** είναι οι ακόλουθοι: 

i. Αρχεία μορφής ``.json``.  Το αρχείο θα πρέπει να δομείται σύμφωνα με το
   :download:`DBDat JSON Schema </_static/structure/DBDAT_SCHEMA.json>`.

#. Αρχεία μορφής ``.xlsx`` με βάση το :download:`υπόδειγμα <_static/structure/DBDAT_TEMPLATE.xlsx>`.

#. Αρχεία μορφής ``.zip``.  Το αρχείο θα πρέπει να περιέχει ως περιεχόμενο μόνο ένα αρχείο με μία από τις παραπάνω μορφές (xlsx, json).


Επεξεργασία και εισαγωγή στοιχείων στη βάση (αφορά σειριακή επεξεργασία)
------------------------------------------------------------------------

1.  Με βάση το username που αντλείται από την ονομασία του αρχείου όπως αυτή έχει δημιουργηθεί από το σύστημα IRIS παράγεται εάν δεν υπάρχει ήδη ένα αρχείο επικύρωσης για το συγκεκριμένο χρήστη.  Σε περίπτωση που έχει παραχθεί αρχείο για το συγκεκριμένο χρήστη και η προσέγγιση επεξεργασίας είναι η παράλληλη δεν δημιουργείται νέο αλλά χρησιμοποιείται το ίδιο.

#.  Σε περίπτωση που το αρχείο είναι μορφής zip θα πρέπει να ελέγχεται ότι το περιεχόμενο είναι είτε μορφής xlsx είτε json.  Αν δεν είναι εισάγεται καταχώρηση στα κρίσιμα λάθη του αρχείου επικύρωσης (corrupt_zip) και η επεξεργασία για το συγκεκριμένο αρχείο ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση processed=False στη λίστα των αρχείων).

#.  Σε περίπτωση που η επέκταση του αρχείου δεν είναι μία από τις .zip, .xlsx, .json εισάγεται καταχώρηση στα κρίσιμα λάθη του αρχείου επικύρωσης (wrong_extension) και η επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση processed=False στη λίστα των αρχείων).

#.  Σε περίπτωση που η επέκταση του αρχείου δεν είναι μία από τις .zip, .xlsx, .json εισάγεται καταχώρηση στα κρίσιμα λάθη του αρχείου επικύρωσης (wrong_extension) και η επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση processed=False στη λίστα των αρχείων).

#.  Εάν το αρχείο είναι μορφής xlsx ακολουθούνται τα ακόλουθα βήματα:

    * Εάν δεν υπάρχει το φύλλο HEADER τότε εισάγεται καταχώρηση στα κρίσιμα λάθη του αρχείου επικύρωσης (no_header) και η επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση processed=False στη λίστα των αρχείων).

    * Εάν εμφανιστεί κάποιο άλλο λάθος στην επεξεργασία το φύλλο
      HEADER τότε εισάγεται καταχώρηση στα κρίσιμα λάθη του αρχείου επικύρωσης
      (corrupt_excel) και η επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς
      (εισάγεται καταχώρηση processed=False στη λίστα των αρχείων).

    * Σε περίπτωση που σε φύλλο CONTENTS εμφανίζεται καταχώρηση ότι κάποιο φύλλο περιέχει στοιχεία αλλά το αντίστοιχο φύλλο είναι κενό εισάγεται καταχώρηση στα κρίσιμα λάθη (no_content) με τα κενά φύλλα και η επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση processed=False στη λίστα των αρχείων).

#.  Εάν το αρχείο είναι μορφής json ακολουθούνται τα ακόλουθα βήματα:

    * Σε περίπτωση που δεν μπορεί να διαβαστεί ως αρχείο json τότε εισάγεται
      καταχώρηση στα κρίσιμα λάθη του αρχείου επικύρωσης (corrupt_json) και η
      επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση
      processed=False στη λίστα των αρχείων).

    * Εάν δεν υπάρχει το κλειδί HEADER τότε εισάγεται καταχώρηση στα κρίσιμα
      λάθη του αρχείου επικύρωσης (no_header) και η επεξεργασία του αρχείου
      ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση processed=False στη λίστα
      των αρχείων).

    * Σε περίπτωση που σε φύλλο CONTENTS εμφανίζεται καταχώρηση ότι κάποιο
      φύλλο περιέχει στοιχεία αλλά το αντίστοιχο φύλλο είναι κενό εισάγεται
      καταχώρηση στα κρίσιμα λάθη (no_content) με τα κενά φύλλα και η
      επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση
      processed=False στη λίστα των αρχείων).

#.  Σε περίπτωση που το USERNAME από τα περιεχόμενα του αρχείου είναι
    διαφορετικό σε σχέση με το USERNAME της ονομασίας του αρχείου τότε εισάγεται
    καταχώρηση στα κρίσιμα λάθη (submitter_inconsistency_error) και η
    επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση
    processed=False στη λίστα των αρχείων).

#.  Σε περίπτωση που το DOMAIN από το HEADER δεν είναι DBDat τότε εισάγεται
    καταχώρηση στα κρίσιμα λάθη (not_supported_domain) και η επεξεργασία του
    αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση processed=False στη
    λίστα των αρχείων).

#.  Σε περίπτωση που το αρχείο είναι xlsx μετατρέπεται σε μορφή json.  Δηλαδή
    για κάθε καταχώρηση στο φύλλο CONTENTS διαβάζεται το αντίστοιχο φύλλο και
    μετατρέπεται σε μορφή json με βάση φυσικά το DBDat json schema.  Σε
    περίπτωση που το υποβαλλόμενο αρχείο είναι json δεν γίνεται κάποια
    επεξεργασία σε αυτό το βήμα.

#.  Το json αρχείο ελέγχεται σύμφωνα με το JSON schema και στην περίπτωση που
    εντοπιστούν λάθη καταχωρούνται στα κρίσιμα λάθη (schema_errors) και η
    επεξεργασία του αρχείου ολοκληρώνεται ανεπιτυχώς (εισάγεται καταχώρηση
    processed=False στη λίστα των αρχείων).

#.  Τα εισαγόμενα στοιχεία ανά δομή δεδομένων μετατρέπονται σε πίνακες δομής
    βάσης δεδομένων όπου τα πεδία για τη πηγή των στοιχείων προκύπτουν από το
    HEADER.  Σε περίπτωση που για μια δομή δεδομένων υπάρχουν ήδη στοιχεία από
    προηγούμενα προς επεξεργασία αρχεία τότε τα νέα στοιχεία συνενώνονται με τα
    προηγούμενα.

#.  Για κάθε πίνακα εάν δεν υπάρχει το STATUS ATTRIBUTE για κάθε μεταβλητή με
    τιμή τότε συμπληρώνεται αυτόματα η τιμή Α για το STATUS ATTRIBUTE εκτός εάν
    έχουν συμπληρωθεί οι ειδικές τιμές MINDATE=1678-01-01 ή '-' για μεταβλητές
    τύπου DATE ή non-DATE αντίστοιχα όπου συμπληρώνεται η ειδική τιμή '-'
    (not-set) για το αντίστοιχο χαρακτηριστικό.

#.  Εάν ο πίνακας περιλαμβάνει τη διάσταση VLD_FRM και η διάσταση VLD_FRM δεν
    έχει συμπληρωθεί για κάποια παρατήρηση τότε συμπληρώνεται αυτόματα το
    MINDATE που υποστηρίζει το backend.  Για παράδειγμα στην Python το
    MINDATE=1678-01-01.

#.  Εάν ο πίνακας περιλαμβάνει τη διάσταση VLD_T και η διάσταση VLD_T δεν έχει
    συμπληρωθεί για κάποια παρατήρηση τότε συμπληρώνεται αυτόματα το MAXDATE
    που υποστηρίζει το backend.  Για παράδειγμα στην Python το
    MAXDATE=2200-12-31.

#.  Πρώτα επεξεργάζονται και εισάγονται στη βάση οι "alias" πίνακες και ύστερα
    οι υπόλοιποι.  Είναι προτιμότερο στοιχεία με συμπληρωμένους τους alias
    πίνακες να υποβάλλονται έως ξεχωριστό αρχείο και να μην συνδυάζονται με
    συμπληρωμένους κάποιους από τους υπόλοιπους πίνακες.  Σε περίπτωση που
    γίνει συνδυασμός οι μη alias πίνακες δεν θα λαμβάνουν υπόψη τα νέα στοιχεία
    των "alias" πινάκων.  Για τους μη alias πίνακες αντικαθίστανται οι
    αναγνωριστικοί κωδικοί που έχουν alias με το alias authoritative record.

#.  Για κάθε εισερχόμενο πίνακα επιλέγονται τα υφιστάμενα στοιχεία της πιο
    πρόσφατης έκδοσης για όλες τις πηγές για τις οντότητες που υποβάλλονται νέα
    στοιχεία.  Εάν ο πίνακας στις διαστάσεις του περιλαμβάνει άνω του ενός
    είδος οντοτήτων επιλέγονται όλα τα στοιχεία για τις οντότητες του πρώτου
    είδους.  Για παράδειγμα εάν στις διαστάσεις περιέχονται οι διαστάσεις LID,
    RID επιλέγεται το σύνολο της πληροφόρησης για την διάσταση LID.  Η επιλογή
    μπορεί να γίνει είτε μέσω του API χρησιμοποιώντας τον προορισμό των πιο
    πρόσφατων στοιχείων ανά πηγή είτε κατευθείαν από τη βάση.

#.  Για τα επιλεγμένα υφιστάμενα στοιχεία για κάθε μεταβλητή όπου το STATUS
    είναι ίσο με '-' η τιμή της μεταβλητής αντικαθίσταται με τιμή None (κάποιο
    είδος None που δηλώνει ότι η μεταβλητή δεν είναι συμπληρωμένη).

#.  Δημιουργούνται τρία αντίγραφα του νέου εισερχόμενου πίνακα.  Στο πρώτο
    αντίγραφο αντικαθίσταται η τιμή του πεδίου SRC_USR με την authoritative
    τιμή του SRC_USR.  Στο δεύτερο αντίγραφο αντικαθίσταται η τιμή του
    SRC_ORG με την authoritative τιμή του SRC_ORG και στο τρίτο αντίγραφο
    αντικαθίσταται η τιμή τόσο του SRC_USR όσο και του SRC_ORG με τις
    authoritative τιμές.  Οι authoritative τιμές του SRC_ORG και του SRC_USR
    μπορεί να είναι το '0' ή το ''.  Τα τρία αντίγραφα προσθέτονται στο νέο
    εισερχόμενο πίνακα.

#.  Διπλότυπες εγγραφές με βάση τις διαστάσεις διαγράφονται και αυτή που
    παραμένει διατηρεί τις τελευταίες τιμές των μεταβλητών.  Στις γενικές
    οδηγίες δίδονται παραδείγματα.

#.  Προσθέτονται στο νέο πίνακα ως κενά τα measures και τα attributes τα οποία
    δεν έχουν αναγγελθεί και είναι προαιρετικά σύμφωνα με το schema.

#.  Για τους πίνακες που περιέχουν στις διαστάσεις τους τα πεδία VLD_FRM και
    VLD_T οι νέοι και οι υφιστάμενοι πίνακες ζυγοσταθμίζονται έτσι ώστε να
    έχουν ενιαίες διαστάσεις και συμπληρώνονται τα κενά στις παρατηρήσεις.
    Περισσότερες πληροφορίες στις γενικές οδηγίες.  

#.  Κενές τιμές στο νέο πίνακα καλύπτονται από μη κενές τιμές από τον
    υφιστάμενο και υπολογίζεται το νέο authoritative record.

#.  Στην περίπτωση που υπάρχουν αλλαγές σε σχέση με τον υφιστάμενο πίνακα
    φορτώνονται οι αλλαγές στη βάση. 

#.  Αφού ολοκληρωθεί η επεξεργασία των στοιχείων για κάθε πίνακα του αρχείου
    τότε συμπληρώνεται η ένδειξη processed=True στο αρχείο επικύρωσης και τα
    στοιχεία της επικύρωσης φορτώνονται στη βάση επικύρωσης.
