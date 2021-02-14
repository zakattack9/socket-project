from socket import *
from utils import Constants
from server.CommandExecutor import execute_command
from utils.Socket import create_socket, validate_port
import argparse

parser = argparse.ArgumentParser(description='IDP server socket process')
parser.add_argument(
  'port_number',
  type=int,
  help='Port number that the server will listen on'
)

args = parser.parse_args()

# store the passed in port # for the server to listen on
SERVER_PORT = validate_port(args.port_number)

def print_command_args(cmd_args):
  client_command = '$ '
  for arg in cmd_args:
    client_command += str(arg) + ' '
  print(client_command)

try:
  server_socket = create_socket(SERVER_PORT)
  print('The server has started successfully and is ready to receive messages')
  
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
except Exception as err:
  print('[ERROR]: Occurred with the UDP socket\n' + str(err))
