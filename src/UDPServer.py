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

try:
  # AF_INET indicates that the underlying network is using IPv4
  # SOCK_DGRAM indicates that it is a UDP socket
  server_socket = socket(AF_INET, SOCK_DGRAM)
  # bind the specified port number to the server's socket instantiated with the above line
  server_socket.bind(('', SERVER_PORT))
  print('The server has started successfully and is ready to receive messages')
except:
  print('An error occurred with the UDP socket')

while True:
  message, client_info = server_socket.recvfrom(2048)
  client_ip, client_port = client_info

  print('\nReceived incoming message from ' + client_ip + ' using port ' + str(client_port))
  command_args = message.decode().split(Constants.DELIMETER)
  
  print('Executing command...')
  return_code, data = execute_command(command_args)
  formatted_response = Constants.DELIMETER.join([ str(return_code), str(data) ])

  operation_status = 'succeeded' if return_code == Constants.SUCCESS_CODE else 'failed'
  print('Contact server operation ' + operation_status + '!!!')
  print('Sending return code to client...')
  
  server_socket.sendto(formatted_response.encode(), client_info)
