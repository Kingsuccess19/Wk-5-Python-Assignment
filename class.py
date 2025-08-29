# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        # Attributes
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
    
    # Method to display phone info
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.battery_life} hours battery life."
    
    # Method to simulate calling
    def make_call(self, number):
        return f"Calling {number} from {self.model}..."
    
    # Method to simulate charging
    def charge(self, hours):
        self.battery_life += hours
        return f"{self.model} charged for {hours}h. Battery life is now {self.battery_life}h."


# Derived Class: SmartphoneWithCamera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        # Inherit attributes from Smartphone
        super().__init__(brand, model, battery_life)
        # New attribute
        self.camera_megapixels = camera_megapixels
    
    # Polymorphic method (redefining behavior)
    def phone_info(self):
        return f"{self.brand} {self.model} - {self.battery_life}h battery, {self.camera_megapixels}MP camera."
    
    # New method for taking a picture
    def take_picture(self):
        return f"📸 {self.model} takes a {self.camera_megapixels}MP photo!"


# Example Usage
phone1 = Smartphone("Nokia", "3310", 72)
phone2 = SmartphoneWithCamera("Apple", "iPhone 15", 20, 48)

# Demonstration
print(phone1.phone_info())
print(phone1.make_call("123-456-7890"))
print(phone1.charge(5))

print("\n---\n")

print(phone2.phone_info())  # Overridden method
print(phone2.make_call("987-654-3210"))
print(phone2.take_picture())

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclasses with their own move() implementations
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("🛥️ Sailing on the water")

# Another example with animals
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def move(self):
        print("🐕 Running around")

class Bird(Animal):
    def move(self):
        print("🐦 Flying high")

class Fish(Animal):
    def move(self):
        print("🐟 Swimming in water")


# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat()]
animals = [Dog(), Bird(), Fish()]

print("=== Vehicles ===")
for v in vehicles:
    v.move()

print("\n=== Animals ===")
for a in animals:
    a.move()
