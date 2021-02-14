DELIMETER = "-_-"
MAX_NUM_OF_CONTACTS = 100
MAX_NUM_OF_CONTACT_LISTS = 150

DB_IP_KEY = 'ip'
DB_PORT_KEY = 'port'

SUCCESS_CODE = 200
# register
FAILURE_CODE_DUPLICATE_CONTACT = 455
FAILURE_CODE_MAX_NUM_CONTACTS = 456
# create
FAILURE_CODE_DUPLICATE_LIST = 457
FAILURE_CODE_MAX_NUM_LISTS = 458
# join / exit
FAILURE_CODE_UNREGISTERED_CONTACT = 459
# join
FAILURE_CODE_UNCREATED_LIST = 460
FAILURE_CODE_DUPLICATE_CONTACT_IN_LIST = 461
# save
FAILURE_CODE_FILE_SAVE_ERROR = 462

FAILURE_CODE_MESSAGES = {
  '455': 'The specified contact name already exists',
  '456': 'The server has reached its max capacity of active contacts',
  '457': 'The specified contact list name already exists',
  '458': 'The server has reached its max capacity of contact lists',
  '459': 'The specified contact name does not exist',
  '460': 'The specified contact list does not exist',
  '461': 'The specified contact name already exists in this list',
  '462': 'The server was unable to save its data to the specified file'
}

def failure_code_message(failure_code):
  failure_code = str(failure_code)
  if (failure_code in FAILURE_CODE_MESSAGES):
    return '[' + failure_code + ']: ' + FAILURE_CODE_MESSAGES[failure_code]
  else:
    return '[ERROR]: Command not executed due to an error that occurred on the server side'
  