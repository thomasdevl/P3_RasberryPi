import rhasspy
from sense_hat import SenseHat
import random

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 

sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.ini") #FAIRE un nv fichier avec nos phrases
print("Apprentissage terminé.")



def blague():

	list_blague = ["Que demande un footballeur à son coiffeur ? La coupe du monde s’il vous plait",
    	"C'est quoi une chauve-souris avec une perruque? Une souris.",
    	"Que fait une fraise sur un cheval ? Tagada Tagada",
    	"C'est l'histoire de 2 patates qui traversent la route. L’une d’elles se fait écraser. L’autre dit : « Oh purée ! »"]

	blague = list_blague[random.randint(0, len(list_blague)-1)]

	rhasspy.text_to_speech(blague)

def temperature():
	temperature = round(sense.temp)
	rhasspy.text_to_speech(f"il fait {temperature} degrés en se moment")
	print(temperature)


	#rajouter phrase perso en fct de la température
	if temperature > 30:
	 	sense.show_message(str(temperature), text_colour=[255, 0, 0]) #texte en rouge si il fait chaud

	elif temperature < 15:
		sense.show_message(str(temperature), text_colour=[0, 0, 255]) #texte en bleu si froid

	else:
	 	sense.show_message(str(temperature), text_colour=[0, 255,0]) #texte en vert si il fait bon

def course():
	

	while True:

		if len(liste_de_course) == 0:
			rhasspy.text_to_speech("Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")
			intent = rhasspy.speech_to_intent()

			while True:

				if intent["name"] == "": # si pas de message 
			    	rhasspy.text_to_speech("je n'ai rien entendu")
			    	continue

			    elif intent["name"] == "Oui":
			    	rhasspy.text_to_speech("Nouvelle liste de course crée")
			    	liste_de_course = []
			    	pass

			    elif intent["name"] == "Non":
			    	break

		
		break





while True:
    sense.show_letter("?")
    # Introduction énoncée
    rhasspy.text_to_speech("Énoncez votre phrase, s'il vous plait.")

    # Réception d'une commande vocale et affichage du résultat.
    intent = rhasspy.speech_to_intent()
    #print(intent)

    if intent["name"] == "": # si pas de message 
    	rhasspy.text_to_speech("je n'ai rien entendu")
    	continue

    else:

	    # Enonce la commande vocale reçue et les variables.
	    if intent["variables"] == "{}":#si pas de paramètres A DEBUG
	    	rhasspy.text_to_speech("Vous avez lancé la commande {} ".format(intent["name"]))
	    	print(intent["name"])

	    else:

	    	if intent["name"] == "Arret": # si cmd arret stop le programme
		    	rhasspy.text_to_speech("Au revoir!")
		    	quit()

	    	rhasspy.text_to_speech("Vous avez lancé la commande {} avec les paramètres {}".format(intent["name"], intent["variables"]))
	    	print(intent["name"])
	    	print(intent["variables"])

	    # Affiche la commande vocale reçue.
	    sense.show_message("Cmd: : {}".format(intent["name"]), scroll_speed=0.07)

    

    elif intent["name"] == 'Blague': # fais une blague
    	blague()
    	
    elif intent["name"] == 'Temperature':
    	temperature()

    elif inten["name"] == 'Course':
    	course()

