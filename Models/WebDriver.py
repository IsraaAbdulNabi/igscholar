from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class ChromeDriver():
    def __init__(self,driverPath):
        if (driverPath is None):
            self.path='./chromedriver'
        else:
            self.path = driverPath

        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir= %s" % self.path)
        #options.add_argument("headless")
        options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=options)


class FireFoxDriver():
    def __int__(self,driverPath):
        if (driverPath is None):
            self.path='./chromedriver'
        else:
            self.path = driverPath
        options = webdriver.FirefoxOptions
        options.add_argument("user-data-dir=" + self.path)
        options.add_argument("headless")
        options.add_argument('window-size=1920x1080')
        try:
            self.driver = webdriver.Firefox(executable_path=self.path,firefox_options=options)
        except WebDriverException:
            print("failed to start driver at " + driverPath)
            self.inUse = True  # scraper with no driver is not ready to handle new job
            # traceback.print_exc()



