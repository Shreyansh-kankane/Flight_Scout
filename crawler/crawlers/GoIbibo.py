from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random


arrayofFlight=[]

def GoIbibo(source,destination,adults,children,infant,date,month,year):
    try:
        
        print("GoIbibo")
        options = webdriver.ChromeOptions()

        options.add_argument("--ignore-certificate-errors")
        # options.add_argument("--headless")
        options.add_argument(f"--window-size=1920,1800")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        userAgent=["53","97","125","45","74"]
        random_integer = random.randint(0, 4)
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147."+userAgent[random_integer]+" Safari/537.36")

        service = Service(executable_path='chromedriver.exe')

        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.goibibo.com/flights/air-"+source+"-"+destination+"-"+year+month+date+"--"+adults+"-"+children+"-"+infant+"-E-D/")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(30)
        original_window = driver.current_window_handle



        for i in range(5):
            flightName=driver.find_elements(By.XPATH,'//div[@class="srp-card-uistyles__CardLeft-sc-3flq99-5 gOROft"]')

            departureTime=driver.find_elements(By.XPATH,'//span[@class="srp-card-uistyles__Time-sc-3flq99-15 iHpsco padT10 f600"]')

            arrivalTime=driver.find_elements(By.XPATH,'//span[@class="srp-card-uistyles__Time-sc-3flq99-15 iHpsco f500  padT10"]')

            priceTag=driver.find_elements(By.XPATH, '//div[@class="srp-card-uistyles__Price-sc-3flq99-17 kxwFaC alignItemsCenter dF f600"]')

            viewPriceTag=driver.find_elements(By.XPATH, '//button[@class="srp-card-uistyles__BookButton-sc-3flq99-21 gtPjNk dF justifyCenter alignItemsCenter f600"]')

            flightDetails={}
            flightDetails["source"]="GoIbibo"
            flight=flightName[i].text.split("\n")[0]
            flightDetails["flightName"]=flight
            print(flight)
            deptTime=departureTime[i].text
            flightDetails["deptTime"]=deptTime
            arrTime=arrivalTime[i].text
            flightDetails["arrivalTime"]=arrTime
            price=priceTag[i].text.split("\n")[0].split(" ")[0].split(",")
            price="".join(price)
            flightDetails["price"]=price
            viewPriceTag[i].click()
            time.sleep(5)
            getLinkTag=driver.find_elements(By.XPATH,'//input[@class="srp-card-uistyles__Fltbook-sc-3flq99-35 hqAmOx f600 widthF105"]')
            time.sleep(10)
            getLinkTag[0].click()
            time.sleep(20)
            if(len(driver.window_handles)>=2):
                for window_handle in driver.window_handles:
                    if(window_handle!=original_window):
                        driver.switch_to.window(window_handle)
                        flightDetails["URL"]=driver.current_url
                        driver.close()
                arrayofFlight.append(flightDetails)
                driver.switch_to.window(original_window)
                time.sleep(2)
                viewPriceTag[i].click()
                time.sleep(10)
            else:
                arrayofFlight.append(flightDetails)
                driver.back()
                time.sleep(30)

        return arrayofFlight
                    
    finally:
        driver.quit()
        Ixigo(source,destination,adults,children,infant,date,month,year)