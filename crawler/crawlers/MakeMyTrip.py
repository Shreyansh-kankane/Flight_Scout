from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import random   

arrayofFlight=[]
def MakeMyTrip(source,destination,adults,children,infant,date,month,year):
    try:
        print("Make My Trip")
        options = webdriver.ChromeOptions() 
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        userAgent=["21","54","115","15","71"]
        random_integer = random.randint(0, 4)
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147."+userAgent[random_integer]+" Safari/537.36")


        service = Service(executable_path='chromedriver.exe') 
        startTime = time.time()

        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.makemytrip.com/flight/search?tripType=O&itinerary="+source+"-"+destination+"-"+date+"/"+month+"/"+year+"&paxType=A-"+adults+"_C-"+children+"_I-"+infant+"&cabinClass=E&sTime=1698553588105&forwardFlowRequired=true&mpo=&semType=&intl=false")
        time.sleep(25)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


        close=driver.find_element(By.XPATH, '//span[@class="bgProperties icon20 overlayCrossIcon"]')
        close.click()
        time.sleep(5)
        original_window = driver.current_window_handle


        flightName=driver.find_elements(By.XPATH,'//div[@class="makeFlex align-items-center gap-x-10 airline-info-wrapper"]')[:5]

        departureTime=driver.find_elements(By.XPATH,'//div[@class="flexOne timeInfoLeft"]')[:5]

        arrivalTime=driver.find_elements(By.XPATH,'//div[@class="flexOne timeInfoRight"]')[:5]

        priceTag=driver.find_elements(By.XPATH, '//div[@class="blackText fontSize18 blackFont white-space-no-wrap clusterViewPrice"]')[:5]

        viewPriceTag=driver.find_elements(By.XPATH, '//span[@class="customArrow arrowDown"]')[:5]
        
        
        for i in range(len(flightName)):
            flightDetails={}
            flightDetails["source"]="MakeMytrip"
            flight=flightName[i].text.split("\n")[0]
            flightDetails["flightName"]=flight
            print(flight)
            deptTime=departureTime[i].text.split("\n")[0]
            flightDetails["deptTime"]=deptTime
            arrTime=arrivalTime[i].text.split("\n")[0]
            flightDetails["arrivalTime"]=arrTime
            price=priceTag[i].text.split("\n")[0].split(" ")[1].split(",")
            price="".join(price)
            flightDetails["price"]=price
            viewPriceTag[i].click()
            time.sleep(5)
            getLinkTag=driver.find_elements(By.XPATH,'//button[@class="button corp-btn latoBlack buttonPrimary fontSize13  "]')
            getLinkTag[0].click()
            time.sleep(20)
            for window_handle in driver.window_handles:
                if(window_handle!=original_window):
                    driver.switch_to.window(window_handle)
                    flightDetails["URL"]=driver.current_url
                    driver.close()
            arrayofFlight.append(flightDetails)
            driver.switch_to.window(original_window)
            time.sleep(2)
            closeArrowTag=driver.find_element(By.XPATH,'//span[@class="customArrow arrowUp"]').click()
            
    finally:
        print("Error")
        driver.quit()
        return arrayofFlight