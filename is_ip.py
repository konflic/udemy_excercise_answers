# IP адрес?

def is_ip(string: str):
    # Разделяю строку на части по разделителю
    parts = string.split(".")

    # Если частей не 4 то это точно не IP
    if len(parts) != 4:
        return False

    for el in parts:
        # Если один из элементов не число то не IP
        if not el.isnumeric():
            return False
        # Если один из элементов не в диапазоне то не IP
        if int(el) < 0 or int(el) > 255:
            return False
    
    # Все условия выполнены => IP
    return True
