
############################################################
# 			    PaPi			   #	
# 		      Code réalisé par 		    	   #	
# Thomas Devlamminck, Dylan Mainghain et  Andrea Dalmasso  #
############################################################


import rhasspy
from sense_hat import SenseHat
import random
import closing as cl
import opening as op
import logo

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 
'''
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.ini") 
print("Apprentissage terminé.")
'''

##########
# BLAGUE #
##########

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

###############
# TEMPERATURE #
###############	

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





###################
# LISTE DE COURSE #
###################


def course():

	#affiche une cerise C'EST MOCHE ---- A MODIF (c'est pas vrai)
	logo.cherry() # import du fichier logo.py affiche une cerise

	# Ajoutez un item et sa quantité 
	# retirer un item ou une quantité précise d'un item 
	# lire la liste 

	def leave():
		'''
		permet de retourner a la boucle global
		'''
		main()


	def quantite(aliment):
		'''
		renvoi le nombre dis par la personne 
		'''

		while True:

			rhasspy.text_to_speech(f"Quel quantité de {aliment} voulez vous rajoutez?")

			intent = rhasspy.speech_to_intent()

			# si pas de message 
			if intent["name"]=="nombre":

				return intent["variables"]["nombre"]

			else:
				rhasspy.text_to_speech("Je n'ai rien entendu")
				continue

				

	def add_items(liste_course):
		'''
		rajouter un item et sa quantité a la liste puis rappelle la fonction add_items
		'''

		
		rhasspy.text_to_speech("Quel aliment voulez vous ajoutez a la liste?")
		while True:

			intent=rhasspy.speech_to_intent()

			if intent["name"] == "add_liste":
				
				#print(intent)
				#rajoutez un aliment 
				

				aliment = intent["variables"]["aliment"] #aliment a rajouter dans la liste

				print(f"aliment : {aliment}")
				
				#choisir la quantité à ajouté
				quant = quantite(aliment) # renvoi le nombre a rajouté

				print(f"quantité : {quant}")
				#rajoute la quantité et l'aliment demandé 
				liste_course.append([f"{quant},{aliment}"])
				if int(quant) > 1:
					rhasspy.text_to_speech(f"{quant}{aliment} ont été rajouté a la liste ")
				else:
					rhasspy.text_to_speech(f"{quant}{aliment} a été rajouté a la liste ")

				print(liste_course)

				#dis la liste de course
				read_list(liste_course)


				#dmd si veut raouter un autre élement a la liste
				while True:

					rhasspy.text_to_speech("Voulez vous rajoutez un autre élément a la liste")

					intent=rhasspy.speech_to_intent()

					if intent["name"] == "Oui":
						add_items(liste_course)

					elif intent["name"] == "Non":
						leave()

					elif intent["name"] == "":
						rhasspy.text_to_speech("je n'ai rien entendu.")
						continue
				
			else:
				rhasspy.text_to_speech("je n'ai rien entendu. Quel aliment voulez vous ajoutez un item a la liste?")


	def read_list(liste_course):
		'''
		lis la liste de course

		'''
		rhasspy.text_to_speech("Votre liste est composé de :")

		for i in liste_course:
			for z in i:
				rhasspy.text_to_speech(z.replace(','," ")) 

	
	def liste_vide(liste_course):
		'''
		si la liste est vide dmd si veux creer une liste 
		'''

		if len(liste_course) < 1:
			rhasspy.text_to_speech("Votre liste est vide. Voulez vous y rajoutez quelque chose?")

			while True:

				intent=rhasspy.speech_to_intent()

				# si pas de message 
				if intent["name"]=="": 
					rhasspy.text_to_speech("je n'ai rien entendu. Votre liste est vide voulez vous rajoutez quelque chose?")
					continue
				
				# rajoutez un item 
				elif intent["name"]=="Oui":
					add_items(liste_course)
					
				# quitter la fonction
				elif intent["name"]=="Non":
					leave()
		

	
	def is_list(liste_course):
		'''
		verif si la liste existe
		'''
	
		try:

			if type(liste_course) == list : # si liste existe pas ERROR -> except
				return True
			else:
				return False

		except:

			return False


	try:
		if is_list() == False: #si aucune liste existe

				rhasspy.text_to_speech("Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")

				while True:

					intent=rhasspy.speech_to_intent()

					# si pas de message 
					if intent["name"]=="":
						rhasspy.text_to_speech("je n'ai rien entendu. Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")
						continue

					elif intent["name"]=="Oui":
						rhasspy.text_to_speech("Nouvelle liste de course créée")
						liste_course=[] #création d'une liste vide
						print("Nouvelle liste de course créée")
						print(liste_course)
						liste_vide(liste_course)

					elif intent["name"]=="Non":
						leave()

		else: #si une liste existe

			#dire la liste et proposer de retirer des bails ou ajoutez ou rien
			while True:

				rhasspy.text_to_speech("Vous avez une liste. Voulez ajoutez un aliment? Retirez un aliment ? Ou lire la liste?")

				if intent["name"]=="":
					rhasspy.text_to_speech("je n'ai rien entendu")
					continue

				elif intent["name"] == "lire_liste":
					read_list(liste_course)

				elif intent["name"] == "ajout_liste":
					add_items()

				elif intent["name"] == "retirer_liste":
					pass #a implimenter 
	except:

		rhasspy.text_to_speech("Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")

		while True:

			intent=rhasspy.speech_to_intent()

			# si pas de message 
			if intent["name"]=="":
				rhasspy.text_to_speech("je n'ai rien entendu. Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")
				continue

			elif intent["name"]=="Oui":
				rhasspy.text_to_speech("Nouvelle liste de course créée")
				liste_course=[] #création d'une liste vide
				print("Nouvelle liste de course créée")
				print(liste_course)
				liste_vide(liste_course)

			elif intent["name"]=="Non":
				leave()






#################
# BOUCLE GLOBAL #
#################
def main():

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


if __name__ == "__main__":
	
	main()

