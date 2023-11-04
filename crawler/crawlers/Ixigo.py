from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


arrayofFlight=[]
def Ixigo(source,destination,adults,children,infant,date,month,year):
    try:
        print("Ixigo")
    
        options = webdriver.ChromeOptions()

        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        userAgent=["53","97","125","45","74"]
        i=0
        while i<=4:
            flightDetails={}
            flightDetails["source"]="Ixigo"
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147."+userAgent[i]+" Safari/537.36")

            service = Service(executable_path='chromedriver.exe')
            startTime = time.time()

            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://www.ixigo.com/search/result/flight?from="+source+"&to="+destination+"&date="+date+month+year+"&returnDate=&adults="+adults+"&children="+children+"&infants="+infant+"&class=e&source=Search%20Form")
            time.sleep(30)
            screen_width = driver.execute_script("return window.innerWidth;")
            x_coordinate = 10  
            y_coordinate = 10  

            action = ActionChains(driver)
            action.move_by_offset(x_coordinate, y_coordinate).click().perform()
            
            flightdetails=driver.find_elements(By.XPATH,'//div[@class="c-flight-listing-row-v2"]')[i]
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", flightdetails)
            time.sleep(10)
            flightName=driver.find_elements(By.XPATH,'//a[@class="flight-name"]')[i]
            flight=flightName.text
            flightDetails["flightName"]=flight

            departureTime=driver.find_elements(By.XPATH,'//div[@class="left-wing"]')[i]
            deptTime=departureTime.text.split("\n")[1]
            flightDetails["deptTime"]=deptTime

            arrivalTime=driver.find_elements(By.XPATH,'//div[@class="right-wing"]')[i]
            arrtime=arrivalTime.text.split("\n")[1]
            flightDetails["arrivalTime"]=arrtime

            priceTag=driver.find_elements(By.XPATH, '//div[@class="price"]')[i]
            price=priceTag.text.split("\n")[0].split(" ")[0].split(",")
            price="".join(price)
            flightDetails["price"]=price
            buttonTag=driver.find_elements(By.XPATH,'//div[@class="book-cta"]')[i]
            buttonTag.click()
            time.sleep(30)
            flightDetails["URL"]=driver.current_url

            driver.close()
            arrayofFlight.append(flightDetails)
            i+=1
            
    finally:
        driver.quit()
        return arrayofFlight