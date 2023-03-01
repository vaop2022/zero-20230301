def Action__010(va_data,app_data):
    print(va_data.get('The current Action...current action'))

    temp = app_data.get('The sum...sum_01')
    app_data.set('The sum...sum_01', temp + 1)

    app_data.printNameValue('The sum...sum_01')

    va_data.set('Direction...direction', 'Direction_10') 
