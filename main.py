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


va_data = VaData()
VaConfig.setup(va_data)
app_data = VaData()

VaConfigLocal.setup(app_data)

VaBox.start(va_data,app_data)


print('\nThe end')

