def custom_write(file_name, strings):
    """
    Функция записывает строки в файл и возвращает словарь с позициями строк.

    :param file_name: имя файла для записи
    :param strings: список строк для записи
    :return: словарь с информацией о позициях строк в формате:
             {(номер строки, байт начала): строка}
    """
    strings_positions = {}  # Словарь для хранения информации о строках

    # Открываем файл для записи в кодировке utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for line_num, string in enumerate(strings, start=1):  # Перебираем строки с их номерами
            start_byte = file.tell()  # Запоминаем позицию начала строки
            file.write(string + '\n')  # Записываем строку с переходом на новую строку
            strings_positions[(line_num, start_byte)] = string  # Добавляем данные в словарь

    return strings_positions


# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
