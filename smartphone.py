class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

    # Метод для получения информации о смартфоне
    def info(self):
        return f"{self.brand} - {self.model}. {self.phone_number}"
