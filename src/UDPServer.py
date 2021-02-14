from socket import *
from utils import Constants
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

def print_command_args(cmd_args):
  client_command = '$ '
  for arg in cmd_args:
    client_command += str(arg) + ' '
  print(client_command)

try:
  # AF_INET indicates that the underlying network is using IPv4
  # SOCK_DGRAM indicates that it is a UDP socket
  server_socket = socket(AF_INET, SOCK_DGRAM)
  # bind the specified port number to the server's socket instantiated with the above line
  server_socket.bind(('', SERVER_PORT))
  print('The server has started successfully and is ready to receive messages')
except:
  print('\nAn error occurred with the UDP socket')

while True:
  client_message, client_info = server_socket.recvfrom(2048)
  client_ip, client_port = client_info
  client = client_ip + ' : ' + str(client_port)

  print('\nNew message from ' + client)
  command_args = client_message.decode().split(Constants.DELIMETER)
  print_command_args(command_args)
  
  return_code, data = execute_command(command_args)
  formatted_response = Constants.DELIMETER.join([ str(return_code), str(data) ])

  if (not return_code == Constants.SUCCESS_CODE):
    print(Constants.failure_code_message(return_code))
  else:
    print('Operation succeeded!!!')
  
  server_socket.sendto(formatted_response.encode(), client_info)
  print('Response sent back to ' + client)
