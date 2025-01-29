# nettoyage_francais
Clean strings with a frenchy class. Modify the special caracters like é,ê,ô,ç,.... and remove the unwanted. Clear and simple to use.
Je n'ai pas approfondi le sujet, il me semble que les librairies qui corrigent les caractères spéciaux ne réagissent pas comme nous l'attendons en général,
c'était l'occasion d'écrire une class utile pour les projets personnels.

from nettoyage_francais import NettoyageFrancais

# Nettoyage du titre à la française
nettoyeur = NettoyageFrancais(string)
string_propre = nettoyeur.nettoyer()
