from socket import *
from client.CommandParser import parse_server_command
from client.CommandFormatter import format_server_command
from utils import Constants
from utils.Socket import create_pair_socket, validate_port
import argparse
import json
import threading

parser = argparse.ArgumentParser(description='UDP client socket process')
parser.add_argument(
  'server_ip',
  help='IPv4 address of UDP socket server'
)
parser.add_argument(
  'server_port',
  type=int,
  help='Listening port number of UDP socket server'
)

args = parser.parse_args()

# store the passed in server IP and port # into variables
SERVER_IP = args.server_ip
SERVER_PORT = validate_port(args.server_port)

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

def udp_server_thread(client_socket):
  while True:
    server_cmd_args = get_server_command()
    formatted_server_cmd = get_formatted_command(server_cmd_args)

    client_socket.sendto(formatted_server_cmd.encode(), (SERVER_IP, SERVER_PORT))
    server_message, server_info = client_socket.recvfrom(2048)
    print("UDP_SERVER")

    return_code, data = server_message.decode().split(Constants.DELIMITER)
    isSuccess = int(return_code) == Constants.SUCCESS_CODE
    
    if (not isSuccess):
      print(Constants.failure_code_message(return_code))

    # parse the data sent back from the server
    parsed_data = json.loads(data)
    if (isSuccess and not parsed_data == None): print(data)
    
    if (isSuccess and server_cmd_args.action == 'exit'):
      print('Terminating session and client server...')
      client_socket.close()
      break

def p2p_im_thread(p2p_socket):
  while True:
    server_message, server_info = p2p_socket.recvfrom(2048)
    print(server_info)

try:
  client_socket, p2p_socket = create_pair_socket(SERVER_PORT)
  
  udp_server = threading.Thread(target = udp_server_thread, args=[client_socket])
  p2p_im = threading.Thread(target = p2p_im_thread, args=[p2p_socket])
  
  udp_server.start()
  p2p_im.start()

except Exception as err:
  print('[ERROR]: Occurred with the UDP socket\n' + str(err))
