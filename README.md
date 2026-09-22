# Laboratoire 1 - 8-Puzzle 

## Résumé de ce qu'on a appris

Ce labo nous a permis de vraiment voir la différence entre les algorithmes de recherche de largeur (BFS), profondeur (DFS) et approfondissement, pas juste
en théorie mais en pratique sur un problème concret. On a remarqué rapidement que le choix de l,algorithmes peut réellement influencer la solution du puzzle.

On a appris, après essai et erreur, que l'algorithme de profondeur était vraiment pas bien adapté pour résoudre la problématique du 8-puzzle. Puisqu'on traverse les noeuds de l'arbre au plus profond avant de remonter, la solution découverte par l'algorithme sera probablement non optimale. À l'inverse, l'algorithme de largeur et d'approfondissement, en pratique, résultait un chemin optimale. 

On a aussi mieux compris ce qu'est la "frontière" concrètement : ce n'est pas juste un concept abstrait, c'est littéralement la structure de données (une file pour BFS, une pile pour DFS) qui contient les états découverts mais pas encore explorés. Le fait de logger sa taille à chaque itération donne une bonne idée de la consommation mémoire réelle de chaque algorithme pendant l'exécution.

## Comparaison des algorithmes

### Performance / qualité de la solution

BFS trouve toujours le chemin le plus court, garanti. Sur nos tests, il trouvait des solutions optimales en explorant un nombre d'états raisonnable. DFS, de son côté, trouve toujours une solution, mais rien ne le pousse vers le but. Sur le même genre de cas, on a eu des chemins de solution extrêmement grand alors que la solution optimale ne faisait que quelques coups. Ça semble étrange au premier abord, mais ça s'explique : DFS explore
une direction à fond avant de reculer, la rendant non optimale.

### Facilité d'implémentation


### Autres critères

