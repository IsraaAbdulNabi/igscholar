from Models import WebDriver
import sys

def create_driver():

 driverType= sys.argv[1]

 if (driverType.lower() == "chrome"):
     driver= WebDriver.ChromeDriver("./chromedriver").driver
 elif(driverType.lower == "firefox"):
     driver=WebDriver.FireFoxDriver("./geckodriver").driver
 else:
     print("Not valid driver ")

 return driver




create_driver()

