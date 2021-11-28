1) Contexte:

Notre équipe a été recrutée par le service Santé de l’État belge afin d’aider les personnes âgées à rester autonomes. Les sondages affirment que les besoins de
base sont de retenir leur liste de courses et leur code de carte bancaire.  Pour plus de sécurité, ce code doit être crypté. La tâche à réaliser est de créer un 
assistant vocal qui pourra effectuer ces deux taches. Une ou plusieurs autres fonctionnalités au choix devront être disponibles. Celles-ci devront
obligatoirement se baser sur un ou plusieurs capteurs présents sur le SenseHat, par exemple le gyroscope, thermomètre, accéléromètre, capteur de température /
pression / humidité), tout en utilisant la reconnaissance vocale avec le microphone (l’écran et le joystick si besoin). Pour relever ce défi, un outil appelé
PaPi (Raspberry pi) est à disposition. Ce dernier permet de lancer des commandes grâce à une synthèse vocale.


2) Fonctionnalités attendues :

Pour le stockage et le rendu du code de la carte bancaire :

  - Proposer une interface utilisant le microphone, l’affichage LED et le joystick du SenseHat permettant d’entrer un numéro : 
    1: Si aucun numéro n’est enregistré, elle doit permettre d’enregistrer un nouveau numéro (à l’aide du joystick et du microphone), puis le nouveau code.
    2: Si un numéro est déjà enregistré, elle permet de tenter d’entrer le code, et d’afficher et énoncer le numéro si celui-ci est correct.
    3: Une fois le numéro énoncé et affiché, il peut être détruit si souhaité (retour au point 1), ou conservé (retour au point 2).
    
  - Le numéro (chiffres entre 0 et 9) doit pouvoir être entré sur le PaPi grâce au microphone et au joystick. Le code doit être une suite de mots énoncés par
  l'utilisateur(ex "fromage","salade",\\"melon"). Les deux doivent être conservés dans un fichier et pouvoir être disponibles même si le Raspberry Pi s'éteint et
  se rallume. Le numéro doit être conservé sous forme de chiffres et le code devra être haché.
  
Pour la liste de courses :

  - Grâce à  une interface utilisant le microphone, l’affichage LED et le joystick du SenseHat, l'utilisateur aura la possibilité d’entrer sa liste de courses :
    1: s'il n'y a aucune liste de courses enregistrée, l'utilisateur doit pouvoir sauvegarder une nouvelle liste de courses
    2: si une liste de courses est enregistrée, elle permet de l'énoncer à l’aide de la synthèse vocale
    3: lorsque celle-ci est énoncée, elle peut être supprimée si souhaité (retour au point 1), ou gardée (retour au point 2)
    
  - Cette liste de courses comprend une série d'articles et leur quantité. L’interface permettra alors de nommer l'article et d'en énoncer la quantité (de un à
  cinquante). Ceci sera donc ajouté à la liste. Et ainsi de suite pour les articles suivants. Lorsque la liste de courses est terminée, l’utilisateur énoncera la
  commande “terminé” pour finir sa liste de courses. 
  
3) Fonctionnalités supplémentaires :

  - Une commande vocale météorologique qui répondra par synthèse vocale. Le PaPi pourra donner la température et l'humidité ambiantes grâce aux capteurs
  d'humidité et de température intégrés. Tout ceci avec une animation sur l'écran LED.
  
  - Grâce à une commande vocale (ex : "Fais une blague", "fais-moi rire") le PaPi fera une blague tirée d'une liste de blagues pré-faite.  
