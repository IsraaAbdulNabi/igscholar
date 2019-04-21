from Models import WebDriver
import sys

def create_driver():
 driverType= sys.argv[1]

 if (driverType.lower() == "chrome"):
     chrome_driver_object = WebDriver.ChromeDriver('./chromedriver')
     driver=chrome_driver_object.driver
 elif(driverType.lower == "firefox"):
     firefox_driver_object=WebDriver.FireFoxDriver('./geckodriver')
     driver= firefox_driver_object.driver
 else:
     print("Not valid driver ")
 return driver


