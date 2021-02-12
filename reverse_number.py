# Переворачиваем число

def reverse_number(number):
    # Определяем является ли число отрицательным, можно 
    negative =  number < 0

    # Приводим к строке для дальнейших манипуляций
    str_number = str(number)

    if negative:
        # Для удобства убираем минус из строки
        str_number = str_number.replace("-", "")
    
    if "." in str_number:
        # Если есть точка. то переворачиваем части числа отдельно и приводим к floaf
        res = float(str_number.split(".")[0][::-1] + "." + str_number.split(".")[1][::-1])
    else:
        # Переворачиваем число и приводим к int
        res = int(str_number[::-1])

    # В конце возвращаем минус который убрали в начале если число было отрицательным
    return res * (-1 if negative else 1)
