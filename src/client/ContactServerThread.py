from socket import *
from client.CommandParser import parse_server_command
from client.CommandFormatter import format_server_command
from client.CommandSuccess import successful_command
from utils import Constants
import threading
import argparse
import json

class Contact_Server_Thread(threading.Thread):
  def __init__(self, client_socket, server_ip, server_port):
    threading.Thread.__init__(self)
    self.client_socket = client_socket
    self.server_ip = server_ip
    self.server_port = server_port
  
  def get_server_command(self):
    server_cmd_args = None
    while(server_cmd_args == None):
      server_command = input('$ ')
      server_cmd_args = parse_server_command(server_command)
    return server_cmd_args

  def get_formatted_command(self, server_cmd_args):
    formatted_command = None
    while(formatted_command == None):
      formatted_command = format_server_command(server_cmd_args)
      if (formatted_command == None):
        server_cmd_args = self.get_server_command()
    return formatted_command

  def run(self):
    while True:
      try:
        server_cmd_args = self.get_server_command()
        formatted_server_cmd = self.get_formatted_command(server_cmd_args)

        self.client_socket.sendto(formatted_server_cmd.encode(), (self.server_ip, self.server_port))
        server_message, server_info = self.client_socket.recvfrom(2048)

        return_code, data = server_message.decode().split(Constants.DELIMITER)
        is_success = int(return_code) == Constants.SUCCESS_CODE
        
        if (not is_success):
          print(Constants.failure_code_message(return_code))

        # parse the data sent back from the server
        parsed_data = json.loads(data)
        if (is_success and not parsed_data == None): 
          successful_command(server_cmd_args.action, parsed_data, self.client_socket)
        
        if (is_success and server_cmd_args.action == 'exit'):
          break
      
      except Exception as err:
        raise Exception('[ERROR]: UDP contact server thread\n' + str(err))
    
    print('Terminating session and client server...')
    self.client_socket.close()
