from socket import *
from utils import Constants
import json

def print_queried_lists(data):
  num_lists = data['num_lists']
  list_names = data['list_names']

  print('\nTotal number of contact lists: ' + str(num_lists))
  for contact_list in list_names:
    print(contact_list)
  print()

def begin_im_start(data, client_socket):
  print('\nPlease enter a message to send to the group')
  text_message = input('> ')
  print()
  
  pointer = 1
  PEER_IP = data['contact_list'][pointer][Constants.DB_IP_KEY]
  PEER_PORT = data['contact_list'][pointer][Constants.DB_PORT_KEY] + 1

  data['text_message'] = text_message
  data['pointer'] = pointer + 1

  try:
    client_socket.sendto(json.dumps(data).encode(), (PEER_IP, PEER_PORT))

  except Exception as err:
    raise Exception('[ERROR]: im-start\n' + str(err))

def successful_command(action, data, client_socket):
  if (action == 'query-lists'):
    print_queried_lists(data)
  elif (action == 'im-start'):
    begin_im_start(data, client_socket)
