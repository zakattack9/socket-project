from utils.Socket import create_pair_socket, validate_port
from client.ContactServerThread import Contact_Server_Thread
from client.P2PIMThread import P2P_IM_Thread
import argparse

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

try:
  client_socket, p2p_socket = create_pair_socket(SERVER_PORT)

  contact_server_thread = Contact_Server_Thread(client_socket, SERVER_IP, SERVER_PORT)
  p2p_im_thread = P2P_IM_Thread(p2p_socket)

  contact_server_thread.start()
  p2p_im_thread.start()

  contact_server_thread.join()
  p2p_im_thread.kill()
  p2p_im_thread.join()

except Exception as err:
  print('[ERROR]: Occurred with the UDP Client\n' + str(err))
