import allure

from Utils.readProperties_Base import ReadConfig_Base


class Test_Formula1Results:
    url= ReadConfig_Base().getURL()
    def test_verifyFormula1Results(self, setup):

        self.driver = setup
        self.driver.get(self.url)

        # Assuming there's a method to verify results on the page
        # This is a placeholder for actual verification logic
        #assert "Results" in self.driver.title, "Formula 1 Results page did not load correctly"

       # allure.attach(self.driver.get_screenshot_as_png(), name="Formula 1 Results Page",
                   #   attachment_type=allure.attachment_type.PNG)

        self.driver.quit()