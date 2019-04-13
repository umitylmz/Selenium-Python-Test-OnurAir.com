from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
print("WAIT LIMIT IS 50 SECS BECAUSE OF THE PROBABILITY OF SLOW INTERNET CONNECTION")
driver.implicitly_wait(50)
driver.get('https://www.onurair.com')




print("SEARCH PARAMETERS")
driver.find_element_by_xpath('(//span[contains(@class,"jcf-select-opener")])[1]').click()
driver.find_element_by_xpath('(//span[contains(.,"Antalya (AYT)")])[4]').click()
driver.find_element_by_xpath('(//span[contains(@class,"jcf-select-opener")])[2]').click()
driver.find_element_by_xpath('(//span[contains(.,"İstanbul Havalimanı (IST)")])[4]').click()
driver.find_element_by_xpath('//input[contains(@placeholder,"Gidiş Tarihi")]').click()
driver.find_element_by_xpath('(//th[@class="next"][contains(.,"›")])[1]').click()
driver.find_element_by_xpath('(//td[@class="day "][contains(.,"25")])[1]').click()
driver.find_element_by_xpath('(//td[@class="day "][contains(.,"28")])[2]').click()
driver.find_element_by_xpath('(//span[contains(@class,"jcf-select-opener")])[4]').click()
driver.find_element_by_xpath('//span[contains(@data-index,"1")]').click()
driver.find_element_by_xpath('//input[contains(@onclick,"ticketSearch()")]').click()
print("SEARCH DONE")





print("FLIGHT SELECTION")
driver.find_element_by_xpath('(//h6[contains(@class,"day__title__date")])[7]').click()
element = driver.find_element_by_xpath('(//h6[contains(@class,"day__title__date")])[13]')
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[1]/div/div[3]/div/div[1]/div[5]/div[1]/div[4]/div[1]/div[3]/div/label/div/div/div[2]/div[1]/div[1]').click()
time.sleep(2)
element = driver.find_element_by_xpath('(//h6[contains(@class,"day__title__date")])[13]')
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath('(//span[contains(@class,"price")])[14]').click()                                     
time.sleep(2)
driver.find_element_by_xpath('//input[contains(@name,"close")]').click()
element = driver.find_element_by_xpath('(//h6[contains(@class,"day__title__date")])[13]')
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath('(//h6[contains(@class,"day__title__date")])[13]').click()
element = driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[1]/div/div[3]/div/div[3]/div[5]/div[1]/div[4]/div[1]/div[3]/div/label/div/div/div[2]/div[1]/div[1]')
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath('/html/body/form/div[3]/div/div/div[1]/div/div[3]/div/div[3]/div[5]/div[1]/div[4]/div[1]/div[3]/div/label/div/div/div[2]/div[1]/div[1]').click()
element = driver.find_element_by_xpath('(//span[contains(@class,"price")])[36]')
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath('(//span[contains(@class,"price")])[36]').click()
time.sleep(2)
driver.find_element_by_xpath('(//input[contains(@id,"close")][@type="submit"])[2]').click()
element = driver.find_element_by_xpath('//input[contains(@name,"btnContinue")]')
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(1)
driver.find_element_by_xpath('//label[@for="lock__price"][contains(.,"Fiyatı Sabitlemek İstiyorum")]').click()
driver.find_element_by_xpath('//input[contains(@name,"btnContinue")]').click()
time.sleep(2)
actions = ActionChains(driver)
actions.send_keys(Keys.ESCAPE)
actions.perform()
print("FLIGHT SELECTION DONE")



print("CUSTOMER INFORMATION")
driver.find_element_by_xpath('//input[contains(@readonly,"readonly")]').click()
driver.find_element_by_xpath('//div[@class="option active"]').click()
driver.find_element_by_xpath('//input[@name="name1"]').send_keys("dd")
driver.find_element_by_xpath('//input[contains(@name,"surname1")]').send_keys("dd")
driver.find_element_by_xpath('//*[@id="nationality1-selectized"]').send_keys("Türkiye (Turkey)")
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath('(//input[@type="text"])[4]').send_keys("5")
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
driver.find_element_by_xpath('(//input[@type="text"])[5]').send_keys("Ocak")
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
driver.find_element_by_xpath('(//input[@type="text"])[6]').send_keys("1996")
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
driver.find_element_by_xpath('//input[contains(@name,"natId1")]').send_keys("61333347910")
driver.find_element_by_xpath('//input[contains(@name,"frst-tel-number0")]').send_keys("5436666666")
driver.find_element_by_xpath('//input[contains(@name,"email0")]').send_keys("dd@gmail.com")
element = driver.find_element_by_xpath('//input[contains(@type,"submit")]')
time.sleep(2)
actions = ActionChains(driver)
actions.move_to_element(element)
actions.perform()
time.sleep(2)
driver.find_element_by_xpath('//input[contains(@type,"submit")]').click()
actions = ActionChains(driver)
actions.send_keys(Keys.ESCAPE)
actions.perform()
print("CUSTOMER INFORMATION DONE")

print("QUIT IN 5 SECS")
time.sleep(10)
driver.quit()

















