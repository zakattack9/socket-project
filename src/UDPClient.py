from socket import *
from client.CommandParser import parse_server_command
from client.CommandFormatter import format_server_command
from utils import Constants
import argparse

parser = argparse.ArgumentParser(description='UDP client socket process')
parser.add_argument(
  'server_ip',
  help='IPv4 address of UDP socket server'
)
parser.add_argument(
  'server_port',
  help='Listnening port number of UDP socket server'
)

args = parser.parse_args()
# print(args)

# store the passed in server IP and port # into variables
SERVER_IP = args.server_ip
SERVER_PORT = int(args.server_port)

def get_server_command():
  server_cmd_args = None
  while(server_cmd_args == None):
    server_command = input('$ ')
    server_cmd_args = parse_server_command(server_command)
  return server_cmd_args

def get_formatted_command(server_cmd_args):
  formatted_command = None
  while(formatted_command == None):
    formatted_command = format_server_command(server_cmd_args)
    if (formatted_command == None):
      server_cmd_args = get_server_command()
  return formatted_command

try:
  # AF_INET indicates that the underlying network is using IPv4
  # SOCK_DGRAM indicates that it is a UDP socket
  client_socket = socket(AF_INET, SOCK_DGRAM)

  while True:
    server_cmd_args = get_server_command()
    formatted_server_cmd = get_formatted_command(server_cmd_args)
    # print(formatted_server_cmd)

    client_socket.sendto(formatted_server_cmd.encode(), (SERVER_IP, SERVER_PORT))
    server_message, server_info = client_socket.recvfrom(2048)

    return_code, data = server_message.decode().split(Constants.DELIMETER)
    isSuccess = int(return_code) == Constants.SUCCESS_CODE
    
    if (isSuccess):
      print('Command executed successfully!!!')
    else:
      print('An error occurred on the server side')

    # print any data sent back from the server
    if (isSuccess and not data == 'None'): print('\n' + data)
    
    if (isSuccess and server_cmd_args.action == 'exit'):
      print('Terminating session and client server...')
      client_socket.close()
      break
except:
  print('An error occurred with the UDP socket')
