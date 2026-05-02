import random

from faker import Faker


class DataGenerator:
    def __init__(self, locale="bg_BG"):
        self.fake = Faker(locale)
        self.existing_owners = ["felix_jackson", "alex_rider", "bella_harper", "chris_oakley", "lucas_morgan"]
        self.existing_engines = ["1.9 TDI", "2.0 TDI", "2.0 TFSI", "3.0 V6"]

    def generate_vehicle_data(self, brand_name, make):
        return {
            "vin": self.fake.bothify(text="WAUZZZ8P4AA######", letters="0123456789"),
            "license_plate": self.fake.bothify(text="CB####BA", letters="0123456789"),
            "owner": random.choice(self.existing_owners),
            "brand": brand_name,
            "make": make,
            "engine_type": random.choice(self.existing_engines),
            "year_of_creation": str(self.fake.random_int(2000, 2026))
        }