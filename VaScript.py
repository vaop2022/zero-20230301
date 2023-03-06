def getVaScript():
    va_script = {
      "Action__init":{
        "_action_description":{
              "description_1":"Set initial app_data"
          },
          "Direction_forward":"Action__increase_sum",  "Description of Direction_forward":"Go streight forward"
          
      },
      "Action__increase_sum":{
          "_action_description":{
              "description_1":"Increase_sum"
          },
          "Direction_forward":"Action__increase_index",  "Description of Direction_forward":"Go streight forward"
          
      },
      "Action__increase_index":{
          "_action_description":{
              "description_1":"increase_index"
          },
          "Direction_forward":"Action__if_end_of_arr",  "Description of Direction_forward":"Go streight forward"
          
      },
      "Action__if_end_of_arr":{
          "_action_description":{
              "description_1":"if end of arr"
          },
          "Direction_loop_back":"Action__increase_sum",  "Description of Direction_loop_back":"not end of arr",
          "Direction_finish":"Action__finish",  "Description of Direction_finish":"ok"
      },
      "Action__finish":{
          "_action_description":{
              "description_1":"finish"
          },
          "Direction_forward":"Action__END",  "Description of Direction_forward":"Go streight forward"    
      }
    }

    return va_script
    