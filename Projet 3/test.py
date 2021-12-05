
############################################################
# 						  PaPi							   #	
# 					  Code réalisé par 					   #	
# Thomas Devlamminck, Dylan Mainghain et  Andrea Dalmasso  #
############################################################

#pour le rasberry 
import rhasspy
from sense_hat import SenseHat

#pour choisir un nmbr aléatoire
import random

#pour faire les animations sur l'écran LED
import closing as cl
import opening as op
import logo

#pour la fct code
import time
import crypto 

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
    	"C'est l'histoire de 2 patates qui traversent la route. L’une d’elles se fait écraser. L’autre dit : « Oh purée ! »",
    	"Allo ? C'est Jésus !– mais non ! mais si !",
    	"Quel est le bar préféré des Espagnols ? Le Bar-celone"]

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
	#affiche une cerise C'EST MOCHE ---- A MODIF 
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
		renvoi le nombre dis par la personne quand la personne veut rajouter un aliment 
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

				

	def add_items():
		'''
		rajoute un item et sa quantité a la liste puis rappelle la fonction add_items
		'''

		rhasspy.text_to_speech("Quel alimant voulez vous ajoutez a la liste?")

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

				#verif si l'aliment est deja dans la liste

				for i in range(len(liste_course)):

					if intent["variables"]["aliment"] in liste_course[i].split():

						rhasspy.text_to_speech(f"Vous avez déjà {aliment} dans votre liste")

						lst = liste_course[i].split()

						new_quant = int(quant) + int(lst[0])

						liste_course[i] = f"{new_quant} {lst[1]}"
						if int(quant) > 1:
							rhasspy.text_to_speech(f"{quant}{aliment} ont été rajouté a la liste ")
						else:
							rhasspy.text_to_speech(f"{quant}{aliment} a été rajouté a la liste ")

						#print(liste_course)

						#clear le file et y rajouter la liste mise a jour 

						#retire tout ce qui est sur le fichier 
						open('/home/pi/liste_course.txt', 'w').close() 

						#retire tout ce qui est sur le fichier 
						with open('/home/pi/liste_course.txt', 'w') as temp_file:
						    for item in liste_course:
						        temp_file.write("%s\n" % item)

						#dis la liste de course
						read_list()

						#dmd si veut rajouter un autre élement a la liste
						while True:

							rhasspy.text_to_speech("Voulez vous rajoutez un autre élément a la liste")

							intent=rhasspy.speech_to_intent()

							if intent["name"] == "Oui":
								add_items()

							elif intent["name"] == "Non":
								leave()

							elif intent["name"] == "":
								rhasspy.text_to_speech("je n'ai rien entendu.")
								continue


				#rajoute la quantité et l'aliment si il ne sont pas dans la liste
				liste_course.append(f"{quant} {aliment}")
				if int(quant) > 1:
					rhasspy.text_to_speech(f"{quant}{aliment} ont été rajouté a la liste ")
				else:
					rhasspy.text_to_speech(f"{quant}{aliment} a été rajouté a la liste ")

				#clear le file et y rajouter la liste mise a jour 

				#retire tout ce qui est sur le fichier 
				open('/home/pi/liste_course.txt', 'w').close() 

				#retire tout ce qui est sur le fichier 
				with open('/home/pi/liste_course.txt', 'w') as temp_file:
				    for item in liste_course:
				        temp_file.write("%s\n" % item)

				#dis la liste de course
				read_list()

				#dmd si veut rajouter un autre élement a la liste
				while True:

					rhasspy.text_to_speech("Voulez vous rajoutez un autre alimant a la liste")

					intent=rhasspy.speech_to_intent()

					if intent["name"] == "Oui":
						add_items()

					elif intent["name"] == "Non":
						leave()

					elif intent["name"] == "":
						rhasspy.text_to_speech("je n'ai rien entendu.")
						continue
				
			else:
				rhasspy.text_to_speech("je n'ai rien entendu. Quel alimant voulez vous ajoutez a la liste?")

	def quantite_remove(aliment,liste_quant_alim,position):
		'''
		renvoi le nombre dis par la personne quand la personne veut retier un aliment
		'''

		while True:

			rhasspy.text_to_speech(f"Quel quantité de {aliment} voulez vous retirer?")

			intent = rhasspy.speech_to_intent()

			lst = liste_quant_alim.split()

			if intent["name"]=="nombre":

				nombre = intent["variables"]["nombre"]

				#si le nombre donné est plus petite 
				if int(nombre) < int(lst[0]):

					print(f"aliment : {aliment}")
					print(f"nombre retirer : {nombre}")

					rhasspy.text_to_speech(f"{nombre} {aliment} ont été retirer de la liste")

					#remplacer dans la liste la valeur
					new_quant = int(lst[0]) - int(nombre)
					print(new_quant)
					liste_course[position] = f"{new_quant} {aliment}"
					#print(liste_course)

					#clear le file et y rajouter la liste mise a jour 
				
					#retire tout ce qui est sur le fichier 
					open('/home/pi/liste_course.txt', 'w').close() 

					#retire tout ce qui est sur le fichier 
					with open('/home/pi/liste_course.txt', 'w') as temp_file:
					    for item in liste_course:
					        temp_file.write("%s\n" % item)

					read_list()

				#si le nombre est plus grand ou égal a la quantité dans la liste l'élement est retirer totalement de la liste
				else:

					rhasspy.text_to_speech(f"Tous les {aliment} ont été retirer de la liste")
					#supprime l'aliment de la liste
					del liste_course[position]
					#print(liste_course)

					#clear le file et y rajouter la liste mise a jour 
				
					#retire tout ce qui est sur le fichier 
					open('/home/pi/liste_course.txt', 'w').close() 

					#retire tout ce qui est sur le fichier 
					with open('/home/pi/liste_course.txt', 'w') as temp_file:
					    for item in liste_course:
					        temp_file.write("%s\n" % item)

					read_list()

				#dmd si veut retirer un autre élement de la liste
				while True:

					rhasspy.text_to_speech("Voulez vous retirer un autre élément de la liste")

					intent=rhasspy.speech_to_intent()

					if intent["name"] == "Oui":
						remove_items()

					elif intent["name"] == "Non":
						leave()

					elif intent["name"] == "":
						rhasspy.text_to_speech("je n'ai rien entendu.")
						continue

			else:
				rhasspy.text_to_speech("Je n'ai rien entendu")
				continue

	def remove_items():

		rhasspy.text_to_speech("Quel alimant voulez vous retirer de la liste?")
		while True:

			intent=rhasspy.speech_to_intent()

			#verifier si l'aliment est dans la liste de choix et dans la liste
			if intent["name"] == "remove_liste":

				ali = intent["variables"]["aliment"]

				for i in range(len(liste_course)):

					if intent["variables"]["aliment"] in liste_course[i].split():

						aliment = intent["variables"]["aliment"]
						quantite_remove(aliment,liste_course[i],i)

				rhasspy.text_to_speech(f"Vous n'avez pas de {ali} dans votre liste")
				continue

			else:
				rhasspy.text_to_speech(f"je n'ai rien entendu")

	def read_list():
		'''
		lis la liste de course
		'''
		rhasspy.text_to_speech("Votre liste est composé de :")
		print(liste_course)

		for i in liste_course:
			rhasspy.text_to_speech(i) 

	if len(liste_course) == 0: #si la liste est vide

			rhasspy.text_to_speech("Votre liste de course est vide. Voulez vous y ajoutez quelque chose?")

			while True:

				intent=rhasspy.speech_to_intent()

				# si pas de message 
				if intent["name"]=="":
					rhasspy.text_to_speech("je n'ai rien entendu. Vous n'avez pas encore de liste de course. Voulez vous en creez une nouvelle ?")
					continue

				elif intent["name"]=="Oui":
					print("Ajout aliment")
					print(liste_course)
					add_items()

				elif intent["name"]=="Non":
					leave()

	else: #si la liste n'est pas vide

		while True:

			rhasspy.text_to_speech("Vous avez une liste. Voulez ajoutez un alimant? Retirez un alimant ? Ou lire la liste? Dites STOP pour retourner au menu")

			intent=rhasspy.speech_to_intent()

			if intent["name"]=="":
				rhasspy.text_to_speech("je n'ai rien entendu")
				continue

			elif intent["name"] == "lire_liste":
				read_list()

			elif intent["name"] == "ajout_liste":
				add_items()

			elif intent["name"] == "retirer_liste":
				remove_items() 

			elif intent["name"] == "Stop":
				main()


			else:
				rhasspy.text_to_speech(f"Ceci n'est pas une commande valide")

##################
#   CODE CARTE   #
##################

def code():

	#afficher un cadenas
	logo.locker_logo() # import du fichier logo.py affiche un cadenas

	def leave():
		'''
		permet de retourner a la boucle global
		'''
		main()

	def code_joystick():
		
		if len(code_carte) < 4:


			num = 0
		
			sense.clear()
			sense.show_letter(str(num))


			while True:

				#recup les mouvements du joystick 
				event = sense.stick.wait_for_event(emptybuffer=True)
				time.sleep(0.3)
		
				#+1
				if event.direction == 'up':
		
					if num <9:
						num += 1
					else:
						num = 0
		
					sense.show_letter(str(num))

				#-1
				elif event.direction == "down":
		
					if num > 0:
						num -= 1
		
					else:
						num = 9
		
					sense.show_letter(str(num))
		

				#comfirmer
				elif event.direction == "middle":
					code_carte.append(str(num))
					code_joystick()

		else:
			new_code()


	def new_code():

		logo.locker_logo()

		print(f"nombre de chiffre dans le code: {len(code_carte)}")


		if len(code_carte) < 4:

			rhasspy.text_to_speech("entrez votre mot de passe a l'aide du joystick Haut et bas pour augmenter ou diminuer le chiffre et a appuyer au centre pour passer au chiffre suivant")

			code_joystick()


		else:

			#appel a la fct pour creer une suite de mot comme mdm
			new_word_pass()


	def read_list():

		rhasspy.text_to_speech("Votre mot de passe est composé de :")
		print(liste_mot)

		for i in liste_mot:
			rhasspy.text_to_speech(i) 


	def encrypt_mdp():

		mdp_carte = ""

		for i in code_carte:
			mdp_carte += i

		print(mdp_carte)

		suite_mot = ""

		for i in liste_mot:
			suite_mot += i

		print(suite_mot)

		print(suite_mot)

		suite_hacher = crypto.hashing(suite_mot)

		# mettre la suite hacher sur un fichier 

		#retire tout ce qui est sur le fichier 
		open('/home/pi/liste_hach.txt', 'w').close() 

		 
		with open('/home/pi/liste_hach.txt', 'w') as temp_file:
			temp_file.write(suite_hacher)

		print(suite_hacher)


		mdp_coder = crypto.encode(suite_mot,mdp_carte)
		print(mdp_coder)

		# mettre le mdp_coder dans un fichier 

		#retire tout ce qui est sur le fichier 
		open('/home/pi/carte_code.txt', 'w').close() 

		 
		with open('/home/pi/carte_code.txt', 'w') as temp_file:
			temp_file.write(mdp_coder)

		#retour au menu qd fini
		main()


	def new_word_pass():
		'''
		créer un nv mdp avec des mots commun pour trouver le code de la carte bancaire 
		'''
		rhasspy.text_to_speech("Quelle suite de mot voulez vous utilisez pour retrouver le mot de passe?")

		while True:

			rhasspy.text_to_speech("Dites votre mot et dites STOP quand vous avez assez de mot")

			intent = rhasspy.speech_to_intent()

			if intent["name"] == "add_liste":

				#aliment a rajouter 
				aliment = intent["variables"]["aliment"]

				liste_mot.append(aliment)
				rhasspy.text_to_speech(f"{aliment} a été rajouté a votre mot de passe")
				read_list()
				continue

			elif intent["name"] == "Stop":


				# si le mdp n'est pas assez long
				if len(liste_mot) < 3:
					rhasspy.text_to_speech("Votre mot de passe n'est pas assez long")
					continue

				else:
					rhasspy.text_to_speech("Fin du mot de passe")
					read_list()
					encrypt_mdp()

			else:
				rhasspy.text_to_speech("Je n'ai rien entendu")
				continue


	def fichier_vide():

		mot = ""

		with open('/home/pi/carte_code.txt', 'r') as temp_file:
			for line in temp_file.readlines():
				mot += line.rstrip()

			if len(mot) == 0:
				return True
			else:
				return False

	def decrypt_mdp():

		suite_mot = ""

		for i in liste_mot:
			suite_mot += i

		#hacher le input du user
		suite_hacher = crypto.hashing(suite_mot)

		#recup le hach sur le fichier

		hach_file = ""

		with open('/home/pi/liste_hach.txt', 'r') as temp_file:
			for line in temp_file.readlines():
				hach_file += line.rstrip()

		#si le bon mdp		
		if suite_hacher == hach_file:

			#afficher un sourire vert 
			logo.green_tick()

			carte_coder = ""

			with open('/home/pi/carte_code.txt', 'r') as temp_file:
				for line in temp_file.readlines():
					carte_coder += line.rstrip()

			mdp = crypto.decode(suite_mot,carte_coder)

			time.sleep(1)

			rhasspy.text_to_speech(f"Votre mot de passe est {mdp}")
			main()

		else:

			#afficher un sourire rouge
			logo.red_cross()

			time.sleep(1)
			rhasspy.text_to_speech(f"Mauvais mot de passe")
			main()


	if fichier_vide():

		while True:

			rhasspy.text_to_speech("Vous n'avez pas encore de code de carte enregistré. Voulez vous en enregistrez un ?")

			intent=rhasspy.speech_to_intent()

			# si pas de message 
			if intent["name"]=="":
				rhasspy.text_to_speech("je n'ai rien entendu.")
				continue

			elif intent["name"]=="Oui":
				print("Nouveau code de carte")
				new_code()

			elif intent["name"]=="Non":
				leave()

	# si deja un code propose de l'écouter avec le bon mdp 
	else:

		rhasspy.text_to_speech("Vous avez un code de carte enregistré.")

		liste_mot.clear()

		while True:

			rhasspy.text_to_speech("Dites votre mot et dites STOP quand vous avez assez de mot")

			intent = rhasspy.speech_to_intent()

			if intent["name"] == "add_liste":

				#aliment a rajouter 
				aliment = intent["variables"]["aliment"]

				liste_mot.append(aliment)
				rhasspy.text_to_speech(f"{aliment} a été rajouté a votre mot de passe")
				read_list()
				continue

			elif intent["name"] == "Stop":


				# si le mdp n'est pas assez long
				if len(liste_mot) < 3:
					rhasspy.text_to_speech("Votre mot de passe n'est pas assez long")
					continue

				else:
					rhasspy.text_to_speech("Fin du mot de passe")
					read_list()
					decrypt_mdp()

			else:
				rhasspy.text_to_speech("Je n'ai rien entendu")
				continue

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
			if intent["name"] == 'Blague' or intent["name"] == 'Temperature' or intent["name"] == 'Course' or intent["name"] == 'CodeCarte':
				rhasspy.text_to_speech("Vous avez lancé la commande {} ".format(intent["name"]))
				print(intent["name"])

			elif intent["name"] == "Arret" or intent["name"] == "Stop": # si cmd arret stop le programme
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

		elif intent["name"] == 'CodeCarte':
			code_carte.clear()
			liste_mot.clear()
			code()


if __name__ == "__main__":

	sense.low_light = True

	liste_course = []

	#chargement de la liste a partir du fichier liste_course.txt
	with open('/home/pi/liste_course.txt','r') as file:
		for line in file.readlines():
			liste_course.append(line.rstrip())

	# si le fichier est vide 
	if liste_course[0] == '':
		liste_course = []

	#chargement du mdp a partir du fichier  + du mdp avec des mots + si le fichier est vide 
	code_carte = [] 
	liste_mot = []




	print(f"liste de course : {liste_course}")
	

	main()

