
############################################################
# 			    PaPi			   #	
# 		      Code réalisé par 			   #	
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
import crypto 

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer 

'''sense.show_letter("A")
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

			rhasspy.text_to_speech("Vous avez une liste. Voulez ajoutez un alimant? Retirez un alimant ? Ou lire la liste?")

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

			else:
				rhasspy.text_to_speech(f"Ceci n'est pas une commande valide")

##################
#   CODE CARTE   #
##################

def code():

	#afficher un cadenas
	logo.locker_logo() # import du fichier logo.py affiche un cadenas
    
    '''
    1. Si aucun numero n’est enregistre, elle doit permettre d’enregistrer un nouveau numero 
    (a l’aide du joystick et du microphone), puis le nouveau code.
    2. Si un numero est deja enregistre, elle permet de tenter d’entrer le code,
     et d’afficher et  enoncer le numero si celui-ci est correct.
    3. Une fois le numero enonce et affiche, il peut etre detruit si souhaite 
    (retour au point 1), ou conserve (retour au point 2).
    '''

	def leave():
		'''
		permet de retourner a la boucle global
		'''
		main()

    
    #si pas de code dmd si on veut en creer un nouveau 

    def new_code():

    	number_of_numbers = 0

    	while number_of_numbers != 4:

    		if number_of_numbers == 0:
    			rhasspy.text_to_speech("Dites le premier numero du code a 4 chiffre")

    		elif number_of_numbers == 1:
    			rhasspy.text_to_speech("Dites le deuxième numero du code a 4 chiffre")

    		elif number_of_numbers == 2:
    			rhasspy.text_to_speech("Dites le troisième numero du code a 4 chiffre")

    		elif number_of_numbers == 3:
    			rhasspy.text_to_speech("Dites le dernier numero du code a 4 chiffre")

    		intent=rhasspy.speech_to_intent()


			if intent["name"] == "Code":

				while True:

					rhasspy.text_to_speech("Le numéro que vous avez dis va s'afficher sur l'écran appuyer vers le haut pour le comfirmer et vers le bas pour le changer")

					chiffre = intent["variables"]["nombre"]

					sense.show_letter(chiffre)

					#recup les mouvements du joystick 
					for event in sense.stick.get_events():

						#numero validé par l'utilisateur 
						if event.direction == 'up':

							#rajoute le chiffre donné au mdp
							code_carte += str(chiffre)

							number_of_numbers += 1

							new_code()


						#numero pas validé par l'utilisateur
						elif event.direction == "down":
							new_code()


			# si pas de message ou mauvaise cmd
			else:
				rhasspy.text_to_speech("je n'ai rien entendu.")
				continue


		#avec les 4 nums hacher le code et le mettre sur un fichier

		print(code_carte)



    if len(code_carte) == 0:

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

		rhasspy.text_to_speech("Vous avez deja un code fdp")



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
			if intent["name"] == 'Blague' or intent["name"] == 'Temperature' or intent["name"] == 'Course' or intent["name"] == 'Code':
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

		elif intent["name"] == 'Code':
			code()


if __name__ == "__main__":

	liste_course = []

	#chargement de la liste a partir du fichier liste_course.txt
	with open('/home/pi/liste_course.txt','r') as file:
		for line in file.readlines():
			liste_course.append(line.rstrip())

	# si le fichier est vide 
	if liste_course[0] == '':
		liste_course = []
        
    #chargement du mdp a partir du fichier  + du mdp avec des mots + si le fichier est vide 
    code_carte = "" #mdp hacher 
    code_mot = ""

    

    print(f"code_carte : {code_carte}")
    print(f"code_mot : {code_mot}")
	print(f"liste de course : {liste_course}")
	

	main()

