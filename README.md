# dockermeteoWPython

## Code Python
1. D'abord, j'ai créé un fichier Python "meteo.py" où je testais le fonctionnement de l'API en local, avec des variables locales. J'ai choisi Python parce que c'est un langage qu'on utilise très souvent en cours.
2. Ensuite j'ai adapté le code pour que celui-ci prenne en compte les variables d'environnement et non les variables locales que j'avais utilisées pour tester mon code au départ.

## Configuration de l'image
1. D'abord, j'ai créé le Dockerfile et y ai configuré mon image. Pour ce faire, j'ai d'abord fait des recherches sur internet. Au début j'ai eu un problème avec la commande **CMD** parce que je ne comprenais pas bien les arguments à y mettre mais ensuite j'ai demandé à un ami en classe et celui-ci m'expliqua que je devais y ajouter mot à mot la commande que j'aurais mise dans le terminal pour lancer mon programme (sur le fichier .py), ce que j'ai fait.
2. Ensuite j'ai dû construire mon docker. Malheureusement la commande de build ne fonctionnait pas au début mais après y avoir mis le ".", tout à fonctionné pour le mieux. J'avais donc la commande ```sh docker build . -t python-docker ```.
4. Après, j'ai testé mon docker avec la commande ```sh docker run --env LAT="5.9" --env LONG="102.7" --env API_KEY="240aa650f4db4e154a07d0459c30a347" python-docker``` et j'avais le resultat escompté alors je me suis donc consacré à la partie bonus.

## Partie bonus
1. J'ai d'abord essayé hidolint. J'ai saisi la commande ```sh docker run --rm -i hadolint/hadolint < Dockerfile```. J'ai eu un ensemble de warnings parmi lesquels:
  * L'utilisation de la dernière version de l'image Python : je devais préciser une version qui ne soit pas celle là.
  * L'absence de version sur l'installation de la librairie "requests". J'ai eu des difficultés lorsque je voulais reconstruire mon projet. D'alleurs je vous ai fait appel et il s'est trouvé que le problème venait du fait de la présence d'espaces sur la ligne.
  *  Aussi je devais ajouter le --no-cache pour eviter le téléchargement de fichiers inutiles.
  *  Enfin, je devais utiliser "**COPY**" à la place de "**ADD**".
2. Enfin, J'ai essayé d'utiliser Trivy. Au départ je n'ai pas reussi à utiliser la commande ```sh trivy image python-docker```. J'ai alors regardé sur internet et j'ai trouvé une commade qui me permettait de télécharger l'image de trivy et l'utiliser.```sh curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.16.0```. Ensuite j'ai pu l'utiliser et remarquer les CVE. Malheureusement je n'ai pas pu les enlever car je ne pouvais pas filtrer sur docker hub les images afin d'obtenir celles avec le moins de vulnérabilités (/plus légères). Même en regardant sur internet. Et les images reconnues officiellement que j'ai testées en avaient toujours beaucoup.
