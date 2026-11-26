from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://www.saucedemo.com/")

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    wait.until(EC.url_contains("inventory"))
    print("Login success")

    add_button = wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
    )
    add_button.click()

    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert cart_badge.text == "1"
    print("Cart badge verification passed!")

    cart_button = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
    )

    cart_button.click()

    wait.until(EC.url_contains("cart"))

    product = wait.until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//div[@class='inventory_item_name' and text()='Sauce Labs Bolt T-Shirt']"
            )
        )
    )

    assert product.text == "Sauce Labs Bolt T-Shirt"

    print("Product verification passed!")
    print("ADD TO CART TEST PASSED!")

    driver.save_screenshot("add_to_cart_result.png")

finally:
    driver.quit()
