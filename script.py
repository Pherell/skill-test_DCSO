from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select

import time
import os

d = webdriver.Chrome()
wait = WebDriverWait(d, 2)
act = ActionChains(d)

# Path Penyimpanan Screenshot
accord = r"skilltest-dcso\report\menu\accord"
search = r"skilltest-dcso\report\search"
navbar = r"skilltest-dcso\report\menu\navbar"
sosmed = r"skilltest-dcso\report\sosmed"
news = r"skilltest-dcso\report\news"
filt = r"skilltest-dcso\report\filter"
accord_prod = r"skilltest-dcso\report\menu\accord_production"

#TEST SEARCH DI CAREERS

def test_search():
    key = [
        "AI", "Full", "analyst", "engine", "strat", 
    ]

    print("Running Search test")

    d.get("https://indonesiaindicator.com/home")
    d.fullscreen_window()

    try:
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR , "div[class='max-w-7xl mx-auto'] li:nth-child(5) a:nth-child(1)"))
        )
        d.find_element(By.CSS_SELECTOR , "div[class='max-w-7xl mx-auto'] li:nth-child(5) a:nth-child(1)").click()
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR , "input[placeholder='Search Job...']"))
        )

        os.makedirs(search, exist_ok=True)
        
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

                
            d.save_screenshot(f"{search}//{k}.png")

        print(f"png saved in {search}")
        print("test completed")

    except Exception as e:
        print("error", e)


#TEST MENU DI NAVBAR

def test_menu_nav():

    link = [
        "div[class='max-w-7xl mx-auto'] li:nth-child(1) a:nth-child(1)",
        "div[class='max-w-7xl mx-auto'] li:nth-child(2) a:nth-child(1)",
        "div[class='max-w-7xl mx-auto'] li:nth-child(3) a:nth-child(1)",
        "div[class='max-w-7xl mx-auto'] li:nth-child(4) a:nth-child(1)",
        "div[class='max-w-7xl mx-auto'] li:nth-child(5) a:nth-child(1)",
        "div[class='max-w-7xl mx-auto'] li:nth-child(6) a:nth-child(1)",
    ]

    print("Running Test Menu Navbar")

    os.makedirs(navbar, exist_ok=True)

    d.get("https://indonesiaindicator.com/home")
    d.fullscreen_window()

    for i, k in enumerate(link):
        try:
            wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, k))
            )
            d.find_element(By.CSS_SELECTOR, k).click()

            title = d.find_element(By.CSS_SELECTOR, k).text.lower()
            space_fix = title.replace(" ", "-")

            d.find_element(By.CSS_SELECTOR, k).click()

            time.sleep(2)

            cur = d.current_url

            if space_fix.lower() in cur.lower():
                print(f"text {space_fix} To url {cur}")
                assert space_fix in cur, f"text {space_fix} To url {cur}"
            time.sleep(2)
            d.save_screenshot(f"{navbar}//screenshot_{i}.png")
            

        except Exception as e:
            print("error" , e)
    
    print(f"png saved in {navbar}")
    print(f"test completed")


#TEST MENU ACCORDION DI /HOME

def test_menu_accord():
    
    link = [
        "div[id='accordion-container-piramida'] div:nth-child(1) div:nth-child(1)",
        "div[class='col-lg-5 col-md-6'] div:nth-child(2) div:nth-child(1)",
        "div[class='elmdd8aabdb0eb2eeef84ef0b2872503b65'] div:nth-child(3) div:nth-child(1)",
    ]
    
    print("Running Test Menu accordion")

    d.get("https://indonesiaindicator.com/home")

    d.fullscreen_window()
    
    time.sleep(2)

    os.makedirs(accord, exist_ok=True)

    element = d.find_element(By.CSS_SELECTOR , ".row.items-center.g-3.mt-10")

    act.move_to_element(element).perform()

    
    for i in link:
        exist = d.find_element(By.CSS_SELECTOR , i)
        assert exist.is_displayed()

    for i, k in enumerate(link):
        try:
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR , k))
            )
            d.find_element(By.CSS_SELECTOR , k).click()
            time.sleep(2)
            d.save_screenshot(f"{accord}//screen_shot{i}.png")

        except Exception as e:
            print("error" , e)
    
    print(f"png saved in {accord}")
    print("test completed")



#TEST MENU ACCORDION DI PRODUK

def test_menu_in_product():
    link1 = [
        "div[class='elm8f2df7e0d418e91881dfa6f49d12d250'] div[id='accordion-container-piramida'] div:nth-child(1) div:nth-child(1)",
        "div[class='elm8f2df7e0d418e91881dfa6f49d12d250'] div[class='col-lg-5 col-md-6'] div:nth-child(2) div:nth-child(1)",
        "div[class='elm8f2df7e0d418e91881dfa6f49d12d250'] div:nth-child(3) div:nth-child(1)",
    ]
    
    link2 = [
        "div[class='elm1b101f93fb32c3ee831852f0d1038165'] div[id='accordion-container-piramida'] div:nth-child(1) div:nth-child(1)",
        "div[class='elm1b101f93fb32c3ee831852f0d1038165'] div[class='col-lg-5 col-md-6'] div:nth-child(2) div:nth-child(1)",
        "div[class='elm1b101f93fb32c3ee831852f0d1038165'] div:nth-child(3) div:nth-child(1)",
        "div[class='elm1b101f93fb32c3ee831852f0d1038165'] div:nth-child(4) div:nth-child(1)",
    ]

    link3 = [
        "div[class='elm0368f820c18c0988d295c654012752fe'] div[id='accordion-container-piramida'] div:nth-child(1) div:nth-child(1)",
        "div[class='elm0368f820c18c0988d295c654012752fe'] div[class='col-lg-5 col-md-6'] div:nth-child(2) div:nth-child(1)",
    ]

    print("Running Test Menu accordion in product")
    d.get("https://indonesiaindicator.com/product")

    d.fullscreen_window()

    print("starting accord menu test in product tab")

    os.makedirs(accord_prod, exist_ok=True)

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR , "div[class='elm8f2df7e0d418e91881dfa6f49d12d250'] div[class='row items-center g-3 mt-10']"))
    )

    element = d.find_element(By.CSS_SELECTOR , "div[class='elm8f2df7e0d418e91881dfa6f49d12d250'] div[class='row items-center g-3 mt-10']")
    act.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()


    time.sleep(3)
    print("start accord 1")
    for i, k in enumerate(link1):
        try:
            exist = d.find_element(By.CSS_SELECTOR , k)
            assert exist.is_displayed()
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR , k))
            )
            d.find_element(By.CSS_SELECTOR , k).click()
            time.sleep(2)

            d.save_screenshot(f"{accord_prod}//accord1{i}.png")

            time.sleep(2)

        except Exception as e:
            print("error" , e)

    print("accord menu 1 : completed")

    time.sleep(3)

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR , "div[class='elm1b101f93fb32c3ee831852f0d1038165'] div[class='max-w-7xl mx-auto lg:pb-10 py-lg-15 py-10']"))
    )

    element = d.find_element(By.CSS_SELECTOR , "div[class='elm1b101f93fb32c3ee831852f0d1038165'] div[class='max-w-7xl mx-auto lg:pb-10 py-lg-15 py-10']")
    act.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()

    time.sleep(5)
    print("start accord 2")
    for i, k in enumerate(link2):
        try:
            exist = d.find_element(By.CSS_SELECTOR , k)
            assert exist.is_displayed()
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR , k))
            )
            d.find_element(By.CSS_SELECTOR , k).click()
            time.sleep(2)
            d.save_screenshot(f"{accord_prod}//accord2{i}.png")
            time.sleep(2)
        except Exception as e:
            print("error" , e)

    print("accord menu 2 : completed")

    time.sleep(1)
    element = d.find_element(By.CSS_SELECTOR , "div[class='elm0368f820c18c0988d295c654012752fe'] div[class='row items-center g-3 mt-10']")
    act.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()
    
    print("start accord 3")
    time.sleep(5)
    for i, k in enumerate(link3):
        try:
            exist = d.find_element(By.CSS_SELECTOR , k)
            assert exist.is_displayed()
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR , k))
            )
            d.find_element(By.CSS_SELECTOR , k).click()
            time.sleep(2)
            d.save_screenshot(f"{accord_prod}//accord3{i}.png")
            time.sleep(2)

        except Exception as e:
            print("error" , e)

    print("accord menu 3 : completed")
    
    print(f"secreenshot saved in {accord_prod}")


# TEST SOSIAL MEDIA DI PALING BAWAH


def test_sosmed():
    
    prev = d.current_window_handle

    link = [
        "div[class='py-5 px-10'] a:nth-child(1) svg",
        "div[class='py-5 px-10'] a:nth-child(2) svg",
        "div[class='py-5 px-10'] a:nth-child(3) svg",
    ]

    expec = [
        "instagram", "x", "linkedin"
    ]

    print("running sosial media test")

    d.get("https://indonesiaindicator.com/home")
    d.fullscreen_window()

    wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='flex justify-between items-center h-full']"))
    )
    time.sleep(2)
    
    element = d.find_element(By.CSS_SELECTOR, "div[class='flex justify-between items-center h-full']")

    assert element is not None

    act.move_to_element(element).send_keys(Keys.END).perform()

    os.makedirs(sosmed, exist_ok=True)

    for k, i in enumerate(link):
        try:

            d.fullscreen_window()

            time.sleep(2)

            d.find_element(By.CSS_SELECTOR , i).click()

            time.sleep(4)

            tabs = d.window_handles
            
            assert len(tabs) > 1, "tab baru tidak terbuka"

            d.switch_to.window(tabs[-1])

            print("opening :" + d.current_url)
                
            assert expec[k] in d.current_url.lower(), f"not opening expected output {expec[k]}|{d.current_url.lower()}"

            d.save_screenshot(f"{sosmed}//screen_shot{k}.png")

            time.sleep(5)

            d.switch_to.window(prev)

            wait.until(
              EC.element_to_be_clickable((By.CSS_SELECTOR , i))
            )
            time.sleep(5)

        except Exception as e:
            print("error" , e)
    
    print(f"png saved in {sosmed}")
    print("test completed")


def test_News():

    link = [
        "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3) > span:nth-child(1)",
        "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3) > span:nth-child(1)",
        "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(7) > div:nth-child(1) > section:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3) > span:nth-child(1)"
    ]

    prev = d.current_window_handle
    
    d.get("https://indonesiaindicator.com/home")
    time.sleep(5)
    element = d.find_element(By.CSS_SELECTOR , ".py-lg-12.py-5.px-10")
    assert element.is_displayed()
    act.move_to_element(element).perform()

    os.makedirs(news, exist_ok=True)
    time.sleep(5)

    for k, i in enumerate(link):
        try:
            d.fullscreen_window()
            time.sleep(4)
            d.find_element(By.CSS_SELECTOR , i).click()
            time.sleep(4)

            tabs = d.window_handles

            assert len(tabs) > 1, "tab baru tidak terbuka"
            d.switch_to.window(tabs[-1])
            print("opening :" + d.current_url)
            
            d.save_screenshot(f"{news}//screen_shot{k}.png")

            time.sleep(5)

            d.switch_to.window(prev)

            wait.until(
              EC.element_to_be_clickable((By.CSS_SELECTOR , i))
            )
            time.sleep(5)
    

        except Exception as e:
            print("error" , e)

    print(f"png saved in {news}")
    print("test completed")

# Test Filter

def test_filter():

    d.get("https://indonesiaindicator.com/careers")
    d.fullscreen_window()

    wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR , "select.dropdown-style.w-full"))
            )

    time.sleep(5)

    os.makedirs(filt, exist_ok=True)
    element = d.find_element(By.CSS_SELECTOR , "select.dropdown-style.w-full")
    act.move_to_element(element).send_keys(Keys.PAGE_DOWN).perform()

    time.sleep(5)
    filter = d.find_element(By.CSS_SELECTOR , "select.dropdown-style.w-full")

    assert filter.is_displayed(), "no filter feature"
    
    select = Select(d.find_element(By.CSS_SELECTOR , "select.dropdown-style.w-full"))
    
    select.select_by_value("AI Researcher")
    
    print("selected AI Researcher")

    try:
        text = d.find_element(By.CSS_SELECTOR , ".text-gray-500.text-lg").text
        print(text)
    except:
        time.sleep(5)
        d.save_screenshot(f"{filt}//screen_shot.png")
        time.sleep(5)

    print(f"png saved in {filt}")
    print(f"Test Completed")

if __name__ == '__main__':

    #print("Web testing script begin")
    #test_menu_nav()
    #test_menu_in_product()
    #test_menu_accord()
    #test_search()
    test_filter()
    #test_sosmed()
    #test_News()
    print("web testing script ended")
    time.sleep(5)
    d.quit