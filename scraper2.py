from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

product = []
cost = []


driver.get("https://jumia.com.ng")

search = driver.find_element_by_name("q")
search.send_keys("Airpods")
search.send_keys(Keys.RETURN)


driver.implicitly_wait(30)
names = driver.find_elements_by_class_name("name")
prices = driver.find_elements_by_class_name('prc')

for name in names:
    product.append(name.text)

for price in prices:
    cost.append(price.text)


df = pd.DataFrame({'Product Name':product,'Price':cost}) 
df.to_csv('Airpods.csv', index=False, encoding='utf-8')

driver.quit() 