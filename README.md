# dockermeteoWPython

- D'abord, j'ai créé un fichier Python "meteo.py" où je testais le fonctionnement de l'API en local, avec des variables locales. J'ai choisi Python parce que c'est un langage qu'on utilise très souvent en cours.
- Ensuite j'ai adapté le code pour que celui-ci prenne en compte les variables d'environnement et non les variables locales que j'avais utilisées pour tester mon code au départ.
- Après j'ai crée le Dockerfile et y ai configuré mon image. Pour se faire, j'ai d'abord fait des recherches sur internet. Au début j'ai eu un problème avec la commande CMD parce que j ene comprenais pas bien les arguments à y mettre mais ensuite j'ai demandé à un ami en classe et celui-ci m'expliqua que je devais y ajouter la mot à mot la commande que j'aurais mise dans le terminal pour lancer mon programme (sur le fichier .py), ce que j'ai fait. Ensuit ej'ai essayé de build
- Après j'ai dû construire mon docker. Malheureusement la commande de build ne fonctionnait pas au début mais après y avoir mis le ".", tout à fonctionné pour le mieux;
- Après j'ai testé mon docker avec la commande "run" et j'avais le resultat escompté alors je me suis donc consacré à la partie bonus.
- J'ai d'abord essayé hidolint. J'ai saisi la commande 
```sh
docker run --rm -i hadolint/hadolint < Dockerfile 

- Enfin, J'ai utilisé hidolint pour que le fichier soit sans bavures
