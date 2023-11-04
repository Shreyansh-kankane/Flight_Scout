from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


arrayofFlight=[]
def Yatra(source,destination,adults,children,infant,date,month,year):
    try:
        
        print("Yatra")
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
            flightDetails["source"]="Yatra"
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147."+userAgent[i]+" Safari/537.36")

            service = Service(executable_path='chromedriver.exe')
            startTime = time.time()

            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://flight.yatra.com/air-search-ui/dom2/trigger?type=O&viewName=normal&flexi=0&noOfSegments=1&origin="+source+"&originCountry=IN&destination="+destination+"&destinationCountry=IN&flight_depart_date="+date+"%2F"+month+"%2F"+year+"&ADT="+adults+"&CHD="+children+"&INF="+infant+"&class=Economy&source=fresco-home&unqvaldesktop=1405365457219")
            
            time.sleep(10)
            screen_width = driver.execute_script("return window.innerWidth;")
            x_coordinate = 10  
            y_coordinate = 10  

            action = ActionChains(driver)
            action.move_by_offset(x_coordinate, y_coordinate).click().perform()
            
            flightdetails=driver.find_elements(By.XPATH,'//div[@class="tuple"]')[i]
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", flightdetails)
            time.sleep(10)
            flightName=driver.find_elements(By.XPATH,'//div[@class="fs-13 airline-name no-pad col-8"]')[i]
            flight=flightName.text
            newList=flight.split("\n")
            flightname=newList[0]
            flightDetails["flightName"]=flightname

            departureTime=driver.find_elements(By.XPATH,'//div[@autom="departureTimeLabel"]')[i]
            deptTime=departureTime.text.split("/n")[0]
            flightDetails["deptTime"]=deptTime

            arrivalTime=driver.find_elements(By.XPATH,'//p[@autom="arrivalTimeLabel"]')[i]
            arrtime=arrivalTime.text.split("/n")[0]
            flightDetails["arrivalTime"]=arrtime


            priceTag=driver.find_elements(By.XPATH, '//div[@class="i-b tipsy fare-summary-tooltip fs-18"]')[i]
            price=priceTag.text.split("\n")[0].split(" ")[0].split(",")
            price="".join(price)
            flightDetails["price"]=price
            buttonTag=driver.find_elements(By.XPATH,'//button[@autom="morefares"]')[i]
            if(buttonTag.text=="View Fares"):
                    buttonTag.click()
                
                    bookTag=driver.find_elements(By.XPATH,'//button[@autom="booknow"]')[0]
                    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' });", bookTag)
                    time.sleep(10)
                    bookTag.click()
                    time.sleep(30)
                    flightDetails["URL"]=driver.current_url
            else:
                    buttonTag.click()
                    time.sleep(30)
                    flightDetails["URL"]=driver.current_url
            arrayofFlight.append(flightDetails)
            driver.close()
            i+=1
        return arrayofFlight
        

    finally:
        driver.quit()