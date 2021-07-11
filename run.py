from typing import Tuple
from pysocketchat import create_app


connection = create_app()

while True:
    connectedsocket, address = connection.accept()
    print("Connection from {address} established".format(address = address))