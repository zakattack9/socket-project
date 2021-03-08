from utils import Validator
from utils.Constants import DELIMITER

validate_action = {
  'register': Validator.validate_register,
  'create': Validator.validate_create,
  'query-lists': Validator.validate_query_lists,
  'join': Validator.validate_join,
  'leave': Validator.validate_leave,
  'exit': Validator.validate_exit,
  'im-start': Validator.validate_im_start,
  'im-complete': Validator.validate_im_complete,
  'save': Validator.validate_save,
}

# validates command first before formatting the command
def format_server_command(args):
  valid_cmd_args = validate_action[args.action](args)

  if (valid_cmd_args == None): return None

  # format the command args into one long string separated by a delimiter
  return DELIMITER.join(valid_cmd_args)
