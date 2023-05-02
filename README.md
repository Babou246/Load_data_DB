# Load_data_DB

## Créer un environnement de developpement
python3 -m venv kafka-env

## Streaming Data avec Kafka
## Si vous êtes sur windows
cd kafka-[version]\bin\windows
## Lancer le serveur zookeeper
zookeeper-server-start.bat ..\..\config\zookeeeper.properties
## Lancer kafka
kafka-server-start.bat ..\..\config\servers.properties
## Ouvrir pour chaque script une fenetre pour producer ainsi que pour le consomer
python3 prod.py
python3 streaming.py
