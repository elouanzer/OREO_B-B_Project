import flowshop

# Pour tester
if __name__ == "__main__":

    # JEU 2 
    print("\n")
    print("JEU 2 : ")
    f2 = flowshop.lire_flowshop("jeu2-704.txt")
    NEH2 = flowshop.liste_NEH(f2)
    
    print("Ordonnancement NEH : ")
    for job in NEH2 : 
        print(job['numéro'], ' ', end='')
    v2, l2, n2 = flowshop.evaluation_separation(f2)
    print("\n")
    print("Ordonnancement optimal : ")
    for job in l2 : 
        print(job['numéro'], ' ', end='')
    print("Durée totale = ", v2)
    print(n2, "sommets parcourus")

    # JEU 3 
    print("\n")
    print("JEU 3 : ")
    f3 = flowshop.lire_flowshop("jeu3-973.txt")
    
    print("Ordonnancement NEH : ")
    NEH3 = flowshop.liste_NEH(f3)
    for job in NEH3 : 
        print(job['numéro'], ' ', end='')
    v3, l3, n3 = flowshop.evaluation_separation(f3)
    print("\n")
    print("Ordonnancement optimal : ")
    for job in l3 : 
        print(job['numéro'], ' ', end='')
    print("Durée totale = ", v3)
    print(n3, "sommets parcourus")

    # JEU 4
    print("\n")
    print("JEU 4 : ")
    f4 = flowshop.lire_flowshop("jeu4-844.txt")
    
    print("Ordonnancement NEH : ")
    NEH4 = flowshop.liste_NEH(f4)
    for job in NEH4 : 
        print(job['numéro'], ' ', end='')
    v4, l4, n4 = flowshop.evaluation_separation(f4)
    print("\n")
    print("Ordonnancement optimal : ")
    for job in l4 : 
        print(job['numéro'], ' ', end='')
    print("Durée totale = ", v4)
    print(n4, "sommets parcourus")

    