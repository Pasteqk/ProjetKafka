from confluent_kafka import Producer
from global_land_mask import globe
import json
import time
import random
import numpy as np
import os
import logging


ip = os.environ.get("ip")
logging.basicConfig(level=logging.INFO)

# Fonction de rappel pour les livraisons de données
def delivery_report(err, data):
    if err is not None:
        logging.error(f'Échec de la livraison des données : {err}')
    else:
        logging.info(f'Données livré à {data.topic()} [{data.partition()}]')

def wait_for_availability(function_that_fails, number_of_tries, time_between_tries):
  for _ in range(number_of_tries):
    try:
      res = function_that_fails()
      return res
    except:
      time.sleep(time_between_tries)
  raise TimeoutError(f'{function_that_fails.__name__} did not answer.')

# Configuration du producteur Kafka
logging.info("Creation of the producer")
producer = wait_for_availability(
    lambda:Producer({'bootstrap.servers': "kafka-broker:9092"}),
    number_of_tries = 10,
    time_between_tries = 2
)
logging.info("Producer created")
# Coordonnées de Paris "Lieu de démarrage"
latitude = 48.87
longitude = 2.33 
def send_gps_data(ip):
    """
    Envoie des données GPS simulées au topic Kafka.
    """
    # Création de données GPS aléatoires
    logging.info("Sending data ")
    data = {
        'ip': ip,
        'latitude': latitude + (random.randrange(-10,10)/500),
        'longitude':  longitude + (random.randrange(-10,10)/500),
        'timestamp': time.time()
    }
    while globe.is_ocean(data["latitude"],data["longitude"]):
        data = {
            'ip': ip,
            'latitude': latitude + (random.randrange(-10,10)/500),
            'longitude': longitude + (random.randrange(-10,10)/500),
            'timestamp': time.time()
        }
        logging.info(f'Sending data: {data}')
    # Envoi des données au topic 'coordinates'
    producer.produce('coordinates', value=json.dumps(data), callback=delivery_report)
    producer.poll(0)

# Boucle pour envoyer des données GPS de manière continue
while True:
    logging.info(f'Topics available: {producer.list_topics()}')
    send_gps_data(ip)
    time.sleep(3)  # Pause de 3 secondes entre les envois