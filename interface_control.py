from phone_book import PhoneBook


class InterfaceControl:
    def __init__(self, book_name):
        self.conn = PhoneBook(book_name, 'data.json')

    def greetings(self) -> None:
        print(f"Добро пожаловать в телефонный справочник {self.conn}")
        print(f"Используйте ввод чисел (1-7) для навигации по меню")

    def show_menu(self) -> None:
        print("1 - Получение всех данных справочника")
        print("2 - Получение данных справочника по ФИО")
        print("3 - Получение данных справочника по названию организации")
        print("4 - Получение данных справочника по номеру телефона")
        print("5 - Добавление профиля в справочник")
        print("6 - Изменение профиля в справочнике")
        print("7 - Удаление профиля в справочнике")
