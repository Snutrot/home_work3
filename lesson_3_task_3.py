from lesson_3_task_3_Address import Address
from lesson_3_task_3_Mailing import Mailing

# Создание экземпляров класса Address
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "20", "3")

# Создание экземпляра класса Mailing
mailing = Mailing(to_address, from_address, 250, "TRK123456")

# Печать информации об отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
