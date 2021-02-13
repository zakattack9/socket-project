from utils import Validator

DELIMETER = "-_-"

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
  valid_cmd_args = validate_action[server_cmd_args.action](server_cmd_args)
  
  if (valid_cmd_args == None): return None

  # format the command args into one long string separated by a delimeter
  return DELIMETER.join(valid_cmd_args)
