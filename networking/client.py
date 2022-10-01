import logging
import socket
import time

class Client:
  def __init__(self, port_number:int) -> None:
    self.port_number = port_number
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.connected = False

  def connect(self):
    while (not self.connected):
      address = ('localhost', self.port_number)     # family is deduced to be 'AF_INET'      
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
        self.socket.connect(address)
        self.connected = True
      except ConnectionRefusedError:
        logging.info("Connect to engine failed...")
        time.sleep(1)

  def read(self) -> str:
    message = self.socket.recv(2048)
    logging.debug("Received message " + message.decode())
    return message.decode()

  def write(self, message:str) -> None:
    logging.debug("Sending message \"" + message + "\"")
    self.socket.sendall(str.encode(message + "\n"))

  def disconnect(self):
    self.socket.close()
    self.connected = False