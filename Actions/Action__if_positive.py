def Action__if_positive(va_data, app_data):

    current_index = app_data.get('Индекс...i')
    arr = app_data.get('Входящий массив...Arr')
    current_element = arr[current_index]

    va_data.set('Direction...direction', 'Direction_not_positive')
    if current_element > 0:
        va_data.set('Direction...direction', 'Direction_positive')

