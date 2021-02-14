from socket import *
from utils import Constants
from models import ContactDatabase
from server.CommandExecutor import execute_command
import argparse

parser = argparse.ArgumentParser(description='IDP server socket process')
parser.add_argument(
  'port_number',
  help='Port number that the server will listen on'
)

args = parser.parse_args()
# print(args)

# store the passed in port # for the server to listen on
SERVER_PORT = int(args.port_number)

try:
  # AF_INET indicates that the underlying network is using IPv4
  # SOCK_DGRAM indicates that it is a UDP socket
  server_socket = socket(AF_INET, SOCK_DGRAM)
  # bind the specified port number to the server's socket instantiated with the above line
  server_socket.bind(('', SERVER_PORT))
  print('The server has start successfully and is ready to receive messages')
except:
  print('An error occurred with the UDP socket')

while True:
  # instantiate new database instance
  ContactDatabase = ContactDatabase()
  message, client_address = server_socket.recvfrom(2048)

  print('Received incoming message from ' + client_address)
  command_args = message.decode().split(Constants.DELIMETER)
  print('Executing command...')
  return_code = execute_command(command_args, ContactDatabase)

  print('Contact server operation ' + 'succeeded' if return_code == Constants.SUCCESS_CODE else 'failed' + '!!!')
  print('Sending return code to client...')
  
  server_socket.sendto(return_code.encode(), client_address)
