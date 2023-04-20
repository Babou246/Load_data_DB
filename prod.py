"""
Top Traffic Simulator
"""
from time import sleep, time, ctime
from random import random, randint, choice
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

TOPIC = 'babacar'

VEHICLE_TYPES = ("Oigno","Tomate","Sel","Kéthiax","Arachide","Sucre")
PAYS = ('SENEGAL','NIGERA','GUINNEE','GHANA','UGANDA','MAROC','BRESIL','FRANCE')
for _ in range(100000):
    ben = randint(10000, 800000)
    pro_type = choice(VEHICLE_TYPES)
    pays = choice(PAYS)
    now = ctime(time())
    pr_un = randint(400, 3010)
    q = randint(4, 30)
    message = f"{now},{ben},{pays},{pr_un},{pro_type},{q}"
    message = bytearray(message.encode("utf-8"))
    print(f"A {pro_type} has passed by the toll plaza {pro_type} at {now}.")
    producer.send(TOPIC, message)
    sleep(random() * 2)