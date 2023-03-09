import os
import sys
fpath = os.path.join(os.path.dirname(__file__), 'Actions')
sys.path.append(fpath)
import VaBox
import Actions
import VaScript
import VaConfig
import VaConfigLocal
from VaData import VaData


va_data = VaData() # отвечает за va-engine ( в коде va-box)
VaConfig.setup(va_data) # инициализатор объекта класса VaData

app_data = VaData() # отвечает за данные приложения, работающего на va-engine
VaConfigLocal.setup(app_data) # инициализатор объекта класса VaData

app_data.set('Входящий массив...Arr', [1, 1, -1])

app_data.printNameValue('Входящий массив...Arr')

VaBox.start(va_data,app_data)

app_data.printNameValue('Сумма...Sum')

print('\nThe end')

