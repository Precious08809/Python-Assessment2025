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
        self.hp.clickFormula1Results()
        allure.attach(self.driver.get_screenshot_as_png(), name="Formula 1 Results Page",
                      attachment_type=allure.attachment_type.PNG)





