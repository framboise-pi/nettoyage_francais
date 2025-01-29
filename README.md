# Nettoyage Français Francais
Cleans our strings with a frenchy class.

## Processing
It modifies the special french caracters like é,ê,ô,ç,... or any caracter added in the script.
<br>And it removes the unwanted. Clear and simple to use.
<br>Easy to edit

## Thoughts
Je n'ai pas approfondi le sujet, il me semble que les librairies qui corrigent les caractères spéciaux ne réagissent pas comme nous l'attendons en général,
c'était l'occasion d'écrire une class utile pour les projets personnels.

# Example usage
```
from nettoyage_francais import NettoyageFrancais

# Nettoyage du titre à la française
nettoyeur = NettoyageFrancais(string)
string_propre = nettoyeur.nettoyer()
```
