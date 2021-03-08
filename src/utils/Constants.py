DELIMITER = "-_-"

MIN_PORT_NUM = 22000
MAX_PORT_NUM = 22499

MAX_NUM_OF_CONTACTS = 100
MAX_NUM_OF_CONTACT_LISTS = 150

DB_NAME_KEY = 'name'
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
# join / leave / exit
FAILURE_CODE_ONGOING_IM = 463
# leave
FAILURE_CODE_MISSING_CONTACT_IN_LIST = 464
# im-complete
FAILURE_CODE_INVALID_IM_COMPLETE = 465

FAILURE_CODE_MESSAGES = {
  str(FAILURE_CODE_DUPLICATE_CONTACT)         : 'The specified contact name already exists',
  str(FAILURE_CODE_MAX_NUM_CONTACTS)          : 'The server has reached its max capacity of active contacts',
  str(FAILURE_CODE_DUPLICATE_LIST)            : 'The specified contact list name already exists',
  str(FAILURE_CODE_MAX_NUM_LISTS)             : 'The server has reached its max capacity of contact lists',
  str(FAILURE_CODE_UNREGISTERED_CONTACT)      : 'The specified contact name does not exist',
  str(FAILURE_CODE_UNCREATED_LIST)            : 'The specified contact list does not exist',
  str(FAILURE_CODE_DUPLICATE_CONTACT_IN_LIST) : 'The specified contact name already exists in the list',
  str(FAILURE_CODE_FILE_SAVE_ERROR)           : 'The server was unable to save its data to the specified file',
  str(FAILURE_CODE_ONGOING_IM)                : 'The server was unable to complete the request due to an ongoing instant message',
  str(FAILURE_CODE_MISSING_CONTACT_IN_LIST)   : 'The specified contact name does not exists in the list',
  str(FAILURE_CODE_INVALID_IM_COMPLETE)       : 'The specified contact did not initiate an im-start for the contact list'
}

def failure_code_message(failure_code):
  failure_code = str(failure_code)
  if (failure_code in FAILURE_CODE_MESSAGES):
    return '[' + failure_code + ']: ' + FAILURE_CODE_MESSAGES[failure_code]
  else:
    return '[ERROR]: Command not executed due to an error that occurred on the server side'
  