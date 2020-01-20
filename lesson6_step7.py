from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    input1 = browser.find_element_by_css_selector('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_css_selector('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_css_selector('city')
    input3.send_keys("Smolensk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
print(elements)