import os
import time

# Укажите путь к каталогу, который хотите просмотреть (для примера используется текущая директория)
directory = "."

# Обход каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # Полный путь к файлу
        filepath = os.path.join(root, file)

        # Время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Размер файла
        filesize = os.path.getsize(filepath)

        # Родительская директория файла
        parent_dir = os.path.dirname(filepath)

        # Вывод информации
        print(
            f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}")
