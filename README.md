# Laboratoire 1 - 8-Puzzle 

## Résumé de ce qu'on a appris

Ce labo nous a permis de vraiment voir la différence entre les algorithmes de recherche de largeur (BFS), profondeur (DFS) et approfondissement, pas juste
en théorie mais en pratique sur un problème concret. On a remarqué rapidement que le choix de l,algorithmes peut réellement influencer la solution du puzzle.

On a aussi appris (à nos dépens) un piège classique : si on limite la profondeur
d'un DFS tout en gardant un ensemble global d'états déjà visités, l'algorithme
peut devenir incomplet. Un état découvert une première fois via un chemin très
long bloque toute réexploration de ce même état via un chemin plus court, même
si ce chemin plus court aurait permis de trouver une solution dans la limite
donnée. Dans un de nos tests, ça faisait carrément dire au DFS qu'il n'y avait
pas de solution alors qu'il y en avait une. La solution la plus simple a été de
ne pas mettre de limite de profondeur du tout sur le DFS "de base" (question 2),
et de garder ça pour l'approfondissement itératif (question 3).

On a aussi mieux compris ce qu'est la "frontière" concrètement : ce n'est pas
juste un concept abstrait, c'est littéralement la structure de données (une
file pour BFS, une pile pour DFS) qui contient les états découverts mais pas
encore explorés. Le fait de logger sa taille à chaque itération donne une bonne
idée de la consommation mémoire réelle de chaque algorithme pendant l'exécution.

## Comparaison des algorithmes

### Performance / qualité de la solution

BFS trouve toujours le chemin le plus court, garanti. Sur nos tests, il
trouvait des solutions optimales (ex. 31 coups sur un cas volontairement
difficile) en explorant un nombre d'états raisonnable, mais sa frontière
grossissait vite parce qu'il garde en mémoire tout un "niveau" de l'arbre
avant de passer au suivant.

DFS, de son côté, trouve toujours *une* solution (parce que l'espace d'états
du 8-puzzle est fini et qu'on empêche les boucles avec un ensemble de visités),
mais rien ne le pousse vers le but. Sur le même genre de cas, on a eu des
chemins de solution de plusieurs dizaines de milliers de mouvements (39 478
dans un de nos tests) alors que la solution optimale ne faisait que quelques
coups. Ça semble étrange au premier abord, mais ça s'explique : DFS explore
une direction à fond avant de reculer, et comme les mouvements du puzzle sont
réversibles, il peut zigzaguer à travers une bonne partie des ~180 000 états
possibles avant de tomber sur le but par hasard. Le nombre total d'états
explorés (`total_explored`) et la longueur du chemin trouvé sont deux mesures
complètement différentes.

Niveau mémoire, DFS garde une frontière beaucoup plus petite en moyenne (une
seule branche active à la fois), même s'il finit souvent par visiter beaucoup
plus d'états au total que BFS pour le même problème.

### Facilité d'implémentation

Les deux algorithmes se ressemblent énormément dans le code : la seule vraie
différence structurelle est le type de structure de données utilisée pour la
frontière (`deque` en FIFO pour BFS, simple liste en LIFO pour DFS). Le reste
(génération des successeurs, détection des doublons, logging des stats) est
presque identique.

Ce qui est plus subtil à implémenter correctement, c'est la gestion des
doublons combinée à une éventuelle limite de profondeur — comme on l'a vu,
c'est facile de se planter là-dessus sans s'en rendre compte, parce que le code
"a l'air" de fonctionner sur des cas simples et ne révèle le bug que sur des
cas plus difficiles.

### Autres critères

- **Prévisibilité** : BFS est très prévisible (toujours le chemin optimal,
  toujours le même comportement peu importe l'ordre des mouvements testés).
  DFS est très sensible à l'ordre dans lequel on essaie les mouvements
  (HAUT/BAS/GAUCHE/DROITE) — changer cet ordre peut complètement changer
  la longueur de la solution trouvée et le temps d'exécution.
- **Utilité pratique** : pour un problème de plus court chemin comme le
  8-puzzle, BFS est clairement le bon choix. DFS serait plus approprié pour
  des problèmes où on veut juste savoir si *une* solution existe, sans se
  soucier de sa qualité (ex. vérifier qu'un graphe est connexe).
- **Reproductibilité entre les 10 exécutions** : comme les deux algorithmes
  sont déterministes (pas de hasard dans le code), les 10 exécutions sur le
  même fichier donnent des résultats identiques (même nombre d'états
  explorés, même temps à quelques millisecondes près dû aux variations
  système).
