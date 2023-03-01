def getVaScript():
    va_script = {
      "Action__000":{
          "_agent_position":{
              "en-US":"In Init block of VA-box",
              "ru-RU":"В блоке Init VA-box"
          },
          "_action_description":{
              "_010":"--> init action"
          },
          "Direction_10":"Action__010",  "_010":"ok",
          
      },
      "Action__010":{
          "_agent_position":{
              "en-US":"The v-agent is adding 1 to sum_01",
              "ru-RU":"v-agent добавляет 1 sum_01"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_10":"Action__020",  "_010":"go to check",
      },
      "Action__020":{
          "_agent_position":{
              "en-US":"The v-agent checks if sum_01 is greater than sum_01_max",
              "ru-RU":"v-agent проверяет если sum_01 больше sum_01_max"
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_10":"Action__010",  "_010":"sum_01 < sum_01_max",
          "Direction_20":"Action_9000",  "_010":"end"
      },   
      "Action__9000":{
          "_agent_position":{
              "en-US":"",
              "ru-RU":""
          },
          "_action_description":{
              "_010":"empty"
          },
          "Direction_10":"Action_END",  "_010":"Final action / The end"
      }
    }

    return va_script
    