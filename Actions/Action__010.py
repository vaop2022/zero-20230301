def Action__010(va_data,app_data):
    print('Action__010')

    temp = app_data.get('The sum...sum_01')
    app_data.set('The sum...sum_01', temp + 1)

    va_data.set('Direction...direction', 'Direction_10') 
