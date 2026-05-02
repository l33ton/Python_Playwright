from playwright.sync_api import expect

from constants import VIN_LOCATOR, LICENSE_PLATE_LOCATOR, OWNER_LOCATOR, BRAND_DROPWDOWN_MENU_LOCATOR, \
    MAKE_LOCATOR, ENGINE_TYPE_LOCATOR, YEAR_OF_PRODUCTION_LOCATOR, SEARCH_BY_OWNER_LOCATOR, SEARCH_BUTTON_LOCATOR
from pages.base_page import BasePage

class VehiclesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.vin_input_locator = self.page.locator(VIN_LOCATOR)
        self.license_plate_input_locator = self.page.locator(LICENSE_PLATE_LOCATOR)
        self.owner_input_locator = self.page.locator(OWNER_LOCATOR)
        self.brand_dropdown_menu_locator = self.page.locator(BRAND_DROPWDOWN_MENU_LOCATOR)
        self.make_input_locator = self.page.locator(MAKE_LOCATOR)
        self.engine_type_input_locator = self.page.locator(ENGINE_TYPE_LOCATOR)
        self.year_of_creation_input_locator = self.page.locator(YEAR_OF_PRODUCTION_LOCATOR)
        self.add_client_car_locator = page.get_by_role("button", name="ADD CLIENT CAR")
        self.search_a_car_by_owner_input_locator = page.locator(SEARCH_BY_OWNER_LOCATOR)
        self.search_button_locator = page.locator(SEARCH_BUTTON_LOCATOR)

    def enter_the_information_about_the_car(self, vehicle, make):
        self.vin_input_locator.fill(vehicle["vin"])
        self.license_plate_input_locator.fill(vehicle["license_plate"])
        self.owner_input_locator.fill(vehicle["owner"])
        self.make_input_locator.fill(make)
        self.engine_type_input_locator.fill(vehicle["engine_type"])
        self.year_of_creation_input_locator.fill(vehicle["year_of_creation"])

    def choose_a_brand(self, brand_name):
        self.brand_dropdown_menu_locator.select_option(brand_name)

    def add_car_to_client(self):
        self.add_client_car_locator.click()

    def finalize_adding_car_to_a_client(self, vehicle, brand_name, make):
        self.enter_the_information_about_the_car(vehicle, make)
        self.choose_a_brand(brand_name)
        self.add_car_to_client()

    def search_a_car_by_owner(self, owner):
        self.search_a_car_by_owner_input_locator.fill(owner)
        self.search_button_locator.click()

    def expect_owner_to_have_assigned_car(self, vehicle):
        self.page.reload()
        self.page.wait_for_load_state("networkidle")
        self.search_a_car_by_owner(vehicle["owner"])
        expect(self.page.get_by_text(vehicle["vin"])).to_be_visible(timeout=10000)