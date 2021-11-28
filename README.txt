1) Contexte:

Notre équipe a été recrutée par le service Santé de l’État belge afin d’aider les personnes âgées à rester autonomes. Les sondages affirment que les besoins de base sont de retenir leur liste de courses et leur code de carte bancaire.  Pour plus de sécurité, ce code doit être crypté. La tâche à réaliser est de créer un assistant vocal qui pourra effectuer ces deux taches. Une ou plusieurs autres fonctionnalités au choix devront être disponibles. Celles-ci devront obligatoirement se baser sur un ou plusieurs capteurs présents sur le SenseHat, par exemple le gyroscope, thermomètre, accéléromètre, capteur de température / pression / humidité), tout en utilisant la reconnaissance vocale avec le microphone (l’écran et le joystick si besoin). Pour relever ce défi, un outil appelé PaPi (Raspberry pi) est à disposition. Ce dernier permet de lancer des commandes grâce à une synthèse vocale.


2) Fonctionnalit ́es attendues :
Pour le stockage et le rendu du code de la carte bancaire :
• Proposer une interface utilisant le microphone, l’affichage LED et le joystick du SenseHat permettant d’entrer un num ́ero :
1. Si aucun num ́ero n’est enregistr ́e, elle doit permettre d’enregistrer un nouveau num ́ero (`a l’aide du joystick et du microphone), puis le nouveau code.
2. Si un num ́ero est d ́ej`a enregistr ́e, elle permet de tenter d’entrer le code, et d’afficher et  ́enoncer le num ́ero si celui-ci est correct.
3. Une fois le num ́ero  ́enonc ́e et affich ́e, il peut ˆetre d ́etruit si souhait ́e (retour au point 1), ou conserv ́e (retour au point 2).
• Le num ́ero (chiffres entre 0 et 9) doit pouvoir ˆetre entr ́e sur le PaPi grˆace au microphone et au joystick. Le code doit ˆetre une suite de mots  ́enonc ́es par l’utilisateur(ex ”fromage”,”salade”, ”melon”). Les deux doivent ˆetre conserv ́es dans un fichier et pouvoir ˆetre disponibles mˆeme si le Raspberry Pi s’ ́eteint et se rallume. Le num ́ero doit ˆetre conserv ́e sous forme de chiffres et le code devra ˆetre hach ́e.
Pour la liste de courses :
• Grˆace `a une interface utilisant le microphone, l’affichage LED et le joystick du SenseHat, l’utilisateur aura la possibilit ́e d’entrer sa liste de courses :
1. s’il n’y a aucune liste de courses enregistr ́ee, l’utilisateur doit pouvoir sauvegarder une nouvelle liste de courses
1
2. si une liste de courses est enregistr ́ee, elle permet de l’ ́enoncer `a l’aide de la synth`ese vocale
3. lorsque celle-ci est  ́enonc ́ee, elle peut ˆetre supprim ́ee si souhait ́e (retour au point 1), ou gard ́ee (retour au point 2)
• Cette liste de courses comprend une s ́erie d’articles et leur quantit ́e. L’interface permettra alors de nommer l’article et d’en  ́enoncer la quantit ́e (de un `a cinquante). Ceci sera donc ajout ́e `a la liste.
Et ainsi de suite pour les articles suivants.
Lorsque la liste de courses est termin ́ee, l’utilisateur  ́enoncera la commande “termin ́e” pour finir sa liste de courses.
Fonctionnalit ́es suppl ́ementaires :
3
•
•
Une commande vocale m ́et ́eorologique qui r ́epondra par synth`ese vocale. Le PaPi pourra don- ner la temp ́erature et l’humidit ́e ambiantes grˆace aux capteurs d’humidit ́e et de temp ́erature int ́egr ́es. Tout ceci avec une animation sur l’ ́ecran LED.
Grˆace `a une commande vocale (ex : ”Fais une blague”, ”fais-moi rire”) le PaPi fera une blague tir ́ee d’une liste de blagues pr ́e-faite.
