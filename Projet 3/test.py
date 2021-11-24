import rhasspy
from sense_hat import SenseHat
import random
import closing as cl
import opening as op
import logo

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 
'''
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.ini") 
print("Apprentissage terminé.")
'''

sense = SenseHat()


def blague():

	#rajoute un smile
	logo.smiley() # import du fichier logo.py affiche un smiley

	list_blague = ["Que demande un footballeur à son coiffeur ? La coupe du monde s’il vous plait",
    	"C'est quoi une chauve-souris avec une perruque? Une souris.",
    	"Que fait une fraise sur un cheval ? Tagada Tagada",
    	"C'est l'histoire de 2 patates qui traversent la route. L’une d’elles se fait écraser. L’autre dit : « Oh purée ! »"]

    #prend un blague au "hasard" de la liste et la dis 
	blague = list_blague[random.randint(0, len(list_blague)-1)]
	rhasspy.text_to_speech(blague)

def temperature():
	
	#rajouter un dessin de thermostat 
	logo.thermostat() # import du fichier logo.py affiche un thermo

	#capte la température et la dis 
	temperature = round(sense.temp)
	rhasspy.text_to_speech(f"il fait {temperature} degrés en se moment")
	print(temperature)

	
	#affiche la température sur les LED 
	if temperature > 30:
	 	sense.show_message(str(temperature), text_colour=[255, 0, 0]) #texte en rouge si il fait chaud
	 	rhasspy.text_to_speech(f"Oula il fait chaud penser a mettre de la crème solaire")

	elif temperature < 15:
		sense.show_message(str(temperature), text_colour=[0, 0, 255]) #texte en bleu si froid
		rhasspy.text_to_speech(f"Pensez a mettre un pull il fais froid")

	else:
	 	sense.show_message(str(temperature), text_colour=[0, 255,0]) #texte en vert si il fait bon
	 	rhasspy.text_to_speech(f"il fait bon dehors")


def course():

	#affiche une cerise
	logo.cherry() # import du fichier logo.py affiche une cerise

	try:

		if len(liste_course)>=1 :
			rhasspy.text_to_speech("let's go")
			rhasspy.text_to_speech(f"Votre liste se compose de{liste_course[0]} ")
		
	except:

		rhasspy.text_to_speech("Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")

		while True:

			intent=rhasspy.speech_to_intent()

			# si pas de message 
			if intent["name"]=="":
				rhasspy.text_to_speech("je n'ai rien entendu")
				continue

			elif intent["name"]=="Oui":
				rhasspy.text_to_speech("Nouvelle liste de course créée")
				liste_course=[]
				rhasspy.text_to_speech("Quel aliment voulez vous ajoutez a la liste?")

				while True:
					aliment =rhasspy.speech_to_text()

					if aliment == "":
						rhasspy.text_to_speech("je n'ai rien entendu")
						continue
					else:
						liste_course.append(aliment)
						course()

			elif intent["name"]=="Non":
				break


op.opening()

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
		if intent["name"] == 'Blague' or intent["name"] == 'Temperature' or intent["name"] == 'Course':
			rhasspy.text_to_speech("Vous avez lancé la commande {} ".format(intent["name"]))
			print(intent["name"])

		elif intent["name"] == "Arret": # si cmd arret stop le programme
			rhasspy.text_to_speech("Au revoir!")
			cl.closing()
			sense.clear()
			quit()

		else:
			rhasspy.text_to_speech(f"Ceci n'est pas une commande valide")


	if intent["name"] == 'Blague': 
		blague()
		
	elif intent["name"] == 'Temperature':
		temperature()

	elif intent["name"] == 'Course':
		course()

