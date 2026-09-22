# Laboratoire 1 - 8-Puzzle 

## Résumé de ce qu'on a appris

Ce labo nous a permis de vraiment voir la différence entre les algorithmes de recherche de largeur (BFS), profondeur (DFS) et approfondissement, pas juste en théorie mais en pratique sur un problème concret. On a remarqué rapidement que le choix de l'algorithmes peut réellement influencer la solution du puzzle. Le choix influence directement le temps d'xécution, la taille de la frontière ainsi que la longueur de la solution trouvé.

On a appris, après essai et erreur, que l'algorithme de profondeur était vraiment pas bien adapté pour résoudre la problématique du 8-puzzle. Puisqu'on traverse les noeuds de l'arbre au plus profond avant de remonter, la solution découverte par l'algorithme sera probablement non optimale. Il n'y a donc aucune garantie que la première solution trouvée soit la plus courte. À l'inverse, l'algorithme de largeur et d'approfondissement, en pratique, résultait un chemin optimale. Pour l'appronfissement, en faisant la recherche de profondeur par couche on assure également d'avoir une solution optimale.

On a aussi mieux compris ce qu'est la "frontière" concrètement : ce n'est pas juste un concept abstrait, c'est littéralement la structure de données (une file pour BFS, une pile pour DFS et approfondissement) qui contient les états découverts mais pas encore explorés. Le fait de logger sa taille à chaque itération donne une bonne idée de la consommation mémoire réelle de chaque algorithme pendant l'exécution.

## Comparaison des algorithmes

### Performance / qualité de la solution

BFS trouve toujours le chemin le plus court, garanti. Sur nos tests, il trouvait des solutions optimales en explorant un nombre d'états raisonnable. Dans notre code, les états sont ajoutés dans une file où le premier état ajouté est toujours le premier exploré (Principe de FIFO). L'inconvénient qu'on a observé est la consommation de mémoire de l'algorithme, qu'on voit dans les fichiers output logs. 

DFS, de son côté, utilise une pile (Principe de LIFO). Ici, on trouve toujours une solution, mais rien n'assure qu'elle est optimale. Dans nos tests, on a remarqué que DFS produisait des chemins considérablememtn plus long. Les principes théorique de la recherche en profondeur appuis nos résultats pratique puisque le chemin pris dans une branche peut très bien nous éloigner rapidement de la solution optimale. 

La recherche par approfondissement effectue des recherches en profondeurs comme DFS mais cette fois si on y va par couches donc avant d'aller plus loins on vérifie tous les noeuds du même étage et ainsi de suite. En augmentant progressivement les couches, on assure de trouver le chemin optimal. On concerve une consommation de mémoire relativement faible comme on à pu voir dans nos fichier logs.

### Facilité d'implémentation
On a eu de la facilité à implémenter l'algorithme de recherche en largeur mais on a eu plus de difficulté lorsqu'on est arrivé à l'algo de profondeur. Une fois qu'on a compris les deux cependant, l'algorithmes d'appronfondissement, qui est techniquement plus complexe, à été relativement facile puisqu'il combine les principes du BFS et DFS. En ajoutant le principe de depth limited search, on peut effectuer la recherche en profondeur progressivement.

### Autres critères

