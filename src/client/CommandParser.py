import argparse

server_command_parser = argparse.ArgumentParser(description='Parser to parse commands for contact server interactions')
server_command_parser.add_argument(
  'action',
  choices=[
    'register', 
    'create', 
    'query-lists', 
    'join', 
    'leave', 
    'exit', 
    'im-start', 
    'im-complete', 
    'save'
  ],
  help='Action to be taken on contact server'
)
server_command_parser.add_argument(
  'arg1',
  nargs='?',
  help='<contact-name | contact-list-name | file-name>'
)
server_command_parser.add_argument(
  'arg2',
  nargs='?',
  help='<ip-address | contact-name>'
)
server_command_parser.add_argument(
  'arg3',
  nargs='?',
  help='<port>'
)

def parse_server_command(server_cmd):
  try:
    args = server_command_parser.parse_args(server_cmd.split())
    return args
  except SystemExit:
    print("Error parsing server command input, please ensure your input is a valid server command!!!")
    return None
