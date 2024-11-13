import random,csv, webbrowser, subprocess
ordre_elt = {"Plante":"Eau","Eau":"Feu","Feu":"Plante","Bonbons":"Robot","Robot":"Lumiere","Lumiere":"Bonbons",'Vide':'Vide'}
carte_rects_j2 = []
carte_rects_j1 = []

def read_csv_to_list(filename):
    liste = []
    with open(filename, mode='r', newline='', encoding='ansi') as file:
        reader = csv.reader(file, delimiter=';')
        for lines in reader:
            liste.append(lines)
    return liste

class Plateau:
    def __init__(self,nom):
        self.__nom = nom
        self.ligne = [[" "," "," "," "," "],[" "," "," "," "," "]]
    def get_nom(self):
        return self.__nom
    def get_ligne(self):
        print(f"{self.ligne[0]}\n{self.ligne[1]}")
    def put_carte(self,position): # l'argument position est compris entre 0 et 9
        if position < 5 :
            self.ligne[0][position] = "Y"
        else:
            self.ligne[1][position-5] = "Y"
    def remove_carte(self,position): # l'argument position est compris entre 0 et 9
        if position < 5 :
            self.ligne[0][position] = " "
        else:
            self.ligne[1][position-5] = " "
    def set_nom(self, nom):
        self.__nom = nom
        
class PlateauBot:
    def __init__(self,Plateau) :
        self.__nom = Plateau.get_nom()
        self.ligne = Plateau.ligne
        self.init_pos()
        
    def init_pos(self): # Cette fonction permet de créer un plateau aléatoire pour le bot.
        compteur_x = 0
        while compteur_x<7:
            lig = random.randint(0,1)
            col = random.randint(0,4)
            if self.ligne[lig][col]!= "X":
                self.ligne[lig][col] = "X"
                compteur_x+=1
    def get_nom(self):
        return self.__nom
    def get_ligne(self):
        print(f"{self.ligne[0]}\n{self.ligne[1]}")
    def put_carte(self,position): # l'argument position est compris entre 0 et 9
        if position < 5 :
            self.ligne[0][position] = "Y"
        else:
            self.ligne[1][position-5] = "Y"
    def remove_carte(self,position): # l'argument position est compris entre 0 et 9
        if position < 5 :
            self.ligne[0][position] = " "
        else:
            self.ligne[1][position-5] = " "
    def set_nom(self, nom):
        self.__nom = nom

class Joueur :
    def __init__(self,nom):
        self.liste = []
        self.liste_placement = []
        self.nom = nom
        self.__pv = 30
        while len(self.liste) != 7: # Cette fonction ajoute dans la main du joueur des cartes aléatoires
            ran = random.randint(0, 20)
            compteur = 0
            for i in range(len(self.liste)):
                if self.liste[i] == valamonlist[ran]:
                    compteur += 1
            if compteur == 0:
                self.liste.append(valamonlist[ran])
        self.tri_cartes()
        for i in range(len(self.liste)):
            self.liste_placement.append(self.liste[i])
    def __sub__(self,valeur):
            self.__pv - valeur
    def get_pv(self):
            return self.__pv
    def get_liste(self):
            return self.liste
    def set_pv(self,valeur):
            self.__pv = valeur
    def sous_pv(self,valeur):
            self.__pv -= valeur
    def add_pv(self,valeur):
            self.__pv += valeur
    def tri_cartes(self):
        l = []
        for _ in range(7):
            mini = self.liste[0]
            for i in range(len(self.liste)):
                if self.liste[i].get_pv() < mini.get_pv():
                    mini = self.liste[i]
            l.append(mini)
            self.liste.remove(mini)
        self.liste = l
            

class Bot :
    def __init__(self,nom):
        self.liste = []
        self.nom = nom
        self.__pv = 30
        while len(self.liste) != 7: # Cette fonction ajoute dans la main du bot des cartes aléatoires
            ran = random.randint(0, 20)
            compteur = 0
            for i in range(len(self.liste)):
                if self.liste[i] == valamonlist[ran]:
                    compteur += 1
            if compteur == 0:
                self.liste.append(valamonlist[ran])
    def __sub__(self,valeur):
            self.__pv - valeur
    def get_pv(self):
            return self.__pv
    def get_liste(self):
            return self.liste
    def set_pv(self,valeur):
            self.__pv = valeur
    def sous_pv(self,valeur):
            self.__pv -= valeur
    def add_pv(self,valeur):
            self.__pv += valeur

class Valamon:
    def __init__(self, nom, pv, pvmax, atk1, atk2, soin1, soin2, soincol1, soincol2, elt1, elt2, titreatk1, titreatk2):
        self.nom = nom
        self.pv = pv
        self.__pvmax = pvmax
        self.atk1 = atk1
        self.titre1 = titreatk1
        self.atk2 = atk2
        self.titre2 = titreatk2
        self.elt1 = elt1
        self.elt2 = elt2
        self.soin1 = soin1
        self.soin2 = soin2
        self.__soincol1 = soincol1
        self.__soincol2 = soincol2

    def __str__(self):
        return f"Nom : {self.nom}\nPV : {self.pv}\nAttaque 1 : {self.titre1}\nDégats d'attaque 1 : {self.atk1}\nAttaque 2 : {self.titre2}\nDégats d'attaque 2 : {self.atk2}\nÉlément 1 : {self.elt1}\nÉlément 2 : {self.elt2}"

    def __sub__(self, valeur):
        self.pv -= valeur

    def get_pvmax(self):
        return self.__pvmax
    def get_pv(self):
        return self.pv
    def set_pv(self,valeur):
        self.pv = valeur
    def set_pvmax(self,valeur):
        self.__pvmax = valeur
    def set_atk1(self,valeur):
        self.atk1 = valeur
    def set_atk2(self,valeur):
        self.atk2 = valeur
        
    def elt_check(self,vala):
        global ordre_elt
        if self.elt2 != 'Vide' or vala.elt2 != 'Vide':
            if ordre_elt[self.elt2] == vala.elt2:
                return 2
        if ordre_elt[self.elt1] == vala.elt1 :
            return 2
        else:
            return 0

    
    def attaque1(self, vala, player, player2, pos, pos_a, pos_b):
        a = self.elt_check(vala)
        vala - (self.atk1 + a)
        if self.__soincol1 == 0:
            if not self.pv + self.soin1 > self.__pvmax:
                self.pv += self.soin1
        else:
            for i in range(len(player.liste)):
                if player.liste[i].pv + self.soin1 <= player.liste[i].get_pvmax():
                    player.liste[i].pv += self.soin1
        if vala.get_pv() <= 0:
            if player2.nom == "Bot":
                player2.liste.pop(pos)
                carte_rects_j2.pop(pos)
                for i in range(pos, len(carte_rects_j2)):
                    carte_rects_j2[i][0] = i
                PlateauBOT.ligne[pos_a][pos_b] = ' '
            else :
                player2.liste.pop(pos)
                carte_rects_j1.pop(pos)
                for i in range(pos, len(carte_rects_j1)):
                    carte_rects_j1[i][0] = i
                PlateauJ1.ligne[pos_a][pos_b] = ' '
        print(f"{self.atk1+a} PV ont été enléves de {vala.nom}")


    def attaque2(self, vala, player, player2, pos, pos_a, pos_b):
        a = self.elt_check(vala)
        vala - (self.atk2 + a)
        if self.__soincol2 == 0:
            if not self.pv + self.soin2 > self.__pvmax:
                self.pv += self.soin2
        else:
            for i in range(len(player.liste)):
                if player.liste[i].pv + self.soin2 <= player.liste[i].get_pvmax():
                    player.liste[i].pv += self.soin2
        if vala.get_pv() <= 0:
            if player2.nom == "Bot":
                player2.liste.pop(pos)
                carte_rects_j2.pop(pos)
                for i in range(pos, len(carte_rects_j2)):
                    carte_rects_j2[i][0] = i
                PlateauBOT.ligne[pos_a][pos_b] = ' '
            else :
                player2.liste.pop(pos)
                carte_rects_j1.pop(pos)
                for i in range(pos, len(carte_rects_j1)):
                    carte_rects_j1[i][0] = i
                PlateauJ1.ligne[pos_a][pos_b] = ' '
        print(f"{self.atk2+a} PV ont été enléves de {vala.nom}")


def init_pos():
    for i in range(len(Bot1.liste)):
        placed = False
        for a in range(2):
            if placed :
                break
            for b in range(5):
                if PlateauBOT.ligne[a][b] == "X" and not placed:
                    carte_rects_j2.append([i, a, b])
                    PlateauBOT.ligne[a][b]="Y"
                    placed = True
        

valamon = read_csv_to_list('assets/valamon.csv')
valamonlist = []

for i in range(len(valamon)):
    valamon[i][0] = valamon[i][0].strip('"')
    valamon[i][0] = Valamon(valamon[i][0], int(valamon[i][1]), int(valamon[i][2]), int(valamon[i][3]),
                               int(valamon[i][4]), int(valamon[i][5]), int(valamon[i][6]), int(valamon[i][7]),
                               int(valamon[i][8]), valamon[i][9], valamon[i][10], valamon[i][11], valamon[i][12])
    valamonlist.append(valamon[i][0])
    
PlateauBOT = PlateauBot(Plateau("Bot"))
PlateauJ1 = Plateau("J1")
Joueur1 = Joueur("J1")
Bot1 = Bot("Bot")
init_pos()
comp_att_j1 = 4
comp_att_j2 = 4

def start():
    print('Bienvenue sur Valamon version console.\n')
    print("Choisisez ce que vous souhaitez faire parmi les options suivantes :\n\n1.Jouer, 2.Règles, 3. Quitter")
    selc = int(input())
    if selc == 1:
        affichage_plateau()
    elif selc == 2:
        webbrowser.open('rules.papylulu.ovh')
    
def affichage_plateau():
    subprocess.run('cls', shell = True)
    print("PV Bot:", Bot1.get_pv())
    PlateauBOT.get_ligne()
    print("\n")
    PlateauJ1.get_ligne()
    print("Vos PV:", Joueur1.get_pv())
    print("\nChoisisez une action à faire :")
    selc = int(input("1.Placer des cartes\n2.Jouer une attaque\n3.Connaître une carte du plateau de l'adversaire\n4.Connaître une carte de votre plateau\n5.Retourner au menu d'acceuil\n"))
    if selc == 1:
        poser_carte()
    elif selc == 2:
        attaque_j1()
    elif selc == 3:
        carte_ad()
    elif selc == 4:
        carte_jr()
    elif selc == 5:
        subprocess.run('cls', shell = True)
        start()
        
def carte_ad():
    print("\nColonne 0 : La plus à gauche, Colonne 4 : La plus à droite")
    print("Ligne 0 : La plus loin du centre, Ligne 1 : La plus proche du centre")
    lgn = int(input("\nDonner la ligne de la carte\n"))
    col = int(input("\nDonner la colonne de la carte\n"))
    selc = []
    selc.append(lgn)
    selc.append(col)
    subprocess.run('cls', shell = True)
    compt = 0
    if carte_rects_j2 : 
        while carte_rects_j2[compt][1] != selc[0] or carte_rects_j2[compt][2] != selc[1]:
            compt = compt + 1
            if compt == 6:
                break
        if Bot1.liste[compt] and carte_rects_j2[compt][2]==col:
            print(Bot1.liste[compt])
        else:
            print("Carte inexistante.")
    else:
        print("Plateau de l'adversaire vide.")
    input("Appuyez sur Entrer pour continuer")
    affichage_plateau()
    
def carte_jr():
    print("\nColonne 0 : La plus à gauche, Colonne 4 : La plus à droite")
    print("Ligne 0 : La plus proche du centre, Ligne 1 : La plus loin du centre")
    lgn = int(input("\nDonner la ligne de la carte\n"))
    col = int(input("\nDonner la colonne de la carte\n"))
    selc = []
    selc.append(lgn)
    selc.append(col)
    subprocess.run('cls', shell = True)
    compteur = 0
    if carte_rects_j1 != []:
        while carte_rects_j1[compteur][1] != selc[0] or carte_rects_j1[compteur][2] != selc[1]:
            compteur += 1
            if compteur == 6:
                break
        if Joueur1.liste[carte_rects_j1[compteur][0]] and carte_rects_j1[compteur][2]==col:
            print(Joueur1.liste[carte_rects_j1[compteur][0]])
        else:
            print("Carte inexistante.")
    else:
        print("Votre plateau est vide.")
    input("Appuyez sur Entrer pour continuer")
    affichage_plateau()

def attaque_j1():
    global saut_tour
    global comp_att_j1
    while comp_att_j1 > 0:
        subprocess.run('cls', shell = True)
        print(f"Il vous reste {comp_att_j1} attaques à jouer avant de passer votre tour.")
        selc = int(input("Voulez-vous continuer ou passer votre tour?\n1.Passer 2.Continuer"))
        if selc == 1:
            comp_att_j1 = 0
        elif selc == 2:     
            PlateauBOT.get_ligne()
            print("\n")
            PlateauJ1.get_ligne()
            print("\nColonne 0 : La plus à gauche, Colonne 4 : La plus à droite")
            print("Ligne 0 : La plus proche du centre, Ligne 1 : La plus loin du centre")
            lgn = int(input("\nDonner la ligne de la carte\n"))
            col = int(input("\nDonner la colonne de la carte\n"))
            selc = []
            selc.append(lgn)
            selc.append(col)
            subprocess.run('cls', shell = True)
            compteur = 0
            if carte_rects_j1 != []:
                while carte_rects_j1[compteur][1] != selc[0] or carte_rects_j1[compteur][2] != selc[1]:
                    compteur += 1
                    if compteur == 6:
                        break
                if Joueur1.liste[carte_rects_j1[compteur][0]] and carte_rects_j1[compteur][2]==col:
                    print(Joueur1.liste[carte_rects_j1[compteur][0]])
                else:
                    print('Carte inexistante ou non présente sur le plateau.')
            else:
                print('Plateau vide.')
                input('Appuyez sur Entrer pour continuer')
                affichage_plateau()
            selc = int(input("Voulez-vous attaquer avec cette carte ? (Soyez-sûr, l'action n'est pas réversible)\n1.Oui 2.Non"))
            if selc == 1:
                subprocess.run('cls', shell = True)
                print(Joueur1.liste[carte_rects_j1[compteur][0]])
                selc = int(input("Quelle attaque souhaitez-vous jouer ? (1.Attaque1, 2.Attaque2)"))
                if selc == 1:
                    a = False
                    for i in range(len(carte_rects_j2)):
                        if carte_rects_j2[i][1] == 1 and carte_rects_j2[i][2] == col:
                            Joueur1.liste[carte_rects_j1[compteur][0]].attaque1(Bot1.liste[carte_rects_j2[i][0]],Joueur1,Bot1,compteur,lgn,col)
                            a = True
                            comp_att_j1 -= 1
                            break
                        elif carte_rects_j2[i][1] == 0 and carte_rects_j2[i][2] == col:
                            Joueur1.liste[carte_rects_j1[compteur][0]].attaque1(Bot1.liste[carte_rects_j2[i][0]],Joueur1,Bot1,compteur,lgn,col)
                            a = True
                            comp_att_j1 -= 1
                            break
                    if a == False:
                        Bot1.sous_pv(Joueur1.liste[carte_rects_j1[compteur][0]].atk1)
                        comp_att_j1 -= 1 
                        print(f'Le Bot à perdu {Joueur1.liste[carte_rects_j1[compteur][0]].atk1} PV est est désormais à {Bot1.get_pv()} PV.')
                        if Bot1.get_pv() <= 0:
                            Bot1.set_pv(0)
                            return win()
                    input("Appuyez sur Entrer pour continuer")                          
                else:
                    a = False
                    for i in range(len(carte_rects_j2)):
                        if carte_rects_j2[i][1] == 1 and carte_rects_j2[i][2] == col:
                            Joueur1.liste[carte_rects_j1[compteur][0]].attaque2(Bot1.liste[carte_rects_j2[i][0]],Joueur1,Bot1,compteur,lgn,col)
                            comp_att_j1 -= 1
                            a = True
                            break
                        elif carte_rects_j2[i][1] == 0 and carte_rects_j2[i][2] == col:
                            Joueur1.liste[carte_rects_j1[compteur][0]].attaque2(Bot1.liste[carte_rects_j2[i][0]],Joueur1,Bot1,compteur,lgn,col)
                            a = True
                            comp_att_j1 -= 1
                            break
                    if a == False:
                        Bot1.sous_pv(Joueur1.liste[carte_rects_j1[compteur][0]].atk2)
                        comp_att_j1 -= 1 
                        print(f'Le Bot à perdu {Joueur1.liste[carte_rects_j1[compteur][0]].atk2} PV est est désormais à {Bot1.get_pv()} PV.')
                        if Bot1.get_pv() <= 0:
                            Bot1.set_pv(0)
                            return win()
                    input("Appuyez sur Entrer pour continuer")
            else:
                attaque_j1()
    if comp_att_j1 <= 0 :
        attaquebot()
    affichage_plateau()

def attaquebot():
    ran = random.randint(0,len(Bot1.liste)-1)
    ran2 = random.randint(0,1)
    if ran2 == 0:
        a = False
        for i in range(len(carte_rects_j1)):
            if carte_rects_j1[i][1] == 0 and carte_rects_j1[i][2] == carte_rects_j2[ran][2]:
                Bot1.liste[ran].attaque1(Joueur1.liste[carte_rects_j1[i][0]],Bot1,Joueur1,ran,carte_rects_j2[ran][1],carte_rects_j2[ran][2])
                a = True
                break
            elif carte_rects_j1[i][1] == 1 and carte_rects_j2[i][2] == carte_rects_j1[i][2]:
                Bot1.liste[ran].attaque1(Joueur1.liste[carte_rects_j1[i][0]],Bot1,Joueur1,ran,carte_rects_j2[ran][1],carte_rects_j2[ran][2])
                a = True
                break
        if a == False:
            Joueur1.sous_pv(Bot1.liste[ran].atk1)
            print(f'Le Joueur à perdu {Bot1.liste[ran].atk1} PV est est désormais à {Joueur1.get_pv()} PV.')
            if Joueur1.get_pv() <= 0:
                Joueur1.set_pv(0)
                return gameover()
    else:
        a = False
        for i in range(len(carte_rects_j1)):
            if carte_rects_j1[i][1] == 0 and carte_rects_j1[i][2] == carte_rects_j2[ran][2]:
                Bot1.liste[ran].attaque2(Joueur1.liste[carte_rects_j1[i][0]],Bot1,Joueur1,ran,carte_rects_j2[ran][1],carte_rects_j2[ran][2])
                a = True
                break
            elif carte_rects_j1[i][1] == 1 and carte_rects_j2[i][2] == carte_rects_j1[i][2]:
                Bot1.liste[ran].attaque2(Joueur1.liste[carte_rects_j1[i][0]],Bot1,Joueur1,ran,carte_rects_j2[ran][1],carte_rects_j2[ran][2])
                a = True
                break
        if a == False:
            Joueur1.sous_pv(Bot1.liste[ran].atk1)
            print(f'Le Joueur à perdu {Bot1.liste[ran].atk2} PV est est désormais à {Joueur1.get_pv()} PV.')
            if Joueur1.get_pv() <= 0:
                Joueur1.set_pv(0)
                return gameover()
    global comp_att_j2
    comp_att_j2 -=1
    if comp_att_j2 <= 0:
        global comp_att_j1
        comp_att_j1 = 4
        comp_att_j2 = 4
        input("Appuyez sur Entrer pour continuer.")
    else:
        attaquebot()

def poser_carte():
    subprocess.run('cls', shell = True)
    l = []
    for i in range(len(Joueur1.liste_placement)):
        l.append(Joueur1.liste_placement[i].nom)
    print(l)
    print("La liste de ces cartes sont triés par ordre croissant de leur PV.")
    a = int(input(f"Donnez l'indice de la carte que vous souhaitez placer. (0 : La plus à gauche de la liste, {len(Joueur1.liste_placement)-1} : La plus à droite) "))
    b = a
    for i in range(len(Joueur1.liste)):
        if Joueur1.liste[i] == Joueur1.liste_placement[a]:
            b = i
            break
    selc_eplacement(b, a)
    
def selc_eplacement(a, c):
    subprocess.run('cls', shell = True)
    print(Joueur1.liste[a])
    b = int(input("1.Placer la carte, 2.Changer de carte"))
    if b == 1:
        PlateauBOT.get_ligne()
        print("\n")
        PlateauJ1.get_ligne()
        print("\nColonne 0 : La plus à gauche, Colonne 4 : La plus à droite")
        print("Ligne 0 : La plus proche du centre, Ligne 1 : La plus loin du centre")
        lgn = int(input("\nDonner la ligne de la carte\n"))
        col = int(input("\nDonner la colonne de la carte\n"))
        selc = []
        selc.append(lgn)
        selc.append(col)
        if PlateauJ1.ligne[lgn][col]!='Y':
            carte_rects_j1.append([a,lgn,col])
            print(carte_rects_j1)
            PlateauJ1.ligne[lgn][col] = 'Y'
            Joueur1.liste_placement.pop(c)
            affichage_plateau()
        elif lgn > 1 or col > 4 or lgn < 0 or col < 0 :
            print("Vous êtes en dehors du plateau.")
            selc_eplacement(a)
        else:
            print('Une carte est déjà placée ici.')
            selc_eplacement(a)
    else:
        poser_carte()


def win():
    subprocess.run('cls', shell = True)
    print("Vous avez gagné la partie. Félicitations!")
    print("Pour rejouer, relancez le script")
    input("Faites Ctrl-Z (Spider) ou Alt-F4 (Terminal) pour quitter le jeu")

    
def gameover():
    subprocess.run('cls', shell = True)
    print("Vous avez perdu la partie...")
    print("Pour rejouer, relancez le script")
    input("Faites Ctrl-Z (Spider) ou Alt-F4 (Terminal) pour quitter le jeu")

start()