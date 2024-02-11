from phone_book import PhoneBook

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
          "business": "+70001112200",
          "private": "+79998887700",
      }
      }
conn = PhoneBook('1st_book', 'data.json')
#
# conn.add_profile(p1)
# conn.add_profile(p2)
# conn.add_profile(p4)
# conn.add_profile(p3)

print(conn)
# conn.show_all_profiles()
# a = conn.get_profile_by_name(name='Joe', patronymic="Petrovich", surname="Johnson")
# b = conn.get_profile_by_organization(organization='MTC')
# conn.show_profile('name', name='Joe', patronymic="Petrovich", surname="Jonson")
# conn.show_profile('phone', phone='+79998887765')
# conn.update_profile({"surname": "Jonson",
#                      "name": "Joe",
#                      "patronymic": "Petrovich",
#                      "organization": "MTC",
#                      "phone": {
#                          "business": "+71234567890",
#                          "private": "+79876543210",
#                      }
#                      }, name='Joe', patronymic="Petrovich", surname="Jonson1")
conn.delete_profile(name='Joe', patronymic="Petrovich", surname="Johnson")

