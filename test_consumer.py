import pytest
from consumer import process_message

def test_process_message():
    # Simulation d'un message Kafka
    test_message = {
        'value': {
            'ip': 'IP1',
            'latitude': 50.0,
            'longitude': 8.0,
            'timestamp': 1609459200
        }
    }
    process_message(test_message)
    # Ajouter des assertions pour vérifier l'insertion correcte des données
