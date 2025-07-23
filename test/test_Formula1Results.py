import allure
import pytest

from Pages.HomePage import HomePage
from Utils.readProperties_Base import ReadConfig_Base


class Test_Formula1Results:
    url = ReadConfig_Base().getURL()

    @pytest.mark.sanity
    def test_verifyFormula1Results(self, setup):
        self.driver = setup
        self.driver.get(self.url)

    @pytest.mark.Formula1Text
    def test_clickFormula1Results(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.hp = HomePage(self.driver)
        self.hp.verifyFormula1Text()
        self.hp.clickFormula1()
        self.hp.clickResults()  # Click the "Results" element
        allure.attach(self.driver.get_screenshot_as_png(), name="Formula 1 Results Page",
                      attachment_type=allure.attachment_type.PNG)
        allure.attach(self.driver.get_screenshot_as_png(), name="Formula 1 Results Page",
                      attachment_type=allure.attachment_type.PNG)
        self.hp.clickYear2023()  # Click the "2023" year element
        allure.attach(self.driver.get_screenshot_as_png(), name="Formula 1 Results Page",
                      attachment_type=allure.attachment_type.PNG)
        self.hp.clickAbuDhabiGrandPrix()  # Click the "Abu Dhabi Grand Prix, Yas Marina" element
        allure.attach(self.driver.get_screenshot_as_png(), name="Abu Dhabi Grand Prix Page",
                      attachment_type=allure.attachment_type.PNG)
        self.hp.clickLasVegasGrandPrix()  # Click the "Las Vegas Grand Prix, Las Vegas Street Circuit" element
        allure.attach(self.driver.get_screenshot_as_png(), name="Las Vegas Grand Prix Page",
                      attachment_type=allure.attachment_type.PNG)





