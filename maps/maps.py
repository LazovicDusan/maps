from selenium.webdriver import Firefox
import time

url = "https://www.google.rs/maps/@44.7933455,20.5005552,12.76z"

driver = Firefox()
driver.implicitly_wait(5)
driver.get(url)
driver.maximize_window()

_directions = "//button[@id='searchbox-directions']"
_start_location = "//div[@id='sb_ifc51']//input[@class='tactile-searchbox-input']"
_end_location = "//div[@id='sb_ifc52']//input[@class='tactile-searchbox-input']"
_search_button = "//div[@id='directions-searchbox-1']//button[@class='searchbox-searchbutton']"
_info1 = "//div[@id='section-directions-trip-0']//div[@jstcache = '1169']"
_info2 = "//div[@id='section-directions-trip-1']//div[@jstcache = '1169']"
_info3 = "//div[@id='section-directions-trip-2']//div[@jstcache = '1169']"

whereToStart = "Beograd"
whereToGo = "Guca"

directionButton = driver.find_element_by_xpath(_directions)
directionButton.click()

startLocation = driver.find_element_by_xpath(_start_location)
endLocation = driver.find_element_by_xpath(_end_location)
startLocation.send_keys(whereToStart)
endLocation.send_keys(whereToGo)

searchButton = driver.find_element_by_xpath(_search_button)
searchButton.click()

time.sleep(5)

length1 = driver.find_element_by_xpath(_info1).get_attribute("innerHTML")
length2 = driver.find_element_by_xpath(_info2).get_attribute("innerHTML")
length3 = driver.find_element_by_xpath(_info3).get_attribute("innerHTML")

list = [int(length1.replace(" km", "")), int(length2.replace(" km", "")), int(length3.replace(" km", ""))]

index = 0
min = 1000
for elem in range(len(list)):
    if list[elem] < min:
        min = list[elem]
        index = elem + 1

print("Shortest road is " + str(index) + ", with distance of " + str(min) + "km.")

driver.quit()



