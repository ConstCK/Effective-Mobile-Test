import json
import jsonlines


class PhoneBook:
    """PhoneBook class with methods for adding and retrieving data
     containing user profiles"""

    def __init__(self, name: str, db: str = "data.json") -> None:
        self.name = name
        self.db = db

    def __str__(self) -> str:
        return f"телефонный справочник {self.name}"

    def add_profile(self, data: dict) -> str:
        """Добавление профиля в справочник"""
        all_data: list[dict[str, str | dict[str, str]]] = self.get_all_profiles()
        if self.check_name_duplicate(data, all_data):
            return "Профиль уже существует"
        with jsonlines.open(self.db, mode='a') as file:
            file.write(data)
        return "Профиль успешно создан"

    def get_all_profiles(self) -> list:
        """Получение всех профилей из справочника"""
        with jsonlines.open(self.db, mode='r') as file:
            try:
                result: list[dict[str, str | dict[str, str]]] = [item for item in file]
            except jsonlines.jsonlines.InvalidLineError:
                return []
            return result

    def get_profile_by_name(self, **kwargs: str) -> list[dict[str, str | dict[str, str]]] | str:
        """Получение профиля из справочника с указанием ФИО"""
        all_data: list[dict[str, str | dict[str, str]]] = self.get_all_profiles()
        result = filter(lambda obj:
                        obj.get("name") == kwargs.get("name") and
                        obj.get("surname") == kwargs.get("surname") and
                        obj.get("patronymic") == kwargs.get("patronymic"),
                        all_data)
        return list(result)

    def get_profile_by_organization(self, **kwargs: str) -> list[dict[str, str | dict[str, str]]]:
        """Получение профиля из справочника с указанием организации"""
        all_data: list[dict[str, str | dict[str, str]]] = self.get_all_profiles()
        result = filter(lambda obj:
                        obj.get("organization") == kwargs.get("organization"),
                        all_data)
        return list(result)

    def get_profile_by_phone(self, **kwargs: str) -> list[dict[str, str | dict[str, str]]]:
        """Получение профиля из справочника с указанием номера телефона"""
        all_data: list[dict[str, str | dict[str, str]]] = self.get_all_profiles()
        result = filter(lambda obj:
                        kwargs.get("phone") in obj.get("phone").get("business") or
                        kwargs.get("phone") in obj.get("phone").get("private"),
                        all_data)
        return list(result)

    def update_profile(self, new_data: dict, **kwargs: str) -> str:
        """Изменение данных профиля из справочника с указанием ФИО"""
        all_data: list[dict[str, str | dict[str, str]]] = self.get_all_profiles()
        old_profile = filter(lambda obj:
                             obj.get("name") == kwargs.get("name") and
                             obj.get("surname") == kwargs.get("surname") and
                             obj.get("patronymic") == kwargs.get("patronymic"),
                             all_data)
        try:
            garbage_profile: dict[str, str | dict[str, str]] = list(old_profile)[0]
        except IndexError:
            return "Профиль не найден"
        all_data.remove(garbage_profile)
        if self.check_name_duplicate(new_data, all_data):
            return "Профиль уже существует"
        all_data.append(new_data)
        with jsonlines.open(self.db, mode='w') as file:
            file.write_all(all_data)
        return "Успешное изменение профиля"

    def delete_profile(self, **kwargs: str) -> str:
        """Удаление профиля из справочника с указанием ФИО"""
        all_data: list[dict[str, str | dict[str, str]]]  = self.get_all_profiles()
        profile = filter(lambda obj:
                         obj.get("name") == kwargs.get("name") and
                         obj.get("surname") == kwargs.get("surname") and
                         obj.get("patronymic") == kwargs.get("patronymic"),
                         all_data)
        try:
            garbage_profile: dict[str, str | dict[str, str]] = list(profile)[0]
        except IndexError:
            return "Профиль не найден"
        all_data.remove(garbage_profile)
        with jsonlines.open(self.db, mode='w') as file:
            file.write_all(all_data)
        return "Успешное удаление профиля"

    def show_all_profiles(self) -> list[str]:
        """Построчная печать всех профилей из справочника"""
        result: list = list()
        for obj in self.get_all_profiles():
            result.append(f"{obj.get("name")} {obj.get("patronymic")}"
                          f" {obj.get("surname")}, "
                          f"из организации {obj.get("organization")}."
                          f" Рабочий телефон : {obj.get("phone").get("business")}, "
                          f"персональный телефон : {obj.get("phone").get("private")}.")
        return result

    def show_profile(self, mode: str, **kwargs) -> list[str] | str | None:
        """Печать определенных профилей из справочника"""
        result: list = list()
        if mode == "name":
            data: list[dict[str, str | dict[str, str]]] = self.get_profile_by_name(**kwargs)
        elif mode == "organization":
            data: list[dict[str, str | dict[str, str]]] = self.get_profile_by_organization(**kwargs)
        elif mode == "phone":
            data: list[dict[str, str | dict[str, str]]] = self.get_profile_by_phone(**kwargs)
        else:
            print("Неправильно указан режим")
            return None
        if not data:
            print("данные не найдены")
            return ""
        for obj in data:
            result.append(f"{obj.get("name")} {obj.get("patronymic")}"
                          f" {obj.get("surname")}, "
                          f"из организации {obj.get("organization")}."
                          f" Рабочий телефон : {obj.get("phone").get("business")}, "
                          f"персональный телефон : {obj.get("phone").get("private")}.")
        return result

    def check_name_duplicate(self, data: dict, all_data: list) -> bool:
        """Проверка справочника на ввод повторяющегося профиля
        Примечание: В данном справочнике исключены профили с одинаковыми ФИО"""
        if all_data:
            for item in all_data:
                if (item.get("name") == data.get("name") and
                        item.get("patronymic") == data.get("patronymic") and
                        item.get("surname") == data.get("surname")):
                    return True
        return False
