class Product:
    """Класс для описания товара"""
    def __init__(self, name, weight, category):
        self.name = name  # Название товара
        self.weight = weight  # Вес товара
        self.category = category  # Категория товара

    def __str__(self):
        """Возвращает строковое представление товара"""
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    """Класс для работы с магазином"""
    __file_name = 'products.txt'  # Инкапсулированное имя файла

    def __init__(self):
        """Инициализация класса Shop"""
        # Создаём файл, если его ещё нет
        open(self.__file_name, 'a').close()

    def get_products(self):
        """Считывает все данные из файла __file_name и возвращает единую строку"""
        with open(self.__file_name, 'r') as file:
            return file.read().strip()  # Убираем лишние пустые строки с помощью strip()

    def add(self, *products):
        """
        Добавляет товары в магазин:
        - Если товара нет, добавляет его в файл.
        - Если товар уже есть (по name и category), увеличивает его общий вес.
        """
        # Читаем все товары из файла
        current_products = self.get_products().split('\n')
        current_products = [line.split(', ') for line in current_products if line]  # Парсим строки в списки

        with open(self.__file_name, 'a') as file:
            for product in products:
                # Проверяем, есть ли такой товар уже в файле
                for prod in current_products:
                    if prod[0] == product.name and prod[2] == product.category:
                        # Если товар найден, увеличиваем его общий вес
                        new_weight = float(prod[1]) + product.weight
                        prod[1] = str(new_weight)
                        print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {new_weight}')
                        break
                else:
                    # Если товар не найден, добавляем его в файл
                    file.write(str(product) + '\n')
                    current_products.append([product.name, str(product.weight), product.category])

        # Перезаписываем файл для обновления весов
        with open(self.__file_name, 'w') as file:
            for prod in current_products:
                file.write(', '.join(prod) + '\n')


# Пример работы программы
s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
