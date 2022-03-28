import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
def Menu(l):
    for i in range(len(l)):
        print(f"{i+1}. {l[i]}")
    x = input("tapez votre choix: ")
    return x
def main_program(brand_name):
    driver = webdriver.Chrome("D:\developpement\chromedriver.exe")
    driver.get("https://www.automobile.tn/fr")
    driver.find_element(By.CLASS_NAME, "chosen-single").click()
    driver.find_element(By.CLASS_NAME, "chosen-search-input").send_keys(brand_name, Keys.ENTER)
    driver.find_element(By.XPATH, '//*[@id="w1"]/div[4]/input').click()
    time.sleep(10)
    cars = driver.find_elements(By.CLASS_NAME, "versions-item")
    list_cars = []
    for c in cars:
        list_cars.append(c.find_element(By.TAG_NAME, "a").get_attribute('href'))
    for c in list_cars:
        test1 = False
        test2 = False
        driver.get(c)
        try:
            driver.find_element(By.CLASS_NAME, "version-details")
            test1 = True
        except:
            pass
        if (test1 == False):
            try:
                driver.find_element(By.CLASS_NAME, "versions-details")
                test2 = True
            except:
                pass
        if (test1):
            with open(f"{brand_name}.txt", "a", newline='') as file:
                write = csv.writer(file, delimiter=';')
                write.writerow([driver.find_element(By.TAG_NAME, "h3").get_property("innerText"),
                                driver.find_element(By.CLASS_NAME, "version-img").find_element(By.TAG_NAME,"img").get_attribute("src"),
                                driver.find_element(By.CLASS_NAME, "buttons").find_element(By.TAG_NAME,"div").get_property("innerText")])
        elif (test2):
            versions = driver.find_element(By.CLASS_NAME, "versions").find_elements(By.CLASS_NAME, "version")
            prices = driver.find_element(By.CLASS_NAME, "versions").find_elements(By.CLASS_NAME, "price")
            i = 0
            while (i < len(versions)):
                with open(f"{brand_name}.txt", "a", newline='') as file:
                    write = csv.writer(file, delimiter=';')
                    write.writerow([driver.find_element(By.TAG_NAME, "h3").get_property("innerText") + " " + versions[i].get_property("innerText"),
                                    driver.find_element(By.CLASS_NAME, "versions-img").find_element(By.TAG_NAME,"img").get_attribute("src"),
                                    prices[i].get_property("innerText")])
                i += 1
    print("Mission complete")
    driver.quit()

car_list = ['Alfa Romeo', 'Audi', 'BMW', 'BYD', 'Changan', 'Chery', 'Chevrolet', 'Dacia', 'DFSK', 'Dongfeng', 'Faw', 'Fiat', 'Foday', 'Ford', 'Geely', 'Great Wall', 'Haval', 'Honda', 'Huanghai', 'Hyundai', 'Jaguar', 'Jeep', 'KIA', 'Land Rover', 'Mahindra', 'Mercedes-Benz', 'MG', 'Mini', 'Mitsubishi', 'Nissan', 'Opel', 'Peugeot', 'Porsche', 'Renault', 'Seat', 'Skoda', 'Soueast', 'Ssangyong', 'Suzuki', 'Tata', 'Toyota', 'Volkswagen', 'Wallyscar']
brand_name = Menu(car_list)
while brand_name in car_list:
    main_program(brand_name)
    print("another choice ?")
    print("type 0 to exit...")
    brand_name = Menu(car_list)
