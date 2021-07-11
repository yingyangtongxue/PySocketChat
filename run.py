from typing import Tuple
from server import create_server


server = create_server()

while True:
    connectedsocket, address = server.accept()
    print("server from {address} established".format(address = address))