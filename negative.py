from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
import time
import os

d = webdriver.Chrome()
wait = WebDriverWait(d, 2)
act = ActionChains(d)

negative = r"skilltest-dcso\report\negative"

d.fullscreen_window()
key = [
        "daiwndoanowdno", "haduh salah", "Ai"
    ]

print("Running Search test")

d.get("https://indonesiaindicator.com/careers")
d.fullscreen_window()

try:
        
    wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR , "input[placeholder='Search Job...']"))
        )

    os.makedirs(negative, exist_ok=True)
        
    act.send_keys(Keys.PAGE_DOWN).perform()

    send =d.find_element(By.CSS_SELECTOR , "input[placeholder='Search Job...']")

    assert send.is_displayed()


    for  k,i in enumerate(key):
        send =d.find_element(By.CSS_SELECTOR , "input[placeholder='Search Job...']")

        send.clear()
            
        send.send_keys(i)
        time.sleep(2)
        try:
            text = d.find_element(By.CSS_SELECTOR , ".text-gray-500.text-lg").text
            print(text)
        except:
            reslt = d.find_elements(By.XPATH, "//h4")

            time.sleep(2)

            for r in reslt:
                title = r.text.strip().lower()
                if title == "we're looking for talented people":
                    continue
                print(f"you search {i} and output {title}")
                assert i.lower() in title, f"{i} not found in title {title}"

                
        d.save_screenshot(f"{negative}//{k}.png")

    print(f"png saved in {negative}")
    print("test completed")

except Exception as e:
    print("error", e)

