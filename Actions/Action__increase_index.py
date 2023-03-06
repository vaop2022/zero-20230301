def Action__increase_index(va_data, app_data):

    current_index = app_data.get('Индекс...i')

    app_data.set('Индекс...i', current_index + 1)

    va_data.set('Direction...direction', 'Direction_forward')
