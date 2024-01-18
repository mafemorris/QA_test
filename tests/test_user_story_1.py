from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
# import pytest

def test_search_cruises(driver_carnival):
    try:
        driver_carnival.find_element(By.XPATH, "//button[@aria-label='Close offer Button']//img").click()
    except:
        print("pop up closed")
    driver_carnival.find_element(By.XPATH, "//a[@id='cdc-destinations']").click()
    time.sleep(2)
    driver_carnival.find_element(By.XPATH, "//button[@aria-label='The Bahamas ']").click()

    location_element = driver_carnival.find_elements(By.XPATH, "//button[@aria-label='The Bahamas selected']")
    assert len(location_element) == 1, "The element does not exist."

    driver_carnival.find_element(By.XPATH, "//a[@id='cdc-durations']").click()
    driver_carnival.find_element(By.XPATH, "//button[@aria-label='6 - 9 Days ']").click()
    
    duration_element = driver_carnival.find_elements(By.XPATH, "//button[@aria-label='6 - 9 Days selected']")
    assert len(duration_element) == 1, "The element does not exist."

    driver_carnival.find_element(By.CSS_SELECTOR, "a[class='cdc-filters-search-cta']").click()
    time.sleep(2)

    cruise_grid = driver_carnival.find_elements(By.XPATH, '//*[@id="mainContent"]/div/div[3]')
    # this element exists if the xpath is correct, given that the element is a grid.
    assert len(cruise_grid) == 1, "The element is not a grid."

def test_sorted_by_price(driver_carnival_cruise):

    assert driver_carnival_cruise.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/select/option[1]').is_selected()

    last_value = 0
    for i in range(1,5):
        value1 = driver_carnival_cruise.find_element(By.XPATH, f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[{i}]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]").text
        value1_num = int(value1.replace("\n*","").replace(",",""))
        assert last_value <= value1_num, "The values are not sorted low to high."
        last_value = value1_num
    for i in range(1,5):
        value2 = driver_carnival_cruise.find_element(By.XPATH, f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[{i}]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]").text
        value2_num = int(value2.replace("\n*","").replace(",",""))
        assert last_value <= value2_num, "The values are not sorted low to high."
        last_value = value2_num

def test_sorted_by_price_h_to_l(driver_carnival_cruise):

    select = Select(driver_carnival_cruise.find_element(By.XPATH, "//select[@aria-label='Sort By:']"))
    select.select_by_visible_text('High to Low')

    assert driver_carnival_cruise.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/select/option[2]').is_selected()

    last_value = 0
    for i in range(4,1,-1):
        value2 = driver_carnival_cruise.find_element(By.XPATH, f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[{i}]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]").text
        value2_num = int(value2.replace("\n*","").replace(",",""))
        assert last_value <= value2_num, "The values are not sorted high to low."
        last_value = value2_num
    for i in range(4,1,-1):
        value1 = driver_carnival_cruise.find_element(By.XPATH, f"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[{i}]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]").text
        value1_num = int(value1.replace("\n*","").replace(",",""))
        assert last_value <= value1_num, "The values are not sorted high to low."


def test_filtered_by_price_slide(driver_carnival_cruise):
    driver_carnival_cruise.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[4]/button/div[2]').click()
    time.sleep(2)
    slider = driver_carnival_cruise.find_element(By.XPATH, "//span[@class='MuiSlider-root MuiSlider-colorPrimary MuiSlider-sizeMedium css-w3y6kt']")
    right = driver_carnival_cruise.find_element(By.XPATH, "//div[@class='ReactModalPortal']//span[4]")
    left = driver_carnival_cruise.find_element(By.XPATH, "//div[@class='ReactModalPortal']//span[3]")
    original_val = [int(val.get_attribute("value").replace("$", "").replace(",","")) for val in driver_carnival_cruise.find_elements(By.CLASS_NAME, "sc-epYGdz.cKWGvb")]
    move = webdriver.ActionChains(driver_carnival_cruise)
    move.click_and_hold(right).move_by_offset(-0.5 * slider.size['width'], 0).release().perform()
    time.sleep(2)
    move.click_and_hold(left).move_by_offset(0.2 * slider.size['width'], 0).release().perform()
    time.sleep(2)

    current_val = [int(val.get_attribute("value").replace("$", "").replace(",","")) for val in driver_carnival_cruise.find_elements(By.CLASS_NAME, "sc-epYGdz.cKWGvb")]
    assert current_val[0] > original_val[0]
    assert current_val[1] < original_val[1]


# @pytest.mark.parametrize("left, right", [('500', '700'),]) #('1200', '1500')])
# def test_filtered_by_price_box(driver_carnival_cruise, left, right):
#     driver_carnival_cruise.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[4]/button/div[2]').click()
#     time.sleep(2)

#     left_box, right_box = driver_carnival_cruise.find_elements(By.CLASS_NAME, "sc-epYGdz.cKWGvb")
    
#     driver_carnival_cruise.execute_script("arguments[0].setAttribute('value', arguments[1])",left_box, left)
#     driver_carnival_cruise.execute_script("arguments[0].setAttribute('value', arguments[1])",right_box, right)
#     left_box.send_keys(left)
#     right_box.send_keys(right)
#     time.sleep(5)

#     current_val = [val.get_attribute("value").replace("$", "").replace(",","") for val in driver_carnival_cruise.find_elements(By.CLASS_NAME, "sc-epYGdz.cKWGvb")]
#     assert current_val[0] == left
#     assert current_val[1] == right


# @pytest.mark.parametrize("wrong", [('1.00'), ('1!'), ('4='), ('4,0')])
# def test_filtered_by_price_box_fail(driver_carnival_cruise, wrong):
#     driver_carnival_cruise.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[2]/div[4]/button/div[2]').click()
#     time.sleep(2)

#     text_boxes = driver_carnival_cruise.find_elements(By.CLASS_NAME, "sc-epYGdz.cKWGvb")
#     original_val = [int(val.get_attribute("value").replace("$", "").replace(",","")) for val in text_boxes]
    
#     text_boxes[0].send_keys(wrong)
#     text_boxes[1].send_keys(wrong)

#     current_val = [int(val.get_attribute("value").replace("$", "").replace(",","")) for val in driver_carnival_cruise.find_elements(By.CLASS_NAME, "sc-epYGdz.cKWGvb")]
#     assert current_val[0] == original_val[0]
#     assert current_val[1] == original_val[1]