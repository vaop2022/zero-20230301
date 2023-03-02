from  Action__000  import *
from  Action__010  import *
from  Action__020  import *
from  Action__finish_1  import *



def start(va_data, app_data):

    Action__000(va_data, app_data)
  
    while 1 == 1: 
        va_data.set('Number of jumps...jump', va_data.get('Number of jumps...jump') + 1)
        if va_data.get('Number of jumps...jump') > va_data.get('Max number of jumps...max_jump'):
            print(va_data)
            print("\n\n Error: Looping")
            break

        va_script = va_data.get('VA script...va_script')
        current_action = va_data.get('The current Action...current action')
        direction = va_data.get('Direction...direction')

        temp = va_script[current_action][direction]
        
        va_data.set('The previous Action...previous action', current_action)

        va_data.set('The current Action...current action', temp)
        
        if va_data.get('The current Action...current action') in va_script:
          va_data.set('Direction...direction', 'The_code_of_the_direction_is _unknown')       
          eval(va_data.get('The current Action...current action') + "(va_data, app_data)")
        else:
          break
        
    print('The v-agent is finished jumping in the action [', va_data.get('The current Action...current action'), ']')    

    return
