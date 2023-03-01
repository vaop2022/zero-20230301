def Action__020(va_data,app_data):
    print(va_data.get('The current Action...current action'))

    va_data.set('Direction...direction', 'Direction_10') 
    if(app_data.get('The sum...sum_01') > app_data.get('The max sum...sum_01_max')):
        va_data.set('Direction...direction', 'Direction_20') 

