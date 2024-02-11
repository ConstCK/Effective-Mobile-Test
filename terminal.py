from phone_book import PhoneBook
from validators import InputValidator


class Terminal:
    def __init__(self, book_name) -> None:
        self.conn = PhoneBook(book_name, 'data.json')
        self.validator = InputValidator()

    def greetings(self) -> None:
        print(f"Добро пожаловать в телефонный справочник {self.conn}")
        print(f"Используйте ввод чисел (1-7) для навигации по меню")

    @staticmethod
    def show_menu() -> None:
        print("1 - Получение всех данных справочника")
        print("2 - Получение данных справочника по ФИО")
        print("3 - Получение данных справочника по названию организации")
        print("4 - Получение данных справочника по номеру телефона")
        print("5 - Добавление профиля в справочник")
        print("6 - Изменение профиля в справочнике")
        print("7 - Удаление профиля в справочнике!")

    def input_name(self) -> dict[str, str]:
        """Ввод ФИО для профиля с валидацией данных"""
        while True:
            name = input("Введите имя (С заглавной буквы): ")
            patronymic = input("Введите отчество (С заглавной буквы): ")
            surname = input("Введите фамилию (С заглавной буквы): ")
            if (self.validator.name_validation(name) and
                    self.validator.name_validation(patronymic) and
                    self.validator.name_validation(surname)):
                return {"name": name,
                        "patronymic": patronymic,
                        "surname": surname
                        }
            print("Данные не корректны. Введите заново...")

    def input_organization(self) -> dict[str, str]:
        """Ввод названия организации для профиля с валидацией данных"""
        while True:
            organization = input("Введите название организации (С заглавной буквы): ")
            if self.validator.organization_validation(organization):
                return {"organization": organization}
            print("Данные не корректны. Введите заново...")

    def input_phone(self) -> dict[str, str]:
        """Ввод номера телефона для профиля с валидацией данных"""
        while True:
            phone = input("Введите номер телефона (в формате +71234567890): ")
            if self.validator.phone_validation(phone):
                return {"phone": phone}
            print("Данные не корректны. Введите заново...")

    def input_new_profile(self):
        """Ввод всех данных для профиля с валидацией данных"""
        while True:
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            surname = input("Введите фамилию: ")
            organization = input("Введите организацию: ")
            business_phone = input("Введите рабочий номер телефона: ")
            private_phone = input("Введите домашний номер телефона: ")
            if (self.validator.name_validation(name) and
                    self.validator.name_validation(patronymic) and
                    self.validator.name_validation(surname) and
                    self.validator.organization_validation(organization) and
                    self.validator.phone_validation(business_phone) and
                    self.validator.phone_validation(private_phone)):
                return {"name": name,
                        "patronymic": patronymic,
                        "surname": surname,
                        "organization": organization,
                        "phone": {
                            "business": business_phone,
                            "private": private_phone
                        }
                        }
            print("Данные не корректны. Введите заново...")

    def run_program(self):
        """Ввод команд меню для управления справочником"""
        choice = None
        while choice != 0:
            self.show_menu()
            try:
                choice = int(input("Введите номер операции: "))
            except ValueError:
                print("Ошибка ввода. Введите число (1-7)")
            match choice:
                case 0:
                    print("Выход из программы...")
                    break
                case 1:
                    print("Получение всех данных справочника...")
                    self.conn.show_all_profiles()
                case 2:
                    print("Получение данных справочника по ФИО...")
                    data = self.input_name()
                    self.conn.show_profile("name", name=data.get("name"),
                                           patronymic=data.get("patronymic"),
                                           surname=data.get("surname"))
                case 3:
                    print("Получение данных справочника по названию организации...")
                    data = self.input_organization()
                    self.conn.show_profile("organization", organization=data.get("organization"))
                case 4:
                    print("Получение данных справочника по названию организации...")
                    data = self.input_phone()
                    self.conn.show_profile("phone", phone=data.get("phone"))
                case 5:
                    print("Добавление профиля в справочник...")
                    data = self.input_new_profile()
                    self.conn.add_profile(data)
                case 6:
                    print("Изменение профиля в справочнике...")
                    print("Ввод данных профиля для изменения...")
                    old_profile = self.input_name()
                    print("Ввод новых данных профиля...")
                    new_profile = self.input_new_profile()
                    self.conn.update_profile(new_profile,
                                             name=old_profile.get("name"),
                                             patronymic=old_profile.get("patronymic"),
                                             surname=old_profile.get("surname")
                                             )
                case 7:
                    print("Удаление профиля в справочнике...")
                    print("Ввод данных профиля для удаления...")
                    data = self.input_name()
                    self.conn.delete_profile(
                        name=data.get("name"),
                        patronymic=data.get("patronymic"),
                        surname=data.get("surname")
                    )
                case _:
                    print("Неизвестная команда. Введите число (1-7)")

        print("Программа завершена!")
        return "Программа завершена!"
