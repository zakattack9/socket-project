from socket import *
from utils.ServerCommandParser import parse_server_command
from utils.ServerCommandFormatter import format_server_command
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

  server_cmd_args = get_server_command()
  formatted_server_cmd = get_formatted_command(server_cmd_args)

  print(formatted_server_cmd)

  # client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
  # modified_message, server_address = client_socket.recvfrom(2048)

  # print(modified_message.decode())
except error:
  print('An error occurred with the UDP socket: ' + error)

# closes the client socket and terminates its process
client_socket.close()
