import rhasspy
from sense_hat import SenseHat
import random

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 

sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.ini") 
print("Apprentissage terminé.")

#setup des couleurs
green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
grey = (95,95,95)

def SMILEY_logo():
	#fait un smile 
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, Y, Y, O, O, O,
    O, Y, Y, Y, Y, Y, O, O,
    O, Y, O, Y, Y, O, Y, O,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, B, Y, Y, Y, Y, B, Y,
    O, Y, B, B, B, B, Y, O,
    O, O, Y, G, G, Y, O, O,
    O, O, O, Y, Y, O, O, O,
    ]
    return logo

def thermostat():
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
	
	#capte la température et la dis 
	temperature = round(sense.temp)
	rhasspy.text_to_speech(f"il fait {temperature} degrés en se moment")
	print(temperature)

	#rajouter un dessin de thermostat 
	sense.set_pixels(thermostat())

	
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


class ListeDeCourse:

	def __inti__(self,num,liste):
		self.num = num
		self.liste = []

	def remove(self,item):

		self.liste.remove(item)

	def add(self,item):

		self.liste.add(item)

def course():
	
	#rajouter un truc de course ?? en faire une class pour pouvoir faire plusieurs liste a la fois 

	while True:

		liste_de_course = []

		if len(liste_de_course) == 0:
			rhasspy.text_to_speech("Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")
			intent = rhasspy.speech_to_intent()

			while True:

				if intent["name"] == "": # si pas de message 
			    	rhasspy.text_to_speech("je n'ai rien entendu")
			    	continue

			    elif intent["name"] == "Oui":
			    	rhasspy.text_to_speech("Nouvelle liste de course crée")
			    	
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


    elif intent["name"] == 'Blague': 
    	blague()
    	
    elif intent["name"] == 'Temperature':
    	temperature()

    elif intent["name"] == 'Course':
    	course()

