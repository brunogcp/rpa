from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("usd to brl")
search_box.send_keys(Keys.RETURN)

time.sleep(5) # Aguarda o carregamento da página
rate = driver.find_element(By.CSS_SELECTOR, "#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt.GDBPqd > span.DFlfde.SwHCTb").text
print(f"Cotação do Dólar para Real: {rate}")
driver.quit()
