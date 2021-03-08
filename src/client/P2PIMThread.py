from utils import Constants
import threading
import socket
import json

class P2P_IM_Thread(threading.Thread):
  def __init__(self, p2p_socket):
    threading.Thread.__init__(self)
    self.kill_thread = False
    self.p2p_socket = p2p_socket
    self.p2p_socket.setblocking(0)
  
  def run(self):
    while not self.kill_thread:
      try:
        data, client_info = self.p2p_socket.recvfrom(2048)
        parsed_data = json.loads(data.decode())

        contact_list = parsed_data['contact_list']
        contact_list_len = parsed_data['num_contacts_in_list']
        pointer = parsed_data['pointer']
        original_sender = contact_list[0][Constants.DB_NAME_KEY]
        message = parsed_data['text_message']

        if (pointer > contact_list_len):
          print('\n\n[IM COMPLETED]')
          print('\n$ ', end = '')
          continue

        print('\n\n[NEW MESSAGE]')
        print('From: ' + original_sender)
        print('Message: ' + message)
        print('\n$ ', end = '')

        PEER_IP = contact_list[0 if pointer == contact_list_len else pointer][Constants.DB_IP_KEY]
        PEER_PORT = contact_list[0 if pointer == contact_list_len else pointer][Constants.DB_PORT_KEY] + 1
        
        parsed_data['pointer'] += 1
        self.p2p_socket.sendto(json.dumps(parsed_data).encode(), (PEER_IP, PEER_PORT))
      
      except Exception as err:
        if ('[Errno 11] Resource temporarily unavailable' in str(err)):
          continue
        else:
          raise Exception('[ERROR]: P2P instant message thread\n' + str(err))
    
    print('Terminating P2P instant message process...')
    self.p2p_socket.close()

  def kill(self):
    self.kill_thread = True
