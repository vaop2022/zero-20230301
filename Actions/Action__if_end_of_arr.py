def Action__increase_index(va_data, app_data):

    current_index = app_data.get('Индекс...i')
    arr = app_data.get('Входящий массив...Arr')

    va_data.set('Direction...direction', 'Direction_loop_back')
    if current_index > len(arr) - 1:
        va_data.set('Direction...direction', 'Direction_finish')

