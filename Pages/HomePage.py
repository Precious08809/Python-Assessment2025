from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    lbl_SPORT_xpath = "//*[contains(text(), 'SPORT')]"
    tab_Formula1_xpath = "//span[text()='Formula 1']"
    tab_Results_xpath = "//span[text()='Results']"
    tab_2023_xpath = "//span[text()='2023']"
    tab_lasvegas_xpath = "//span[text()='Las Vegas Grand Prix, Las Vegas Street Circuit']"
    RESULTS_TEXT_XPATH = "//span[@class='ssrcss-1mstwv3-LinkTextContainer eis6szr1' and text()='Results']"
    YEAR_2023_XPATH = "//div[@data-content='2023' and @type='year' and text()='2023']"
    ABU_DHABI_GP_XPATH = "//span[@class='ssrcss-6v626p-DrawerHandleTitle elwr9uk5' and text()='Abu Dhabi Grand Prix, Yas Marina']"
    LAS_VEGAS_GP_XPATH = "//span[@class='ssrcss-6v626p-DrawerHandleTitle elwr9uk5' and text()='Las Vegas Grand Prix, Las Vegas Street Circuit']"

    def __init__(self, driver):
        self.driver = driver

    def verifySportIsDisplayed(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.lbl_welcome_xpath)))
        element.is_displayed()

    def clickFormula1(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_Formula1_xpath)))
        element.click()

    def clickResults(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_Results_xpath)))
        element.click()

    def click2023(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_2023_xpath)))
        element.click()

    def verifyFormula1Text(self):
        pass

    def clickLasVegas(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_lasvegas_xpath)))
        element.click()

    def clickResults(self):
        results_element = self.driver.find_element(By.XPATH, self.RESULTS_TEXT_XPATH)
        results_element.click()

    def clickYear2023(self):
        year_2023_element = self.driver.find_element(By.XPATH, self.YEAR_2023_XPATH)
        year_2023_element.click()

    def clickAbuDhabiGrandPrix(self):
        abu_dhabi_gp_element = self.driver.find_element(By.XPATH, self.ABU_DHABI_GP_XPATH)
        abu_dhabi_gp_element.click()

    def clickLasVegasGrandPrix(self):
        las_vegas_gp_element = self.driver.find_element(By.XPATH, self.LAS_VEGAS_GP_XPATH)
        las_vegas_gp_element.click()
