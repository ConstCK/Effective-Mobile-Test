import jsonlines


class PhoneBook:
    """PhoneBook class with methods for adding and retrieving data
     containing user profiles"""

    def __init__(self, name: str, db: str) -> None:
        self.name = name
        self.db = db
        self.id = 1

    def __str__(self):
        return f"телефонный справочник {self.name}"

    def add_profile(self, data: dict) -> str:
        """Добавление профиля в справочник"""
        if self.check_duplicate(data):
            return "The current profile already exists"
        with jsonlines.open(self.db, mode='a') as file:
            file.write(data)
        return "The current profile is successfully created"

    def get_all_profiles(self) -> list:
        """Получение всех профилей из справочника"""
        with jsonlines.open(self.db, mode='r') as file:
            result = [item for item in file]
            return result

    def get_profile_by_name(self, **kwargs: str) -> list | str:
        """Получение профиля из справочника с указанием ФИО"""
        all_data = self.get_all_profiles()
        result = filter(lambda obj:
                        obj.get("name") == kwargs.get("name") and
                        obj.get("surname") == kwargs.get("surname") and
                        obj.get("patronymic") == kwargs.get("patronymic"),
                        all_data)

        return list(result)

    def get_profile_by_organization(self, **kwargs: str) -> list | str:
        all_data = self.get_all_profiles()
        result = filter(lambda obj:
                        obj.get("organization") == kwargs.get("organization"),
                        all_data)
        return list(result)

    def show_all_profiles(self) -> None:
        """Построчная печать всех профилей из справочника"""
        for obj in self.get_all_profiles():
            print(f"{obj.get("name")} {obj.get("patronymic")}"
                  f" {obj.get("surname")}, "
                  f"из организации {obj.get("organization")}."
                  f" Рабочий телефон : {obj.get("phone").get("business")}, "
                  f"персональный телефон : {obj.get("phone").get("private")}.")

    def show_profile(self, mode: str, **kwargs) -> None:
        """Печать определенных профилей из справочника"""
        result = None
        if mode == "name":
            result = self.get_profile_by_name(**kwargs)
        if mode == "organization":
            result = self.get_profile_by_organization(**kwargs)
        if not result:
            print('Профиль не найден')
        for obj in result:
            print(f"{obj.get("name")} {obj.get("patronymic")}"
                  f" {obj.get("surname")}, "
                  f"из организации {obj.get("organization")}."
                  f" Рабочий телефон : {obj.get("phone").get("business")}, "
                  f"персональный телефон : {obj.get("phone").get("private")}.")

    def check_duplicate(self, data: dict) -> bool:
        """Проверка справочника на ввод повторяющегося профиля"""
        all_data = self.get_all_profiles()
        return True if data in all_data else False


p1 = {"surname": "Johnson",
      "name": "Joe",
      "patronymic": "Petrovich",
      "organization": "MTC",
      "phone": {
          "business": "+71234567890",
          "private": "+79876543210",
      }
      }

p2 = {"surname": "Ivanov",
      "name": "Ivan",
      "patronymic": "Ivanovich",
      "organization": "Beeline",
      "phone": {
          "business": "+711111111111",
          "private": "+79999999999",
      }
      }

p3 = {"surname": "Maximov",
      "name": "Maxim",
      "patronymic": "Maximovich",
      "organization": "Tele2",
      "phone": {
          "business": "+70001112233",
          "private": "+79998887766",
      }
      }

p4 = {"surname": "Kozlov",
      "name": "Akop",
      "patronymic": "Sergeevich",
      "organization": "Tele2",
      "phone": {
          "business": "+70001112233",
          "private": "+79998887766",
      }
      }
conn = PhoneBook('1st_book', 'data.json')
#
conn.add_profile(p1)
conn.add_profile(p2)
conn.add_profile(p4)
conn.add_profile(p3)

print(conn)
# conn.show_all_profiles()
# a = conn.get_profile_by_name(name='Joe', patronymic="Petrovich", surname="Johnson")
b = conn.get_profile_by_organization(organization='MTC')
conn.show_profile('name', name='Joe', patronymic="Petrovich", surname="Johnson")
conn.show_profile('organization', organization='Tele23')
