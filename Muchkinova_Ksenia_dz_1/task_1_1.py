def convert_time(duration: int) -> str:
    if duration < 60:
        res_time = (duration, 'сек')
    elif duration < 3600:
        res_time = (duration // 60, 'мин', duration % 60, 'сек')
    elif duration < 86400:
        res_time = (duration // 3600, 'час', duration % 3600 // 60, 'мин', duration % 3600 % 60, 'сек')
    elif duration < 31536000:
        res_time = (duration // 86400, 'дн', duration % 86400 // 3600, 'час', duration % 86400 % 3600 // 60, 'мин', duration % 86000 % 3600 % 60, 'сек')
    elif duration > 31536000:
        res_time = ('Вы ввели очень большое число')
    return(res_time)
duration = 400153
result = convert_time(duration)
print(result)





