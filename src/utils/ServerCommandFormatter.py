from src.utils import Validator

validate_action = {
  'register': Validator.validate_register,
  'create': Validator.validate_create,
  'query-lists': Validator.validate_query_lists,
  'join': Validator.validate_join,
  'leave': Validator.validate_leave,
  'exit': Validator.validate_exit,
  'im-start': Validator.validate_im_start,
  'im-complete': Validator.validate_im_complete,
  'save': Validator.validate_sav,
}

def format_server_command(server_cmd_args):
  print(server_cmd_args)
  cmdArgsIsValid = validate_action[server_cmd_args.action](args)
  if (not cmdArgsIsValid):
    return False

  # format the command args to send to contact server
  
  return "HI"

