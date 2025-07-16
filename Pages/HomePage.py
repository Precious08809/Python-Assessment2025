from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    lbl_welcome_xpath="//*[contains(text(), 'SPORT')]"

    def __init__(self, driver):
        self.driver = driver

    def verifySportIsDisplayed(self):
        wait=WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.lbl_welcome_xpath)))
        element.is_displayed()