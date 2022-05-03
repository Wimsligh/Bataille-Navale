def create_grille():
    """Fonction qui permet de créer une grille de 11 lignes et 11 colonnes :
    -1ère ligne : Numérotation de 1 à 10 horizontalement
    -1ère colonne : Numérotation de A à J verticalement
    -Contenu de la grille : Des espaces"""
    nombre_lignes=10 #Choix du nombre de lignes pour le jeu
    nombre_colonnes=10 #Choix du nombre de colonnes pour le jeu
    case=" " #Choix de l'aspet des cases du jeu
    grille=[[case for x in range (nombre_colonnes+1)]for _ in range(nombre_lignes+1)] #Création du tableau par compréhension (on ajoute 1 au nombre de colonnes et de lignes pour placer les coordonnées)

    Alphabet={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J"} #Création d'un dictionnaire qui assigne aux entiers de 1 à 10, les lettres de A à J (chaines de caractères)

    colonne=0 #Création de la varibale colonne qui permettra de créer le nom de chaque colonne (Au début, elle vaut 0, c'est une colonne qui ne servira pas au jeu)

    ligne=Alphabet[1] #Création de la varibale ligne qui permettra de créer le nom de chaque ligne en utilisant le dictionnaire Alphabet afin de remplacer les entiers de 1 à 10 par des lettres de A à J (au début elle vaut A)

    for i in range(1,len(grille)): #On itère la liste principale en partant de la deuxième , la 1ère étant le renseignement des colonnes
        ligne=Alphabet[i] #On remplace la variable ligne par la lettre correspondant à la ligne
        grille[i][0]=ligne #On remplace le premier terme de chaque liste par la lettre correspondante
    for u in range (len(grille[0])): #On itère la 1ère liste de la liste principale
        grille[0][u]=str(colonne) #Pour renseigner les nombres de 0 à 10, sous forme ici d'une chaine de caractère
        colonne+=1 #On ajoute 1 à la variable colonne car on passe à la colonne suivante

    return grille #On renvoie la grille créée, qui servira de grille vide pour le jeu


def affiche_grille(grille:list): #procédure d'affichage
    """Permet d'afficher une grille en allant de ligne en ligne, pour que celle-ci est davantage l'apparence d'un plateau de jeu (un tableau)"""
    for i in grille: #A chaque ligne :
        print(i) #On affiche la ligne


def placement_bateaux(j1="Joueur 1",j2="Joueur 2"):
    """Phase de PLACEMENT des bateaux sur les grilles : Permet de placer les bateaux de la flotte où le désirent les deux joueurs, dans leurs propres grilles, qui seront sauvegardées pour continuer le jeu (ainsi que leur pseudonyme, renseignés en arguments et ayant des valeurs par défaut : "Joueur 1" et "Joueur 2")"""

    cases_boats={"Porte-avion":5,"Croiseur":4,"Sous-marin":3,"Torpilleur":2} #Dictionnaire qui renseigne le nombre de cases, soit la taille de chaque bateau
    flotte={"1":"Porte-avion","2":"Croiseur","3":"Sous-marin","4":"Torpilleur"} #Dictionnaire qui renseigne la touche à entrer par le joueur pour choisir un bateau
    Alphabet={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10} #Dictionnaire qui assigne aux entiers de 1 à 10, les lettres de A à J (soit les colonnes entrées par la joueur)

    sens={"1":"Horizontal (de la gauche vers la droite)","2":"Vertical (du haut vers le bas)"}#Dictionnaire qui renseigne la touche à entrer par le joueur pour choisir le sens de placement de son bateau

    colonne_str=["1","2","3","4","5","6","7","8","9","10"] #Liste comprenant les 10 colonnes du tableau mais sous forme de chaine de caractère

    grille_1=create_grille() #Création de la première grille (pour le joueur 1)
    grille_2=create_grille() #Création de la deuxième grille (pour le joueur 2)

    j=j1 #Variable j contenant d'abord le nom du joueur 1 puis le nom du joueur 2 (dans la boucle)
    grille=grille_1 #Variable grille contenant la grille du joueur 1 puis du joueur 2

    for _ in range (2): #Boucle qui répètera 2 fois le choix du placement des bateaux dans la grille (pour les 2 joueurs)

        print(f"\n {j} : c'est à vous de placer vos bateaux ! Votre adveraire détourne le regard...\n") #Phrase d'introduction au jeu qui appelle un des joueurs à placer ses bataux

        affiche_grille(grille) #On affiche tout d'abord sa grille vide pour qu'il choisisse où placer ses bateaux

        number_boats={"Porte-avion":1,"Croiseur":1,"Sous-marin":2,"Torpilleur":1} #Dictionnaire qui renseigne le nombre de bateaux restants du joueur, qui évoluera au fil du placement

        #Phase de choix du BATEAU + PLACEMENT :

        for u in range (1,6): #Boucle qui se répetera 5 fois (de 1 à 5) soit le nombre de bateaux à placer par chaque joueur

            #Annonce au joueur du reste de bateaux à placer :
            print(f"\nPlacement du bateau numéro {u} :")
            print(f"\n-Voici le nombre de bateaux de votre flotte: {number_boats}")

            #Choix du bateau et de son placement :

            bateau=str(input(f"\n-Quel bateau voulez-vous placer {flotte} (Nombre entre 1 et 4 à renseigner):")) #On demande au joueur quel type de bateau il veut placer (Nombre de 1 à 4 sous forme de chaine de caractère)


            #Phase de TEST sur le choix de bateau à placer du joueur (contrôles de saisie):

            Flag=False #On créer la variable Flag qui contient False par défaut et qui définira si les tests sont justes (True) ou si une erreur est détectée (False)

            while Flag==False: #Tant qu'une erreur est détectée, donc tant que Flag vaut False, on continue de réaliser les tests suivants et de redemander au joueur de choisir son bateau à placer :
                """Permet de faire rejouer le joueur s'il choisi un bateau plus disponible car déjà placé ou s'il a entré un choix de bateau qui n'esxiste pas"""

                Flag=True #Flag vaut ensuite "True", soit qu'aucune erreur est détectée et vaudra "False" à la première erreur mais permettra si ce n'est pas le cas, de sortir de la boucle
                texte="" #On crée une variable texte qui renseignera, si erreur détectée, le message de celle-ci

                if bateau not in flotte.keys(): #On teste d'abord si le nombre (sous forme de str) entré par la joueur correspond bien à un bateau, donc si c'est une clé renseignée dans le dictionnaire "flotte" :
                    Flag=False #Flag vaut donc : "False" si c'est le cas, car une erreur est détectée
                    texte="\nAttention ! Vous venez d'entrer un choix de bateau qui n'existe pas (doit être un nombre entre 1 et 4), réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici qu'il vient d'entrer un choix de bateau inexistant

                else: #S'il n'y a pas d'erreur sur un choix inexistant :
                    reste_bateau=number_boats[flotte[bateau]] #On créé une variable "reste_bateau" qui aura la valeur du reste des bateaux du bateau choisi (flotte[bateau]) soit en utilisant le dictionnaire "number_boats" : number_boats[flotte[bateau]]
                    if reste_bateau==0: #Puis on teste si celle-ci vaut 0, donc si le joueur vient de choisir un type de navire dont les bateaux ont été déjà tous placés
                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                        texte=f"\nAttention ! Vous ne pouvez plus placer un {flotte[bateau]} car ils sont tous déjà placés, retentez votre chance : \n-Voici le nombre de bateaux de votre flotte: {number_boats}" #Message pour faire prendre conaissance au joueur de son erreur et pour lui remontrer le nombre de ses bateaux afin qu'il ne choisisse plus un bateau déjà placé

                if Flag==False: #Tous les tests réalisés pour le choix de bateau du joueur, si erreur détectée, donc si Flag==False :
                    print(texte) #On affiche le message correspondant à l'erreur détectée

                    bateau=str(input(f"\n-Quel bateaux voulez-vous placer {flotte} :")) #Puis on lui redemande le bateau à placer

            reste_bateau-=1 #Si le joueur a bien fait son choix, on retire à la variable "reste_bateau" : 1
            number_boats[flotte[bateau]]=reste_bateau #Puis on remplace dans le dictionnaire number_boats, le nombre de bateaux restants du bateau choisi par le nouveau : "reste_bateau"

            print(f"\n-Voici le nouveau nombre de bateaux de votre flotte: {number_boats}") #Puis on affiche au joueur le nombre de bateaux de sa flotte après son choix


            ligne_bateau=str(input(f"\n--> La ligne où vous voulez placer la première case de votre {flotte[bateau]} (A,B,C...):")) #On demande au joueur de renseigner la ligne de la première case du bateau qu'il veut placer, entre A et J (chaine de caractère)

            colonne_bateau=str(input(f"\n--> La colonne où vous voulez placer la première case de votre {flotte[bateau]} (1,2,3...):")) #On demande au joueur de renseigner la colonne de la première case du bateau qu'il veut placer, entre 1 et 10 (chaine de carcatère)

            sens_bateau=str(input(f"\nDans quel sens {sens} :")) #Puis le sens dans lequel il veut placer son bateau : Horizontal->De gauche à droite, symbolisé par le "1" (chaine de carcatère) et : Vertical-> de haut en bas, symbolisé par le 2 (chaine de carcatère), visible grâce au dictionnaire "sens"




        #Phase de TEST sur le placement du bateau choisi (contrôles de saisie):

            Flag=False #On créer la variable Flag qui contient False par défaut et qui définira si les tests sont justes (True) ou si une erreur est détectée (False)
            while Flag==False: #Tant que une erreur est détectée, donc tant que Flag vaut False, on continue de réaliser les tests suivants et de redemander au joueur de placer son bateau :
                """Permet de vérifier:
                -si la ligne, la colonne et le sens sont bien entrés (compris dans les choix proposés)
                -s'il n'y a pas déjà de bateaux placés sur les cases du nouveau bateau
                -si le nouveau bateau n'en touche pas un autre (côte à côte)
                -si le bateau ne dépasse pas de la grille"""

                Flag=True #Flag vaut ensuite "True", soit qu'aucune erreur est détectée et vaudra "False" à la première erreur

                texte="" #On crée une variable texte qui renseignera, si une erreur est détectée, le message de celle-ci

                #Tests sur les choix du joueur :

                if ligne_bateau not in Alphabet.keys(): #Si la ligne n'est pas une clé dans le dictionnaire alphabet soit si elle n'est pas comprise entre A et J
                    Flag=False #Flag vaut donc : "False" si c'est le cas car erreur détectée
                    texte="\nAttention ! Vous avez renseigné une ligne qui n'existe pas, réessayez:" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur

                if colonne_bateau not in colonne_str: #Si la colonne choisie n'est pas comprise entre 1 et 10, sous forme de chaines de caractères disponibles dans "colonne_str"
                    Flag=False #Flag vaut : "False" si c'est le cas car une erreur est détectée
                    texte="\nAttention ! Vous avez renseigné une colonne qui n'existe pas, réessayez:" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur

                if sens_bateau not in sens.keys(): #Si le sens choisi n'est pas "1" et "2", donc s'il n'est pas présent dans les clés du dictionnaire indiquant les sens à choisir
                    Flag=False #Flag vaut : "False" si c'est le cas car une erreur est détectée
                    texte="\nAttention ! Vous avez renseigné un sens qui n'existe pas, réessayez:" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur

                if Flag==True: #Si aucune erreur a été faite sur les lignes, colonnes et sens (controlôles de saisie), on réalise le reste des tests sur le placement des bateaux (contrôles de cohérence)

                    l=Alphabet[ligne_bateau] #On peut donc créer une variable l qui sera la ligne choisie par le joueur pour son bateau mais sous la forme d'un entier entre 1 et 10, en utilisant le dictionnaire "Alphabet"
                    c=int(colonne_bateau) #Variable c qui sera la colonne choisie par le joueur mais sous forme d'entier, car il n'y aura pas eu d'erreur sur le choix du joueur

                    #Tests sur le placement du bateau (contrôles de cohérence):

                    if sens_bateau=="1": #Si le sens choisi par le joueur est 1 (str), soit horizontal (de gauche à droite)

                        if l==10: #si le bateau est à la dernière ligne

                            if grille[l-1][c]=="●" or grille[l][c-1]=="●": #vérifie si la première case n'est pas à côté d'un bateau (ligne au dessus et colonne derrière seulement car sinon, dépassement de la grille)
                                    Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                    texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur

                            elif cases_boats[flotte[bateau]]>11-c: #vérifie si le bateau ne dépasse pas la grille, soit que sa taille (son nombre de cases) n'est pas plus élevée que les cases disponibles (11 - la colonne choisie c)
                                Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                texte="\nAttention ! Votre bateau dépasse la grille, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur

                            else: #Si pour l'instant il n'y a pas d'erreur détectée, on continue les tests
                                for i in range(cases_boats[flotte[bateau]]): #On créer une boucle itérative qui se répetera le nombre de fois correspondant au nombre de cases du bateau
                                    if grille[l][c]=="●": #Vérifie si une des cases est déjà occupée
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                        texte="\nAttention ! Une des cases est déjà occupée par un de vos bateaux, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici qu'une case est occupée

                                    if grille[l-1][c]=="●": #Vérifie si le reste des cases n'est pas à côté d'un bateau sur la ligne du dessus (on teste juste la ligne au dessus car ligne en dessous -> dépassement de grille, colonne derrière -> même bateau et colonne devant si colonne vaut 10, dépassement
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                        texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici que le bateau en touche un autre
                                    if c!=10: #Si la case n'est pas à la fin du tableau (si ligne et colonne ne valent pas 10)
                                        if grille[l][c+1]=="●": #Vérifie si le reste des cases n'est pas à côté d'un bateau sur la colonne suivante
                                            Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                            texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici que le bateau en touche un autre

                                    c+=1 #On ajoute 1 à c pour avancer au test à la colonne suivante (on ne touche pas à la ligne l car c'est un mouvement horizontal, donc on reste dans la même ligne)


                        else: #Si on ne se trouve pas sur la dernière ligne

                            if grille[l-1][c]=="●" or grille[l][c-1]=="●" or grille[l+1][c]=="●": #Vérifie si la première case n'est pas à côté d'un bateau (ligne au dessus, colonne précédente et ligne en dessous)
                                Flag=False #Flag vaut donc : "False" si c'est le cas car erreur détectée
                                texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici que le bateau en touche un autre

                            elif cases_boats[flotte[bateau]]>11-c: #Vérifie si le bateau ne dépasse pas la grille (même procédé que pour l==10)
                                Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                texte="\nAttention ! Votre bateau dépasse la grille, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici que le bateau dépasse la grille

                            else: #Si pour l'instant il n'y a pas d'erreur détectée, on continue les tests
                                for i in range(cases_boats[flotte[bateau]]): #On créer une boucle itérative qui se répetera le nombre de fois correspondant au nombre de cases du bateau
                                    if grille[l][c]=="●": #Vérifie si une des cases est déjà occupée
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                        texte="\nAttention ! Une des cases est déjà occupée par un de vos bateaux, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici qu'une case est occupée

                                    if grille[l-1][c]=="●" or grille[l+1][c]=="●": #Vérifie si le reste des cases n'est pas à côté d'un bateau (ligne au dessus et ligne en dessous car colonne précédente-> ce bateau et colonne suivante si c==0-> dépassement de la grille)
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                        texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici que le bateau en touche un autre
                                    if c!=10: #Si la case n'est pas sur la dernière colonne du tableau
                                        if grille[l][c+1]=="●": #vérifie si reste des cases pas à côté d'un bateau sur la colonne suivante
                                            Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                            texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Et on assigne à "texte" l'erreur détectée sous forme d'un message au joueur, ici que le bateau en touche un autre

                                    c+=1 #On ajoute 1 à c pour avancer au test à la colonne suivante (on ne touche pas à la ligne l car c'est un mouvement horizontal, donc on reste dans la même ligne)




                    if sens_bateau=="2": #Si le sens choisi par le joueur est 2 (str), soit vertical (de haut en bas)

                        if c==10: #Si le bateau est sur la dernière colonne
                            if grille[l-1][c]=="●" or grille[l][c-1]=="●": #vérifie si la première case pas n'est pas à côté d'un bateau (ligne au dessus et colonne derrière seulement car sinon, dépassement de la grille)
                                Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Message de l'erreur détectée

                            elif cases_boats[flotte[bateau]]>11-l: #vérifie si le bateau ne dépasse pas la grille, soit que sa taille (son nombre de cases) n'est pas plus élevée que les cases disponibles (11 - la ligne choisie l)
                                Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                texte="\nAttention ! Votre bateau dépasse la grille, réessayez :" #Message de l'erreur détectée

                            else: #Si pour l'instant il n'y a pas d'erreur détectée, on continue les tests
                                for i in range(cases_boats[flotte[bateau]]): #On créer une boucle itérative qui se répetera le nombre de fois correspondant au nombre de cases du bateau
                                    if grille[l][c]=="●": #vérifie si une des cases est déjà occupée
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car erreur détectée
                                        texte="\nAttention ! Une des cases est déjà occupée par un de vos bateaux, réessayez :" #Message de l'erreur détectée

                                    if grille[l][c-1]=="●": #vérifie si reste des cases pas à côté d'un bateau sur la colonne précédente (on teste juste la colonne précédente car colonne suivante -> dépassement de grille, ligne au dessus -> même bateau et ligne suivante si ligne vaut 10-> dépassement)
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                        texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Message de l'erreur détectée
                                    if l!=10: #si la case n'est pas à la fin du tableau (si ligne et colonne ne valent pas 10)
                                        if grille[l+1][c]=="●": #vérifie si reste des cases pas à côté d'un bateau sur la ligne suivante
                                            Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                            texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Message de l'erreur détectée

                                    l+=1 #On ajoute 1 à l pour avancer au test à la ligne suivante (on ne touche pas à la colonne c car c'est un mouvement vertical, donc on reste dans la même colonne)


                        else: #Si on ne se trouve pas sur la dernière colonne

                            if grille[l-1][c]=="●" or grille[l][c-1]=="●" or grille[l][c+1]=="●": #vérifie si la première case n'est pas à côté d'un bateau (ligne au dessus, colonne précédente et colonne suivante)
                                Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Message de l'erreur détectée

                            elif cases_boats[flotte[bateau]]>11-l:  #vérifie si le bateau ne dépasse pas de la grille (même procédé que pour c==10)
                                Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                texte="\nAttention ! Votre bateau dépasse la grille, réessayez :" #Message de l'erreur détectée

                            else: #Si pour l'instant il n'y a pas d'erreur détectée, on continue les tests
                                for i in range(cases_boats[flotte[bateau]]): #On créer une boucle itérative qui se répetera le nombre de fois correspondant au nombre de cases du bateau
                                    if grille[l][c]=="●": #vérifie si une des cases est déjà occupée
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                        texte="\nAttention ! Une des cases est déjà occupée par un de vos bateaux, réessayez :" #Message de l'erreur détectée

                                    if grille[l][c+1]=="●" or grille[l][c-1]=="●": #vérifie si le reste des cases n'est pas à côté d'un bateau (colonne suivante et colonne précédente car ligne au dessous -> ce bateau et colonne suivante si l==0 -> dépassement de la grille)
                                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                        texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Message de l'erreur détectée
                                    if l!=10: #si la case n'est pas sur la dernière ligne
                                        if grille[l+1][c]=="●": #vérifie si le reste des cases n'est pas à côté d'un bateau sur la ligne suivante
                                            Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                                            texte="\nAttention ! Votre bateau en touche un autre, réessayez :" #Message de l'erreur détectée

                                    l+=1 #On ajoute 1 à l pour avancer au test à la ligne suivante (on ne touche pas à la colonne c car c'est un mouvement vertical, donc on reste dans la même colonne)


                if Flag==False: #Tous les tests réalisés pour les données entrées par le joueur, si une erreur est détectée, donc si Flag==False :
                    print(texte) #On affiche le message concernant l'erreur détectée (si plusieurs, seulement 1 sera affiché)
                    #Puis on redemande au joueur d'entrer ses choix :
                    ligne_bateau=str(input(f"\n--> La ligne où vous voulez placer la première case de votre {flotte[bateau]} (A,B,C...):"))
                    colonne_bateau=str(input(f"\n--> La colonne où vous voulez placer la première case de votre {flotte[bateau]} (1,2,3...):"))
                    sens_bateau=str(input(f"\nDans quel sens {sens} :"))

                #(Si Flag sera faux, on recommence les mêmes tests et le nouveau choix--> boucle : "while Flag==False", sinon on passe à la suite du code)




        #Phase de PLACEMENT sur la grille du joueur :

            if sens_bateau=="1": #Si le sens choisi par le joueur est 1 (str), soit horizontal (de gauche à droite)
                l=Alphabet[ligne_bateau] #Variable l qui est la ligne choisie (lettre entre A et J) par le joueur pour la première case de son bateau, sous la forme d'une entier entre 1 et 10
                c=int(colonne_bateau) #Variable c qui contient la colonne choisie pour placer la première case de son bateau mais en changeant son type en entier
                for i in range(cases_boats[flotte[bateau]]): #On réalise, le nombre de fois correspondant au nombre de cases du bateau choisi, le placement des pions du bateau
                    grille[l][c]="●" #La case d'index l et c devient un "●", le pion
                    c+=1 #On ajoute 1 à c pour avancer d'une colonne puis placer un nouveau pion car c'est un mouvement horizontal et on reste sur la même ligne mais on avance de colonne en colonne

            if sens_bateau=="2": #Si le sens choisi par le joueur est 2, soit vertical (de haut en bas)
                l=Alphabet[ligne_bateau] #Même procédé que pour le sens horizontal
                c=int(colonne_bateau) #Même procédé que pour le sens horizontal
                for i in range(cases_boats[flotte[bateau]]): #Même procédé que pour le sens horizontal
                    grille[l][c]="●" #On remplace ensuite la case d'index l et c par un pion "●"
                    l+=1 #On ajoute 1 à l pour avancer d'une ligne puis placer un nouveau pion car c'est un mouvement vertical et on reste sur la même colonne mais on avance de ligne en ligne

            affiche_grille(grille) #On affiche la grille contenant le nouveau bateau qui vient d'être placé

        print(f"\n Bravo {j}, vous avez fini de placer vos bateaux !\n") #Message d'information pour faire comprendre que le joueur a placé ses 5 bateaux

        j=j2 #La variable j contient maintenant le joueur 2 car c'est à lui de jouer
        grille=grille_2 #La variable grille contient maintenant la grille du deuxième joueur car c'est à lui de jouer

    plateau_jeu=[j1,grille_1,j2,grille_2] #Création d'une liste "plateau_jeu" dans laquelle est rensignée le nom de chaque joueur et la grille qu'ils viennent de remplir

    return plateau_jeu #On retourne cette liste pour qu'elle puisse être utilisée par la prochaine fonction : le combat



def combat_bateaux(plateau_jeu:list):
    """Phase de TIR : Permet d'utiliser un plateau de jeu sous forme d'une liste comportant : 2 noms de joueurs et 2 grilles dans lesquelles sont placés 5 bateauux, pour pouvoir effectuer une bataille en visant une case pour toucher puis couler les bateaux de son adversaire"""

    cases_boats={5:"Porte-avion",4:"Croiseur",3:"Sous-marin",2:"Torpilleur"} #Dictionnaire qui renseigne le nombre de cases, soit la taille de chaque bateau

    number_boats_1={"Porte-avion":1,"Croiseur":1,"Sous-marin":2,"Torpilleur":1} #Le nombre de bateaux restants de la flotte du joueur 1, soit le nombre de bateaux à couler par le joueur 2
    number_boats_2={"Porte-avion":1,"Croiseur":1,"Sous-marin":2,"Torpilleur":1} #Le nombre de bateaux restants de la flotte du joueur 2, soit le nombre de bateaux à couler par le joueur 1


    cases_restantes_boats_1={"Porte-avion":5,"Croiseur":4,"Sous-marin_1":3,"Sous-marin_2":3,"Torpilleur":2} #Le nombre de cases restantes de chaque bateau de la flotte du joueur 1, soit le nombre de cases à toucher par le joueur 2 pour couler chaque bateaux de son adversaire (Il y a deux sous-marins : "Sous-marin_1" et "Sous-marin_2")

    cases_restantes_boats_2={"Porte-avion":5,"Croiseur":4,"Sous-marin_1":3,"Sous-marin_2":3,"Torpilleur":2} #Le nombre de cases restantes de chaque bateau de la flotte du joueur 2, soit le nombre de cases à toucher par le joueur 1 pour couler chaque bateaux de son adversaire (Il y a deux sous-marins : "Sous-marin_1" et "Sous-marin_2")


    signe_bateau_1={1:"Porte-avion",2:"Croiseur",3:"Sous-marin",4:"Sous-marin",5:"Torpilleur"} #Création d'un dictionnaire renseignant le "signe" ou symbole de chaque bateau (de 1 à 5) de la flotte du joueur 1, selon leur ordre de placement dans la grille 1, permettant de savoir lequel a été touché/coulé

    signe_bateau_2={1:"Porte-avion",2:"Croiseur",3:"Sous-marin",4:"Sous-marin",5:"Torpilleur"}  #Création d'un dictionnaire renseignant le "signe" ou symbole de chaque bateau (de 1 à 5) de la flotte du joueur 2, selon leur ordre de placement dans la grille 2, permettant de savoir lequel a été touché/coulé


    Alphabet={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10} #Création cette fois, d'un dictionnaire qui assigne aux lettres de A à J (chaines de caractères)les entiers de 1 à 10

    colonne_str=["1","2","3","4","5","6","7","8","9","10"] #Liste comprenant les 10 colonnes du tableau mais sous forme de chaine de caractère

    j1=plateau_jeu[0] #Variable "j1", soit joueur 1 contient le premier élément de la liste "plateau_jeu" (argument), le nom du 1er joueur
    j2=plateau_jeu[2] #Variable "j2", soit joueur 2 contient le troisième élément de la liste "plateau_jeu", le nom du 2ème joueur
    grille_1=plateau_jeu[1] #Variable "grille_1" contient le deuxième élément de la liste "plateau_jeu", soit la grille du 1er joueur
    grille_2=plateau_jeu[3] #Variable "grille_2" contient le quatrième élément de la liste "plateau_jeu", soit la grille du 2ème joueur

    grille_tirs_1=create_grille() #On créé une grille pour l'instant vide "grille_tirs_1" qui servira pour afficher les tirs (touchés ou manqués) du joueur 1 sur la grille du joueur 2
    grille_tirs_2=create_grille() #On créé une grille pour l'instant vide "grille_tirs_1" qui servira pour afficher les tirs (touchés ou manqués) du joueur 2 sur la grille du joueur 1

    limite_signe_1=0 #Création d'une variable "limite_signe_1" qui permettra par la suite de réaliser une action qu'une seule fois dans la partie après un test, lors d'un tour du joueur 1
    limite_signe_2=0 #Création d'une variable "limite_signe_2" qui permettra par la suite de réaliser une action qu'une seule fois dans la partie après un test, lors d'un tour du joueur 2

    tours=0 #Création d'une variable "tours" qui correspond au nombre de tours de la phase de tir
    bateaux_coulés_1=0 #Variable "bateaux_coulés_1" qui correspond au nombre de bateaux coulés par le joueur 1, soit les bateaux coulés du joueur 2
    bateaux_coulés_2=0 #Variable "bateaux_coulés_2" qui correspond au nombre de bateaux coulés par le joueur 2, soit les bateaux coulés du joueur 1



    #Phase qui vise à déterminer le type de chaque navire dans chaque grille :

    grille_tampon_1=[a[:] for a in grille_1] #Création d'une variable "grille_tampon_1", une copie de la grille du joueur 1 en procédant par une copie de chaque listes de la liste principale par compréhension
    grille_tampon_2=[a[:] for a in grille_2] #Création d'une variable "grille_tampon_2", une copie de la grille du joueur 2 en procédant par une copie de chaque listes de la liste principale par compréhension

    signe_bateau=signe_bateau_1 #"signe_bateau" qui correspond dans un 1er temps au dictionnaire "signe_bateau_1" pour pouvoir être utilisée dans la boucle suivante car on commence par la grille du joueur 1
    grille_tampon=grille_tampon_1 #"grille_tampon" qui correspond dans un 1er temps à la copie de la grille du 1er joueur "grille_tampon_1" pour pouvoir être utilisée dans la boucle suivante car on commence par celle-ci pour déterminer les types de navire

    for _ in range(2): #Boucle qui répètera 2 fois la détermination du type des navires (pour les 2 grilles)
        signe=1 #Création de la variable "signe" qui sera la clé (dans le dictionnaire signe_bateau) du type de navire déterminé, soit le symbole de chaque bateau selon leur ordre de placment, elle vaut tout d'abord 1, donc le type de navire déterminé en premier aura comme "symbole", le 1
        for l in range(len(grille_tampon)): #On itère par indexation "grille_tampon"

            for c in range(len(grille_tampon[l])): #On itère ensuite par indexation les listes (lignes) de "grilles_tampon"
                L=l #Création d'une variable L pour modifier l'index de la ligne sans interférer dans l'itération
                C=c #Création d'une variable C pour modifier l'index de la colonne sans interférer dans l'itération
                nombre_cases=0 #Création de la variable (copmteur) "nombre_cases" qui permettra de déterminer le type des navires car on y renseignera leurs tailles
                if grille_tampon[l][c]=="●": #Si la case de la "grille_tampon" à la ligne l et la colonne c, est un pion ("●"), donc si c'est la première case d'un bateau :

                    nombre_cases+=1 #On ajoute 1 au compteur du nombre de cases

                    if c!=10 and l!=10: #Ensuite on teste si la première case des bateaux ne se trouve ni sur la dernière colonne et ni sur la dernière ligne (car des erreurs de dépassement de grille pourraient arriver)

                #On détermine ensuite le type de navire en partant de la première case d'index l et c en parcourant le reste de ses cases

                        while grille_tampon[L][C]=="●" and L<10 and C<10: #Si c'est le cas, on entre dans une boucle conditionnelle : tant que la case de "grille_tampon" de ligne L et de colonne C est un pion, donc tant qu'on se trouve sur un bateau, et tant que la ligne L et la colonne C n'atteignent pas 10 on continue d'avancer de case en case pour compter le nombre de cases du bateau et donc son type :
                            grille_tampon[L][C]=signe #Tant que c'est le cas on remplace le pion de la case par le signe correspondant à l'ordre de placement des bateaux
                            if grille_tampon[L+1][C]=="●": #On teste donc ensuite si la case à la ligne suivante est un pion
                                nombre_cases+=1 #Si c'est le cas on ajoute 1 au compteur de cases
                                L+=1 #Puis on ajoute 1 à la ligne L car on se trouve sur un bateau qui a été placé verticalement et on passe donc au pion suivant du bateau
                                if L==10: #Si la ligne de la case du pion suivant est la dixième
                                    grille_tampon[L][C]=signe #On le remplace par le signe du bateau concerné
                            if grille_tampon[L][C+1]=="●": #Dans l'autre cas, on teste si la case à la colonne suivante est un pion, donc si le bateau a été placé horizontalement
                                nombre_cases+=1 #Si c'est le cas on ajoute 1 au compteur de cases
                                C+=1 #Puis on ajoute 1 à la colonne C car on se trouve sur un bateau qui a été placé horizontalement et on passe donc au pion suivant du bateau
                                if C==10: #Si la colonne de la case du pion suivant est la dixième
                                    grille_tampon[L][C]=signe #On le remplace par le signe du bateau concerné




                    else: #Si la première case du bateau se trouve soit sur la dernière ligne, soit sur la dernière colonne :
                        if c==10: #Si c'est la dernière colonne :
                            while grille_tampon[L][C]=="●" and L<10: #Boucle conditionelle : Tant que la case de "grille_tampon" de ligne L et de colonne C est un pion, donc tant qu'on se trouve sur un bateau, et tant que la ligne L n'atteint pas 10, on continue d'avancer de case en case pour compter le nombre de cases du bateau et donc son type
                                grille_tampon[L][C]=signe #Tant que c'est le cas on remplace le pion de la case par le signe correspondant à l'ordre de placement des bateaux
                                if grille_tampon[L+1][C]=="●": #On teste ensuite si la case à la ligne suivante est un pion (On ne teste pas la colonne suivante car si la première case d'un bateau se trouve sur la dernière colonne, il est forcément placé verticalement)
                                    nombre_cases+=1 #Si c'est le cas on ajoute 1 au compteur de cases
                                    L+=1 #Puis on ajoute 1 à la ligne L car on se trouve sur un bateau qui a été placé verticalement et on passe donc au pion suivant du bateau
                                if L==10: #Si la ligne de la case du pion suivant est la dixième
                                    grille_tampon[L][C]=signe #On le remplace par le signe du bateau concerné

                        if l==10: #Si la première case du bateau se trouve sur la dernière ligne :
                                while grille_tampon[L][C]=="●" and C<10: #Boucle conditionelle : Tant que la case de "grille_tampon" de ligne L et de colonne C est un pion, donc tant qu'on se trouve sur un bateau, et tant que la colonne C n'atteint pas 10, on continue d'avancer de case en case pour compter le nombre de cases du bateau et donc son type
                                    grille_tampon[L][C]=signe #Tant que c'est le cas on remplace le pion de la case par le signe correspondant à l'ordre de placement des bateaux
                                    if grille_tampon[L][C+1]=="●": #On teste ensuite si la case à la colonne suivante est un pion (On ne teste pas la ligne suivante car si la première case d'un bateau se trouve sur la dernière ligne, il est forcément placé horizontalement)
                                        nombre_cases+=1 #Si c'est le cas on ajoute 1 au compteur de cases
                                        C+=1 #Puis on ajoute 1 à la colonne C car on se trouve sur un bateau qui a été placé verticalement et on passe donc au pion suivant du bateau
                                    if C==10: #Si la colonne de la case du pion suivant est la dixième
                                        grille_tampon[L][C]=signe #On le remplace par le signe du bateau concerné


                    bateau=cases_boats[nombre_cases] #Une fois le bateau entièrement remplacé par son symbole "signe" correspondant à son ordre de placement dans la grille, et son nombre de cases "nombre_cases" compté, on créé la variable "bateau" qui renseignera le type de ce navire à partir de son nombre de cases grâce au dictionnaire "cases_boats"

                    signe_bateau[signe]=bateau #Ensuite on remplace dans le dictionnaire "signe_bateau" le bateau assigné au signe correspondant, par celui déterminé : "bateau"

                    signe+=1 #Puis on ajoute 1 au signe, pour que le bateau suivant soit représenté par le nombre correspondant à son ordre de placement


        signe_bateau=signe_bateau_2 #"signe_bateau" qui correspond maitenant au dictionnaire "signe_bateau_2" car on passe à la grille du joueur 2

        grille_tampon=grille_tampon_2 #"grille_tampon" qui correspond maintenant à la copie de la grille du 2ème joueur "grille_tampon_2" car on détermine les types de navire de celle-ci


    print("\nPlace au combat !") #On affiche un message au joueur pour lui annoncer que la phase de TIR/COMBAT commence

    while bateaux_coulés_1<5 and bateaux_coulés_2<5: #Boucle conditionnelle : Tant qu'un des deux joueurs n'a pas coulé tous les bateaux de son adversaire, on continue la phase de tir :

        tours+=1 #Variable "tours" qui correspond au nombre de tours joués par les joueurs

        j=j1 #Variable "j" qui correspond au joueur qui tire, ici "j1", le joueur 1
        autre_j=j2 #Variable "autr_j" qui correspond au joueur qui ne tire pas, ici "j2", le joueur 2

        grille=grille_2 #"grille" qui correspond à la grille de l'adversaire du joueur qui tire, ici "grille_2", la grille du joueur 2
        grille_tirs=grille_tirs_1 #"grille_tirs" qui correspond à la grille des tirs du joueur qui tire, ici "grille_tirs_1", la grille de tirs du joueur 1

        number_boats=number_boats_2 #"number_boats" qui correspond au dictionnaire du nombre de bateaux restants de la flotte du joueur qui ne tire pas, ici "number_boats_2", du joueur 2
        cases_restantes_boats=cases_restantes_boats_2 #"cases_restantes_boats" qui correspond au dictionnaire du nombre de cases restantes de chaque bateau de la flotte du joueur qui ne tire pas, ici "cases_restantes_boats_2" du joueur 2

        grille_tampon=grille_tampon_2 #"grille_tampon" qui correspond à la grille dans laquelle est renseignée les types de navire (à partir de leur signe) du joueur qui ne tire pas, ici "grille_tampon_2" du joueur 2
        signe_bateau=signe_bateau_2 #"signe_bateau" qui correspond au dictionnaire qui renseigne les signes correspondant à chaque bateaux de la flotte du joueur qui ne tire pas, ici le joueur 2 : "signe_bateau_2"


        for i in range(2): #Boucle qui répètera 2 fois le choix d'une case à viser sur la grille adverse (pour les 2 joueurs, chacun leur tour)



            #Affichage du nombre de tours déjà réalisés et de la grille de tirs du joueur qui attaque, représentant la grille de son adversaire :
            print(f"\nTour {tours} : {j} c'est à toi d'attaquer :")
            print(f"\nGrille de {autre_j}:\n")
            affiche_grille(grille_tirs)

            #On demande au joueur la ligne (l_attaque, sous forme d'une lettre de A à J) et la colonne (c_colonne, entier de 1 à 10) de la case qu'il veut viser dans la grille adverse
            l_attaque=str(input("\n--> La ligne de la case que vous voulez viser (A,B,C...):"))
            c_attaque=str(input("\n--> La colonne de la case que vous voulez viser (1,2,3...):"))


            #Phase de TEST (contrôles de saise + cohérence):


            Flag=False #On créer la variable Flag qui contient False par défaut et qui définira si les tests sont justes (True) ou si une erreur est détectée (False)

            while Flag==False: #Tant qu'une erreur est détectée, donc tant que Flag vaut False, on continue de réaliser les tests suivants et on redemande au joueur de choisir la case visée :
                """Permet de vérifier si :
                -la ligne et la colonne de la case visée existent
                -la case visée n'a pas déjà été visée"""

                Flag=True #Variable Flag qui sera vraie "True" tant qu'aucune erreur ne sera détectée

                texte="" #On crée une variable texte qui renseignera, si erreur détectée, le message de celle-ci

                if l_attaque not in Alphabet.keys(): #Si la ligne "l_attaque" n'est pas dans le dictionnaire alphabet soit si elle n'est pas comprise entre A et J :
                    Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                    texte="\nAttention ! Vous avez renseigné une ligne qui n'existe pas, réessayez:" #Et on assigne à "texte" le message de l'erreur détectée, ici que la ligne a été mal renseignée
                if c_attaque not in colonne_str: #Si la colonne n'est pas comprise entre 1 et 10 sous forme de chaine de caractère, donc si elle n'est pas présente dans la liste "colonne_str"
                    Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                    texte="\nAttention ! Vous avez renseigné une colonne qui n'existe pas, réessayez:" #Et on assigne à "texte" le message de l'erreur détectée, ici que la colonne a été mal renseignée

                if Flag==True: #Si aucune erreur a été faite sur les lignes et colonnes de la case attaquée on réalise le reste des tests sur l'emplacement de la case choisie

                    l=Alphabet[l_attaque] #On peut donc créer une variable l qui contient la ligne choisie par le joueur pour tirer mais sous la forme d'un entier entre 1 et 10, en utilisant le dictionnaire "Alphabet"
                    c=int(c_attaque)#Variable c qui contient la colonne choisie par le joueur sous forme d'un entier en fonctionnant par un "cast" car l'existence de la colonne a été vérifiée

                    if grille_tirs[l][c]=="X" or grille_tirs[l][c]=="O": #Si cette case choisie a déjà été attaquée, donc si le tir a été manqué ("O") ou s'il a touché un navire ("X") :
                        Flag=False #Flag vaut donc : "False" si c'est le cas car une erreur est détectée
                        texte=("\nAttention ! Cette case a déjà été visée, réessayez :") #Et on assigne à "texte" le message de l'erreur détectée, ici que la case visée a déjà été visée

                if Flag==False: #Si Flag est "False", donc si une erreur a été détectée
                    print(texte) #On affiche le texte correspondant à l'erreur
                    #On redemande au joueur de renseigner la ligne et la colonne de la case visée :
                    l_attaque=str(input("\n--> La ligne de la case que vous voulez viser (A,B,C...):"))
                    c_attaque=str(input("\n--> La colonne de la case que vous voulez viser (1,2,3...):"))


            l=Alphabet[l_attaque] #Une fois les tests réalisés, on assigne à la variable l, la ligne choisie par le joueur pour tirer mais sous la forme d'un entier entre 1 et 10, en utilisant le dictionnaire "Alphabet"
            c=int(c_attaque) #Variable c qui contient la colonne choisie par le joueur mais sous forme d'un entier en fonctionnant par un "cast" car l'existence de la colonne a été vérifiée

            #Phase dite de "TIR" :


            if grille[l][c]=="●": #Si case visée est un pion, donc si un bateau est touché  :
                print("\nTouché !\n") #On affiche au joueur "Touché !"
                grille_tirs[l][c]="X" #Puis on place aux mêmes indexs que la case visée, un "X" sur la grille des tirs du joueur, symbole d'un bateau touché sur cette case

                bateau_touché=signe_bateau[grille_tampon[l][c]] #Ensuite on utilise la grille_tampon qui renseigne le signe de chaque bateau, ici celui sur la case visée, puis le dictionnaire qui le fait correspondre avec le type de bateau, pour déterminer le bateau touché, soit "bateau_touché



                if bateau_touché=="Sous-marin": #Si le type de navire touché est le "Sous-marin" alors on va différencier les deux sous-marins du joueur adverse disponibles sur la grille :
                    if i==0: #Si i==0 (une fois sur 2) donc si c'est le joueur 1 qui tire:
                        if limite_signe_1==0: #Utilisation de la variable "limite_signe_1" qui va permettre lors d'un seul tour du joueur 1 où il visera un des sous-marin, car après elle vaudra 1, de :
                            signe_sous_marin_diff_1=grille_tampon[l][c] #Créer une variable "signe_sous_marin_diff_1" qui contiendra le signe/symbole (disponible dans "grille_tampon") du premier sous-marin touché par le joueur 1 pour qu'on puisse les différencier
                            limite_signe_1=1 #Elle vaut maintenant 1, pour que cette action n'est plus lieu

                        if grille_tampon[l][c]==signe_sous_marin_diff_1: #On peut donc ensuite tester si ce signe du premier sous-marin touché est le même que le sous-marin touché
                            sous_marin_touché="Sous-marin_1" #Si c'est le cas, la variable "sous_marin_touché" contient le 1er sous-marin : "Sous-marin_1"
                        else: #Sinon, c'est le second sous-marin qui est touché donc  :
                            sous_marin_touché="Sous-marin_2" #Elle contient l'autre sous-marin, soit "Sous-marin_2"

                    else: #Si i==1 (une fois sur 2) donc si c'est le joueur 2 qui tire:
                        #On applique le même procédé :
                        if limite_signe_2==0: #Utilisation de la variable "limite_signe_2" qui va permettre lors d'un seul tour du joueur 2 où il visera un des sous-marin, car après elle vaudra 1, de :
                            signe_sous_marin_diff_2=grille_tampon[l][c] #Créer une variable "signe_sous_marin_diff_2" qui contiendra le signe/symbole (disponible dans "grille_tampon") du premier sous-marin touché par le joueur 2 pour qu'on puisse les différencier
                            limite_signe_2=1 #Elle vaut maintenant 1, pour que cette action n'est plus lieu

                        if grille_tampon[l][c]==signe_sous_marin_diff_2: #On peut donc ensuite tester si ce signe du premier sous-marin touché est le même que le sous-marin touché
                            sous_marin_touché="Sous-marin_1" #Si c'est le cas, la variable "sous_marin_touché" contient le 1er sous-marin : "Sous-marin_1"
                        else: #Sinon c'est le second sous-marin qui est touché donc  :
                            sous_marin_touché="Sous-marin_2" #Elle contient l'autre sous-marin, soit "Sous-marin_2"

                    cases_restantes_boats[sous_marin_touché]-=1 #Maintenant qu'on sais quel sous-marin a été touché, on peut lui retirer 1 à ses cases restantes dans : "cases_restantes_boats"

                else: #Si le type de navire n'est pas le sous-marin ;
                    cases_restantes_boats[bateau_touché]-=1 #On retire 1 aux cases restantes de ce bateau car une de celles-ci vient d'être touchée



                if bateau_touché=="Sous-marin": #Si le bateau touché est un sous-marin
                    if cases_restantes_boats[sous_marin_touché]==0: #Si le sous-marin touché n'a plus de cases restantes, donc s'il a été coulé :
                        print(f"{sous_marin_touché} coulé !") #On affiche au joueur qu'il vient de couler un navire, ici on précise quel sous-marin des deux
                        number_boats[bateau_touché]-=1 #Puis on retire 1 au nombre de bateaux de ce type dans la flotte du joueur adverse

                        if i==0: #Si i==0 (une fois sur 2) donc si c'est le joueur 1 qui tire:
                            bateaux_coulés_1+=1 #On ajoute 1 au nombre de bateaux que le joueur 1 à couler de la flotte du joueur 2
                        else: #Si i==1 (une fois sur 2) donc si c'est le joueur 2 qui tire:
                            bateaux_coulés_2+=1 #On ajoute 1 au nombre de bateaux que le joueur 2 à couler de la flotte du joueur 1

                    else: #Si le sous-marin n'a pas coulé, il est seulement touché, donc :
                        print(f"{sous_marin_touché} touché ! Il lui reste {cases_restantes_boats[sous_marin_touché]} case(s) avant de couler :") #On affiche au joueur le sous-marin touché et le reste de ses cases




                elif cases_restantes_boats[bateau_touché]==0: #De manière plus générale (quand le bateau touché n'est pas un sous-marin), si le nombre de cases restantes renseignées dans le dictionnaire "cases_restantes_boats" du bateau touché vaut 0 alors le bateau touché est coulé :
                    print(f"{bateau_touché} coulé !") #On affiche donc au joueur qu'il vient de couler un navire, et le type de celui ci ("bateau_touché")
                    number_boats[bateau_touché]-=1 #Puis on retire 1 aux nombre de bateaux de ce type dans la flotte du joueur adverse

                    #De la même manière :

                    if i==0: #Si i==0 (une fois sur 2) donc si c'est le joueur 1 qui tire:
                        bateaux_coulés_1+=1 #On ajoute 1 au nombre de bateaux que le joueur 1 à couler de la flotte du joueur 2
                    else: #Si i==1 (une fois sur 2) donc si c'est le joueur 2 qui tire:
                        bateaux_coulés_2+=1 #On ajoute 1 au nombre de bateaux que le joueur 2 à couler de la flotte du joueur 1

                else: #En revanche, si aucun bateau n'est coulé, il faut avertir le joueur qu'il a tout de même touché un bateau

                    print(f"{bateau_touché} touché ! Il lui reste {cases_restantes_boats[bateau_touché]} case(s) avant de couler :") #On affiche donc au joueur quel bateau il vient de toucher et combien il lui reste de cases à viser avant de le couler


                print(f"\n->Flotte de {autre_j} : {number_boats}\n\n->Leurs cases restantes : {cases_restantes_boats}\n") #On affiche, après le tir, l'état de la flotte du joueur adverse avec le nombre de bateaux restants ("number_boats") et leur nombre de cases restantes ("cases_restantes_boats")

            else: #Si aucun bateau n'est sur la case visée, donc si le tir est manqué
                print("\nManqué !\n") #On affiche au joueur "Manqué !"
                grille_tirs[l][c]="O" #Puis on place aux mêmes indexs que la case visée, un "O" sur la grille des tirs du joueur, symbole d'un tir raté sur cette case

            print("Résumé de vos attaques :\n") #On annonce ce qu'on affiche au joueur :
            affiche_grille(grille_tirs) #On affiche au joueur sa grille de tirs après son tir

            #C'est au tour du joueur 2 :
            j=j2 #On passe au joueur 2
            autre_j=j1 #Le joueur adverse est maintenant le joueur 1
            grille=grille_1 #La grille attaquée est celle du joueur 1
            grille_tirs=grille_tirs_2 #La grille représentant les tirs est celle du joueur 2


            number_boats=number_boats_1 #Le nombre de bateaux restants est celui du joueur 1
            cases_restantes_boats=cases_restantes_boats_1 #Les cases restantes des bateaux sont celles du joueur 1

            grille_tampon=grille_tampon_1 #La grille tampon qui renseigne le type de chaque navire est celle du joueur 1 car c'est sa grille qui est attaquée
            signe_bateau=signe_bateau_1 #Puis les correspondances entre les signes et les types de navire sont les siennes

    #Une fois que le jeu est fini, soit qu'au moins un des deux joueurs a coulé tous les navires de son adversaire :
    if bateaux_coulés_1==5 and bateaux_coulés_2==5: #Si les deux joueurs ont coulé leurs 5 bateaux :
        print(f"\nAprès les {tours} tours vous êtes, {j1} et {j2} à égalité !") #On annonce donc aux deux joueurs l'égalité et le nombre de tours effectués
        resultat=f"Egalité entre {j1} et {j2} !" #La variable "resultat" contient donc le message de l'égalité

    elif bateaux_coulés_1==5:  #Si c'est le nombre de bateaux coulés du joueur 2 par la joueur 1 qui vaut 5 (et qu'il n'y a pas eu d'égalité):
        print(f"\nTous les bateaux de {j2} ont été coulés en {tours} coups !\nBravo au gagnant {j1} !") #On annonce donc au joueur 1 sa victoire et le nombre de tours effectués
        resultat=f"Victoire de {j1} !" #La variable "resultat" contient donc le message de victoire du joueur 1 : "j1"

    elif bateaux_coulés_2==5: #Si c'est le nombre de bateaux coulés du joueur 1 par la joueur 2 qui vaut 5 (et qu'il n'y a pas eu d'égalité):
        print(f"\nTous les bateaux de {j1} ont été coulés en {tours} coups !\nBravo au gagnant {j2} !") #On annonce donc au joueur 2 sa victoire et le nombre de tours effectués
        resultat=f"Victoire de {j2} !" #La variable "resultat" contient donc le message de victoire du joueur 2 : "j2"

    return resultat #Et on renvoie le résultat final de la partie

def NavalWar(j1="Joueur 1",j2="Joueur 2"):
    """Dernière fontion qui rassemble les deux phases du jeu :
    -Le placement des bateaux, sous la forme d'une fonction : placement_bateaux
    -Le phase dite de tir, sous la forme d'une fonction : combat_bateaux
    Celle-ci prend en argument les deux noms des joueurs, appelle ces deux fonctions et renverra la nom du gagnant"""
    plateau_jeu=placement_bateaux(j1,j2) #On appelle la fonction "placement_bateaux" (à laquelle on renseigne les deux noms des joueurs) en créant "plateau_jeu" qui contiendra le retour de celle-ci, soit la liste contenant le nom de chaque joueur et leur grille remplie de leurs bateaux
    resultat=combat_bateaux(plateau_jeu) #On appelle la fonction "combat_bateaux" (prenant en argument la liste précédemment créée "plateau_jeu") en créant "resultat" qui contiendra le retour de celle-ci, soit le résultat final de cette partie de bataile navale
    return resultat #Puis on renvoie ce résultat

#Pour jouer une partie de bataille navale : on appelle donc la fonction : NavalWar()