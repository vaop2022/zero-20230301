def Action__increase_sum(va_data, app_data):

    temp_sum = app_data.get('Сумма...Sum')
    current_index = app_data.get('Индекс...i')
    arr = app_data.get('Входящий массив...Arr')

    app_data.set('Сумма...Sum', arr[current_index] + temp_sum)


    va_data.set('Direction...direction', 'Direction_forward')
