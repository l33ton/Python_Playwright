import pytest
from utils.data_generator import DataGenerator

gen = DataGenerator()
@pytest.mark.skip_auth
@pytest.mark.parametrize("brand_name, make", [
    ("Audi", "A4"),
    ("Audi", "A6"),
    ("Porsche", "911")])
def test_adding_a_car_to_a_client(logged_in, vehicles_page, brand_name, make):
    # Arrange
    vehicle = gen.generate_vehicle_data(brand_name, make)
    # Act
    vehicles_page.finalize_adding_car_to_a_client(vehicle, brand_name, make)
    # Assert
    vehicles_page.expect_owner_to_have_assigned_car(vehicle)