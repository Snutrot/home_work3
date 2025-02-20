from smartphone import Smartphone

# Объявляем переменную catalog
catalog = []

# Наполняем список пятью разными экземплярами класса Smartphone
catalog.append(Smartphone("Apple", "iPhone 16 Pro Max", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79007654321"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79009876543"))
catalog.append(Smartphone("Google", "Pixel 6", "+79003456789"))
catalog.append(Smartphone("OnePlus", "9 Pro", "+79004567890"))

# Цикл, который печатает весь каталог
for smartphone in catalog:
    print(smartphone.info())
