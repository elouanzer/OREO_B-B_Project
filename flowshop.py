#!/usr/bin/env python

__author__ = 'Chams Lahlou'
__date__ = 'Octobre 2019 - novembre 2023'
__version__ = '0.5'

"""Résolution du flowshop de permutation : 

 - par l'algorithme NEH
 - par évaluation et séparation
 """

# La résolution par évaluation et séparation utilise une file de priorité pour 
# stocker et trier les sommets. Python propose le module 'heapq' :
import heapq

# On utilise deux fonctions du module 'heapq' :
#
# La fonction 'heappop' permet de récupérér le sommet de plus petite valeur. Par
# exemple : sommet = heapq.heappop(file_priorite)
#
# La fonction 'heappush' permet d'ajouter un nouveau sommet. Par exemple : 
# heapq.heappush(file_priorite, sommet)

# La structure de données des sommets est définie dans un module :
import sommet

# valeur (arbitraire) maximale d'un entier
MAXINT = 100000

'''
Fonctions pour un job
'''

def creer_job(numero_job, duree_op):
    ''' - numero_job = numéro du job
        - duree_op = liste des durées des opérations du job
        - début = liste des date de début des opérations du job
    '''

    return {'numéro':numero_job, 
            'durée':duree_op,
            'début':[None for i in duree_op]}

def afficher_job(job):
    print("Job n°", job['numéro'], 
            "de durée totale", sum(job['durée']), ":")
    
    nb_op = len(job['durée'])
    for numero in range(nb_op):
        print("  opération n°", numero, ": durée =", job['durée'][numero],
                "démarre à", job['début'][numero])

'''
Fonctions pour un ordonnancement
'''

def creer_ordo_vide(nb_mach):
    ''' renvoie un ordonnancement avec 'nb_mach' machines vides.

        - séquence = la liste des jobs ordonnancés.
        - disponibilité = la liste des dates de fin de l'ordonnancement pour 
          chaque machine.
    '''

    date_dispo = [0 for i in range(nb_mach)]
    return {'séquence':[], 'disponibilité':date_dispo}


def afficher_ordo(ordo):
    print("Ordre des jobs :", end='')
    for job in ordo['séquence']:
        print(" ", job['numéro']," ", end='')

    print()

    nb_machines = len(ordo['disponibilité'])
    for job in ordo['séquence']:
        print("Job", job['numéro'], ":", end='')

        
        for machine in range(nb_machines):
            print(" op", machine, 
                  "à t =", job['début'][machine],
                  "|", end='')

        print()
        
    print("Cmax =", ordo['disponibilité'][nb_machines-1])

################################################################################
# exo 1 :
################################################################################
def ordonnancer_job(ordo, job):
    ''' Ajoute le job 'job' à l'ordonnancemement 'ordo' à la suite des jobs
        déjà placés.
    '''

    seq = ordo['séquence']
    seq.append(job)
    dispo = ordo['disponibilité']

    job['début'][0] = dispo[0]
    dispo[0] += job['durée'][0]

    for i in range(1, len(dispo)) :
        job['début'][i] = max(dispo[i], dispo[i-1])
        dispo[i] = job['début'][i] + job['durée'][i]

    


################################################################################
# exo 2 :
################################################################################
def ordonnancer_liste_jobs(ordo, liste_jobs):
    ''' Ajoute les jobs de la liste 'liste_jobs' à l'ordonnancemement 'ordo'
        à la suite des jobs déjà placés.
    '''
    for job in liste_jobs :
        ordonnancer_job(ordo, job)


'''
Fonctions pour un flowshop
'''

def creer_flowshop(liste_jobs=[], nb_machines=0):
    ''' - liste jobs = liste des jobs du problème
        - nombre machines : nombre de machines du problème
    '''

    return {'liste jobs':liste_jobs,
            'nombre machines':nb_machines
            }

def lire_flowshop(nom_fichier):
    """ crée un problème de flowshop à partir d'un fichier """

    # ouverture du fichier en mode lecture
    flowshop = creer_flowshop()

    fdonnees = open(nom_fichier,"r")
    # lecture de la première ligne
    ligne = fdonnees.readline() 
    l = ligne.split() # on récupère les valeurs dans une liste
    nb_jobs = int(l[0])

    nb_machines = int(l[1])
    flowshop['nombre machines'] = nb_machines
    
    flowshop['liste jobs'] = []
    # création des jobs
    for num in range(nb_jobs):
        ligne = fdonnees.readline() 
        l = ligne.split()
        # on transforme la suite de chaînes de caractères représentant
        # les durées des opérations en une liste d'entiers
        l_op = [int(d_op) for d_op in l]
        # puis on crée le job
        job = creer_job(num, l_op)
        flowshop['liste jobs'].append(job)
    # fermeture du fichier
    fdonnees.close()
    return flowshop
        
  
################################################################################
# exo 3 :
################################################################################
def liste_NEH(flow_shop):
    ''' Renvoie la liste obtenue par l'algorithme NEH pour le problème défini
        par 'flow_shop'.
    '''
    seq_NEH = [] # liste dans l'ordre NEH

    pass # remplacer cette ligne

    return seq_NEH


'''
Fonctions pour la résolution par évaluation et séparation
'''

################################################################################
# exo 4 :
################################################################################
def date_dispo(machine, job):
    ''' Renvoie la valeur de r_kj avec k = 'machine' et j = 'job
    '''

    pass # remplacer cette ligne


# calcul de q_kj
def duree_latence(machine, job, nombre_machines):
    ''' Renvoie la valeur de q_kj avec k = 'machine' et j = 'job
    '''

    pass # remplacer cette ligne


# calcul de la somme des durées des opérations d'une liste
# exécutées sur une machine donnée
def duree_jobs(machine, liste_jobs):
    ''' Renvoie la somme des durées des opérations sur 'machine' des jobs de 
        'liste_jobs'
    '''

    pass # remplacer cette ligne


################################################################################
# exo 5 :
################################################################################
def eval(ordo, liste_jobs):
    ''' Renvoie la valeur du minorant en tenant compte de l'ordonnancement 
        'ordo' et des jobs non places de liste_jobs
    '''

    LB_machine = [] # liste des valeurs LB_k (pour 1 <= k <= m)

    pass # remplacer cette ligne

    return max(LB_machine)

def creer_sommet(evaluation, places, non_places, numero):
    # liste des jobs déjà placés
    return  (evaluation,
            numero,
            places,
            non_places,
            )

################################################################################
# exo 6 :
################################################################################
def evaluation_separation(flowshop):
    ''' Résout par évaluation et séparation le problème défini par 
        'flowshop'
    '''

    # calcul d'une borne supérieure initiale par l'algo NEH
    l_NEH = liste_NEH(flowshop)
    ordo = creer_ordo_vide(flowshop['nombre machines'])
    ordonnancer_liste_jobs(ordo, l_NEH)
    val_solution = ordo['durée']
    print("Valeur solution de départ =", val_solution)
    liste_solution = [job for job in l_NEH]

    arbre = []  # utilisé sous forme de file de priorité avec heapq

    # création de la racine
    ordo = creer_ordo_vide(flowshop['nombre machines'])
    evaluation = eval(ordo, l_NEH)

    # création du premier sommet
    numero = 1
    s = creer_sommet(evaluation, [], l_NEH, numero)
    # qui est ajouté à la file de priorité
    heapq.heappush(arbre, s)

    while arbre != []:
        pass # remplacer cette ligne


    return val_solution, liste_solution, numero
