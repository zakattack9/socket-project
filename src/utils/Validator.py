def validate_register(args):
  if (args.arg1 == None):
    print_missing_arg('client contact name')
  elif (args.arg2 == None):
    print_missing_arg('client ip address')
  elif (args.arg3 == None):
    print_missing_arg('client port number')
  elif (not args.arg3.isdigit()):
    print('Please enter a valid port number')
  else:
    return build_arg_list(args, 4)
  return None

def validate_create(args):
  if (args.arg1 == None):
    print_missing_arg('contact list name')
  else:
    return build_arg_list(args, 2)
  return None

def validate_query_lists(args):
  return build_arg_list(args, 1)

def validate_join(args):
  return verify_contact_list_and_name(args)

def validate_leave(args):
  return verify_contact_list_and_name(args)

def validate_exit(args):
  if (args.arg1 == None):
    print_missing_arg('client contact name')
  else:
    return build_arg_list(args, 2)
  return None

def validate_im_start(args):
  return verify_contact_list_and_name(args)

def validate_im_complete(args):
  return verify_contact_list_and_name(args)

def validate_save(args):
  if (args.arg1 == None):
    print_missing_arg('save filename')
  else:
    return build_arg_list(args, 2)
  return None

def verify_contact_list_and_name(args):
  if (args.arg1 == None):
    print_missing_arg('contact list name')
  elif (args.arg2 == None):
    print_missing_arg('client contact name')
  else:
    return build_arg_list(args, 3)
  return None

def print_missing_arg(missing_arg):
  print('Please specify the ' + missing_arg)

# num_args must include action arg as part of its total
def build_arg_list(args, num_args):
  arg_dict = vars(args)
  arg_values = list(arg_dict.values())

  arg_list = []
  for i in range(num_args):
    arg_list.append(arg_values[i])
  return arg_list
