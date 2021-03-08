from utils import Constants
from utils.FileWriter import FileWriter

contacts = {}
contact_lists = {}
ongoing_ims = {}

def register_contact(contact_name, ip, port):
  if (contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_DUPLICATE_CONTACT)
  if (len(contacts) + 1 > Constants.MAX_NUM_OF_CONTACTS):
    return _build_response(Constants.FAILURE_CODE_MAX_NUM_CONTACTS)

  contacts[contact_name] = { 
    Constants.DB_NAME_KEY: contact_name,
    Constants.DB_IP_KEY: ip, 
    Constants.DB_PORT_KEY: port 
  }
  return _build_response(Constants.SUCCESS_CODE)

def create_contact_list(list_name):
  if (list_name in contact_lists):
    return _build_response(Constants.FAILURE_CODE_DUPLICATE_LIST)
  if (len(contact_lists) + 1 > Constants.MAX_NUM_OF_CONTACT_LISTS):
    return _build_response(Constants.FAILURE_CODE_MAX_NUM_LISTS)
  
  contact_lists[list_name] = []
  ongoing_ims[list_name] = []
  return _build_response(Constants.SUCCESS_CODE)

def get_lists():
  num_lists = len(contact_lists)
  list_names = list(contact_lists.keys())

  response_str = 'Total number of contact lists: ' + str(num_lists)
  for contact_list in list_names:
    response_str += '\n' + contact_list
  return _build_response(Constants.SUCCESS_CODE, response_str)

def add_contact_to_list(list_name, contact_name):
  if (not contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_UNREGISTERED_CONTACT)
  if (not list_name in contact_lists):
    return _build_response(Constants.FAILURE_CODE_UNCREATED_LIST)
  if (contact_name in contact_lists[list_name]):
    return _build_response(Constants.FAILURE_CODE_DUPLICATE_CONTACT_IN_LIST)
  if (_is_ongoing_im(list_name)):
    return _build_response(Constants.FAILURE_CODE_ONGOING_IM)
  
  contact_lists[list_name].append(contact_name)
  return _build_response(Constants.SUCCESS_CODE)

def remove_contact_from_list(list_name, contact_name):
  if (not contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_UNREGISTERED_CONTACT)
  if (not list_name in contact_lists):
    return _build_response(Constants.FAILURE_CODE_UNCREATED_LIST)
  if (not contact_name in contact_lists[list_name]):
    return _build_response(Constants.FAILURE_CODE_MISSING_CONTACT_IN_LIST)
  if (_is_ongoing_im(list_name)):
    return _build_response(Constants.FAILURE_CODE_ONGOING_IM)

  contact_lists[list_name].remove(contact_name)
  return _build_response(Constants.SUCCESS_CODE)

def exit(contact_name):
  if (not contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_UNREGISTERED_CONTACT)
  
  # check if contact is in any ongoing im's
  for list_name, list_contacts in contact_lists.items():
    if (contact_name in list_contacts and _is_ongoing_im(list_name)):
      return _build_response(Constants.FAILURE_CODE_ONGOING_IM)

  # delete contact from all associated contact lists
  for list_contacts in contact_lists.values():
    if (contact_name in list_contacts):
      list_contacts.remove(contact_name)
  
  # delete contact from list of currently active contacts
  del contacts[contact_name]

  return _build_response(Constants.SUCCESS_CODE)

def begin_instant_message(list_name, contact_name):
  if (not contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_UNREGISTERED_CONTACT)
  if (not list_name in contact_lists):
    return _build_response(Constants.FAILURE_CODE_UNCREATED_LIST)
  if (not contact_name in contact_lists[list_name]):
    return _build_response(Constants.FAILURE_CODE_MISSING_CONTACT_IN_LIST)
  
  full_contact_list = []
  for contact in contact_lists[list_name]:
    if (contact == contact_name):
      full_contact_list.insert(0, contacts[contact])
    else:
      full_contact_list.append(contacts[contact])

  res_obj = {
    'num_contacts': len(contact_lists[list_name]),
    'contact_list': full_contact_list,
  }
  print(full_contact_list)

  ongoing_ims[list_name].append(contact_name)
  return _build_response(Constants.SUCCESS_CODE, res_obj)

def end_instant_message(list_name, contact_name):
  if (not contact_name in contacts):
    return _build_response(Constants.FAILURE_CODE_UNREGISTERED_CONTACT)
  if (not list_name in contact_lists):
    return _build_response(Constants.FAILURE_CODE_UNCREATED_LIST)
  if (not contact_name in contact_lists[list_name]):
    return _build_response(Constants.FAILURE_CODE_MISSING_CONTACT_IN_LIST)
  if (not contact_name in ongoing_ims[list_name]):
    return _build_response(Constants.FAILURE_CODE_INVALID_IM_COMPLETE)

  ongoing_ims[list_name].remove(contact_name)
  return _build_response(Constants.SUCCESS_CODE)

def save_to_file(file_name):
  try:
    file = FileWriter(file_name)
    file.clear_contents() # overwrite same file with each save
    
    # write line containing number of contacts
    file.append_to_end(str(len(contacts)), False)
    # for each contact, append a line containing the contact's info
    for contact_name, contact_info in contacts.items():
      _save_contact_info(
        file,
        contact_name, 
        contact_info[Constants.DB_IP_KEY], 
        contact_info[Constants.DB_PORT_KEY])
      
    # append line containing number of contact lists
    file.append_line(str(len(contact_lists)))
    # for each list, append its name, number of contacts, and their respective contact info
    for list_name, list_contacts in contact_lists.items():
      # append line containing contact list name
      file.append_line(list_name)
      # append line containing number of contacts in current list
      file.append_line(str(len(list_contacts)))
      # for each contact in the current list, append a line containing the contact's info
      # skips first index of contact list
      for contact in list_contacts:
        _save_contact_info(
          file,
          contact, 
          contacts[contact][Constants.DB_IP_KEY], 
          contacts[contact][Constants.DB_PORT_KEY])
    file.close()
  except Exception as err:
    print('[CONTACT DB ERROR]: Occurred while saving to file\n' + str(err))
    return _build_response(Constants.FAILURE_CODE_FILE_SAVE_ERROR)
  return _build_response(Constants.SUCCESS_CODE)

# appends contact name, IP address, and port number on one line to the end of a file
def _save_contact_info(file, name, ip, port):
  file.append_line(name)
  file.append_to_end(ip)
  file.append_to_end(port)

def _build_response(return_code, data = None):
  return (return_code, data)

def _is_ongoing_im(list_name):
  return list_name in ongoing_ims and len(ongoing_ims[list_name]) > 0
