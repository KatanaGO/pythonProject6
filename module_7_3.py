import string


class WordsFinder:
    def __init__(self, *file_names):
        """
        Инициализация объекта. Сохраняем названия файлов в атрибут file_names.
        :param file_names: названия файлов
        """
        self.file_names = file_names  # Сохраняем переданные названия файлов

    def get_all_words(self):
        """
        Метод возвращает словарь с названием файла в качестве ключа и списком всех слов из файла в качестве значения.
        """
        all_words = {}  # Словарь для хранения результата
        punctuations = [',', '.', '=', '!', '?', ';', ':', ' - ']  # Убираемая пунктуация

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Чтение файла, перевод в нижний регистр
                    text = file.read().lower()

                    # Удаление пунктуации
                    for p in punctuations:
                        text = text.replace(p, '')

                    # Разделение текста на слова
                    words = text.split()

                    # Запись результата в словарь
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден. Пропускаем.")
                all_words[file_name] = []

        return all_words

    def find(self, word):
        """
        Метод ищет первое вхождение слова в каждом из файлов.
        :param word: искомое слово
        :return: словарь с первым вхождением слова в каждом файле
        """
        word = word.lower()  # Игнорируем регистр при поиске
        results = {}

        for file_name, words in self.get_all_words().items():
            # Найти индекс первого вхождения слова или вернуть None
            try:
                position = words.index(word) + 1  # Индексы в Python с 0, поэтому добавляем 1
                results[file_name] = position
            except ValueError:
                results[file_name] = None  # Слово не найдено в файле

        return results

    def count(self, word):
        """
        Метод считает количество вхождений слова в каждом из файлов.
        :param word: искомое слово
        :return: словарь с количеством вхождений слова в каждом файле
        """
        word = word.lower()  # Игнорируем регистр при подсчёте
        results = {}

        for file_name, words in self.get_all_words().items():
            # Подсчитываем количество вхождений
            results[file_name] = words.count(word)

        return results


# Пример использования
finder = WordsFinder('test_file.txt')

# Тестируем методы
print(finder.get_all_words())  # Все слова в файле
print(finder.find('TEXT'))     # Позиция первого вхождения слова 'TEXT'
print(finder.count('teXT'))    # Количество вхождений слова 'teXT'
