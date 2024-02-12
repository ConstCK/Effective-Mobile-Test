import jsonlines
import pytest

from fake_data import p1, p2, p4, p5, p6, p7, p8, p9, p3, p10, p11
from phone_book import PhoneBook

my_test = PhoneBook('my test book', 'test.json')


@pytest.fixture(scope="function")
def initial_run():
    with jsonlines.open("test.json", mode='w'):
        pass


def test_get_initial_data(initial_run):
    assert my_test.show_all_profiles() == []


@pytest.mark.parametrize("data, expected", [(p1, "Профиль успешно создан"),
                                            (p2, "Профиль успешно создан"),
                                            (p3, "Профиль успешно создан"),
                                            (p1, "Профиль уже существует")
                                            ])
def test_create_profile(data, expected):
    assert my_test.add_profile(data) == expected


@pytest.mark.parametrize("mode, input_data, expected", [("name", p4, [f"{p2.get("name")} {p2.get("patronymic")}"
                                                                      f" {p2.get("surname")}, "
                                                                      f"из организации {p2.get("organization")}."
                                                                      f" Рабочий телефон : {p2.get("phone").get("business")}, "
                                                                      f"персональный телефон : {p2.get("phone").get("private")}."]),
                                                        ("organization", p5,
                                                         [f"{p2.get("name")} {p2.get("patronymic")}"
                                                          f" {p2.get("surname")}, "
                                                          f"из организации {p2.get("organization")}."
                                                          f" Рабочий телефон : {p2.get("phone").get("business")}, "
                                                          f"персональный телефон : {p2.get("phone").get("private")}.",
                                                          f"{p3.get("name")} {p3.get("patronymic")}"
                                                          f" {p3.get("surname")}, "
                                                          f"из организации {p3.get("organization")}."
                                                          f" Рабочий телефо"
                                                          f"н : {p3.get("phone").get("business")}, "
                                                          f"персональный телефон : "
                                                          f"{p3.get("phone").get("private")}."
                                                          ]),
                                                        ("phone", p6, [f"{p3.get("name")} {p3.get("patronymic")}"
                                                                       f" {p3.get("surname")}, "
                                                                       f"из организации {p3.get("organization")}."
                                                                       f" Рабочий телефон : {p3.get("phone").get("business")}, "
                                                                       f"персональный телефон : {p3.get("phone").get("private")}."]),
                                                        ("name", p7, ""),
                                                        ("organization", p8, ""),
                                                        ("phone", p9, ""),
                                                        ])
def test_get_profile(mode, input_data, expected):
    assert my_test.show_profile(mode, **input_data) == expected


def test_get_all_data():
    assert my_test.show_all_profiles() == [f"{p1.get("name")} {p1.get("patronymic")}"
                                           f" {p1.get("surname")}, "
                                           f"из организации {p1.get("organization")}."
                                           f" Рабочий телефон : {p1.get("phone").get("business")}, "
                                           f"персональный телефон : {p1.get("phone").get("private")}.",
                                           f"{p2.get("name")} {p2.get("patronymic")}"
                                           f" {p2.get("surname")}, "
                                           f"из организации {p2.get("organization")}."
                                           f" Рабочий телефон : {p2.get("phone").get("business")}, "
                                           f"персональный телефон : {p2.get("phone").get("private")}.",
                                           f"{p3.get("name")} {p3.get("patronymic")}"
                                           f" {p3.get("surname")}, "
                                           f"из организации {p3.get("organization")}."
                                           f" Рабочий телефон : {p3.get("phone").get("business")}, "
                                           f"персональный телефон : {p3.get("phone").get("private")}."
                                           ]


@pytest.mark.parametrize("new_data, old_data, expected", [(p10, p4, "Успешное изменение профиля"),
                                                          (p10, p7, "Профиль не найден"),
                                                          (p10, p11, "Профиль уже существует"),

                                                          ])
def test_update_profile(new_data, old_data, expected):
    assert my_test.update_profile(new_data, **old_data) == expected


@pytest.mark.parametrize("input_data, expected", [(p11, "Успешное удаление профиля"),
                                                  (p7, "Профиль не найден"),
                                                  ])
def test_delete_profile(input_data, expected):
    assert my_test.delete_profile(**input_data) == expected
