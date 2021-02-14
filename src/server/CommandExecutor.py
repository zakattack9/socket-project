execute_action = {
  'register': execute_register,
  'create': execute_create,
  'query-lists': execute_query_lists,
  'join': execute_join,
  'leave': execute_leave,
  'exit': execute_exit,
  'im-start': execute_im_start,
  'im-complete': execute_im_complete,
  'save': execute_save,
}

ContactDatabase = None
def execute_command(args, database):
  ContactDatabase = database
  return_code = execute_action[args[0]](args)
  return return_code

def execute_register(args):
  return ContactDatabase.register_contact(args[1], args[2], args[3])

def execute_create(args):
  return ContactDatabase.register_contact(args[1])

def execute_query_lists(args):
  return ContactDatabase.get_lists()

def execute_join(args):
  return ContactDatabase.add_contact_to_list(args[1], args[2])

def execute_leave(args):
  return

def execute_exit(args):
  return ContactDatabase.exit(args[1])

def execute_im_start(args):
  return

def execute_im_complete(args):
  return

def execute_save(args):
  return ContactDatabase.save_to_file(args[1])
