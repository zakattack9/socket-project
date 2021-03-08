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
  print("sup losers i am the best of the best and you are trash boi")
  
  contact_list = data['contact_list']
  contact_list_len = data['num_contacts_in_list']
  if (contact_list_len < 2): 
    print('[IM COMPLETED]\n')
    return

  pointer = 1
  PEER_IP = contact_list[pointer][Constants.DB_IP_KEY]
  PEER_PORT = contact_list[pointer][Constants.DB_PORT_KEY] + 1

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
