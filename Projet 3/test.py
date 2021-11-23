import rhasspy
from sense_hat import SenseHat
import random
import closing as cl
import opening as op


sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 
'''
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.ini") 
print("Apprentissage terminé.")
'''

#setup des couleurs
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
grey = (95,95,95)
brown = (139,69,19)

def SMILEY_logo():
	#fait un smile 
    G = green
    Y = yellow
    B = blue
    O = nothing
    R = red
    P = pink

    logo = [
    O, O, O, Y, Y, O, O, O,
    O, Y, Y, Y, Y, Y, O, O,
    O, Y, P, Y, Y, P, Y, O,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, B, Y, Y, Y, Y, B, Y,
    O, Y, B, B, B, B, Y, O,
    O, O, Y, R, R, Y, O, O,
    O, O, O, Y, Y, O, O, O,
    ]
    return logo

def thermostat_logo():
  	#fait un thermostat
	O = nothing 
	W = white
	R = red
	B = blue
	G = grey
	logo = [
	G, G, G, W, W, G, G, G,
	G, G, G, W, O, G, G, G,
	G, G, G, W, W, G, G, G,
	G, G, G, W, O, G, G, G,
	G, G, G, W, W, G, G, G,
	G, G, W, R, R, W, G, G,
	G, G, W, R, R, W, G, G,
	G, G, G, W, W, G, G, G,
	]
	return logo

def cherry_logo():
    R = red
    B = brown
    O = nothing
    logo = [
    O, O, O, O, B, O, O, O,
    O, O, O, O, B, O, O, O,
    O, O, O, B, O, B, O, O,
    O, O, R, O, O, B, O, O,
    O, R, R, R, O, R, O, O,
    O, O, R, O, R, R, R, O,
    O, O, O, O, O, R, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo


def blague():

	#rajoute un smile
	sense.set_pixels(SMILEY_logo())

	list_blague = ["Que demande un footballeur à son coiffeur ? La coupe du monde s’il vous plait",
    	"C'est quoi une chauve-souris avec une perruque? Une souris.",
    	"Que fait une fraise sur un cheval ? Tagada Tagada",
    	"C'est l'histoire de 2 patates qui traversent la route. L’une d’elles se fait écraser. L’autre dit : « Oh purée ! »"]

    #prend un blague au "hasard" de la liste et la dis 
	blague = list_blague[random.randint(0, len(list_blague)-1)]
	rhasspy.text_to_speech(blague)

def temperature():
	
	#rajouter un dessin de thermostat 
	sense.set_pixels(thermostat_logo())

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

	sense.set_pixels(cherry_logo())

	try:

		if len(liste_course)>=1 :
			rhasspy.text_to_speech("let's go")
			rhasspy.text_to_speech(f"Votre liste se compose de{liste_course[0]} ")
		
	except:

		rhasspy.text_to_speech("Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")
		intent=rhasspy.speech_to_intent()

		while True:

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
	    if intent["name"] == 'Blague' or intent["name"] == 'Temperature' or intent["name"] == 'Course':#si pas de paramètres A DEBUG
	    	rhasspy.text_to_speech("Vous avez lancé la commande {} ".format(intent["name"]))
	    	print(intent["name"])

	    else:

	    	if intent["name"] == "Arret": # si cmd arret stop le programme
		    	rhasspy.text_to_speech("Au revoir!")
		    	cl.closing()
		    	sense.clear()
		    	quit()

	    	rhasspy.text_to_speech("Vous avez lancé la commande {} avec les paramètres {}".format(intent["name"], intent["variables"]))
	    	print(intent["name"])
	    	print(intent["variables"])

	    # Affiche la commande vocale reçue.
	    sense.show_message(" {}".format(intent["name"]), scroll_speed=0.09)


    if intent["name"] == 'Blague': 
    	blague()
    	
    elif intent["name"] == 'Temperature':
    	temperature()

    elif intent["name"] == 'Course':
    	course()

