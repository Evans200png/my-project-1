#main class:smartphone
class smartphone:
  def __init__(self, brand, model, price):
    self.brand=brand
    self.model=model
    self.__price=price
  def get_price(self):
    return f"The price of {self.brand} {self.model} is {self.__price}"
  def make_call(self, number):
    return f"Calling {number}..."
  def send_message(self, message):
    return f"Sending message: {message}"

# sub class :smartphone_pro with inheritance features from main class
class smartphone_pro(smartphone):
  def __init__(self, brand, model, price, camera_megapixels, battery_life):
    super().__init__(brand, model, price)
    self.camera_megapixels=camera_megapixels
    self.battery_life=battery_life
  def take_photo(self):
    return f"Capturing a photo of {self.camera_megapixels} megapixels"
  def get_battery_life(self):
    return f"my battery life:{self.battery_life} hours"

#creating objects
phone1 = smartphone("Samsung", "Galaxy S22", 799)
phone2 = smartphone_pro("Apple", "iPhone 14 Pro", 999, 48, 24)

#accessings methods
print(phone1.get_price())  # Encapsulation: Access private attribute safely
print(phone2.get_price())  # Inherited from Smartphone
print(phone2.take_photo())  # Polymorphism: Extra functionality
print(phone2.get_battery_life())  # Specific to SmartPhonePro
print(phone1.make_call("123-456-7890")) #call feature