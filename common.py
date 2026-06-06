"""
To avoid 'Circular Import Error' this module created.
"""
task_list = []
json_file = None

def task_uuid():
      """
      'task_uuid' method checks there is an specific uuid or not;
      if there was: returns a boolean value 'True' and that dict
      if there wasn't: returns a boolean value 'False'
      """
      input_uuid = input("\nEnter UUID: ")
      for dict_element in task_list:
            if dict_element["UUID"] == input_uuid:
               return True, dict_element
      else:
        return False, None