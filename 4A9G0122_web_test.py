# 4A9G0122_web_test
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://flipclass.stust.edu.tw/")

account_field = driver.find_element(By.NAME, "account")
password_field = driver.find_element(By.NAME, "password")

account_field.send_keys("******")
password_field.send_keys("******")

login_button = driver.find_element(By.CSS_SELECTOR, ".btn-lg")
login_button.click()

time.sleep(2)
element = driver.find_element(By.LINK_TEXT, "軟體工程_四技資工三乙")
driver.execute_script("arguments[0].click();", element)

time.sleep(1)
homework_link = driver.find_element(
    By.XPATH, '//a[contains(@href, "/course/homeworkList")]'
)
homework_link.click()

time.sleep(1)
link_element = driver.find_element(
    By.LINK_TEXT, "[加分題]測試網頁，在這裡自動上傳一個作業，並自動標註學號姓名，與自動上傳你的python code，自動繳交送出"
)
parent_element = link_element.find_element(By.XPATH, "..")  # 获取元素的父元素
parent_element.click()

time.sleep(1)
button = driver.find_element(By.XPATH, '//a[@data-modal-title="交作業"]')
button.click()

time.sleep(5)
my_iframe = driver.find_element(By.XPATH, '//iframe[@class="fs-modal-iframe"]')
driver.switch_to.frame(my_iframe)
iframe2 = driver.find_element(
    By.XPATH, '//iframe[@class="cke_wysiwyg_frame cke_reset"]'
)
driver.switch_to.frame(iframe2)

text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//body[@class='cke_editable cke_editable_themed cke_contents_ltr cke_show_borders']",
        )
    )
)
text.click()
text.send_keys("4a9g0122陳冠霖")

driver.switch_to.default_content()
driver.switch_to.frame(my_iframe)

hw = driver.find_element(
    By.XPATH, '//div[@class="fs-form-control form-inline "]/button'
)
hw.click()

sav = driver.find_element(By.XPATH, '//input[@type="file"]')
sav.send_keys(r"C:\Users\88690\Desktop\4A9G0122_web_test.py")


time.sleep(5)
bu = driver.find_element(By.XPATH, '//button[@class="close"]')
bu.click()

time.sleep(5)
Button = driver.find_element(By.XPATH, '//button[@class="btn btn-success"]')
Button.click()
