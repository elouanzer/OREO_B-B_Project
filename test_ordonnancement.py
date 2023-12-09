#!/usr/bin/env python

__author__ = 'Chams Lahlou'
__date__ = 'Décembre 2022'
__version__ = '0.4'

import flowshop

# Pour tester
if __name__ == "__main__":
    j1 = flowshop.creer_job(0,[5,9,8,10,1])
    j2 = flowshop.creer_job(1,[9,3,10,1,8])
    j3 = flowshop.creer_job(2,[9,4,5,8,6])
    j4 = flowshop.creer_job(3,[4,8,8,7,2])
    l = [j1, j2, j3, j4]
    f = flowshop.creer_flowshop(l, 5)
    
    print("test date_dispo : ", flowshop.date_dispo(3, j1))
    print("test duree_latence : ", flowshop.duree_latence(2, j1, 5))
    print("test duree_jobs : ", flowshop.duree_jobs(0, l))
    ordo = flowshop.creer_ordo_vide(5)
    print("test eval : ", flowshop.eval(ordo, l))
    print("test NEH : ", flowshop.liste_NEH(f))
    print(flowshop.evaluation_separation(f))