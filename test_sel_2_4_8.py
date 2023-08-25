import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/explicit_wait2.html"


def cacl(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    browser.find_element(By.CSS_SELECTOR, "#book").click()

    x_el = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_el.text)

    browser.find_element(By.CSS_SELECTOR, "#answer.form-control").send_keys(cacl(x))

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
