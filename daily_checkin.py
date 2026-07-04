import json
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

def load_cookies(driver, filepath):
    with open(filepath, 'r') as f:
        cookies = json.load(f)
        for cookie in cookies:
            try:
                clean_cookie = {
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'path': cookie.get('path', '/')
                }
                domain = cookie.get('domain', '')
                if domain == '.www.blablalink.com':
                    clean_cookie['domain'] = '.blablalink.com'
                else:
                    clean_cookie['domain'] = domain
                if 'secure' in cookie:
                    clean_cookie['secure'] = cookie['secure']
                if 'httpOnly' in cookie:
                    clean_cookie['httpOnly'] = cookie['httpOnly']
                if 'expiry' in cookie:
                    clean_cookie['expiry'] = int(cookie['expiry'])
                elif 'expirationDate' in cookie:
                    clean_cookie['expiry'] = int(cookie['expirationDate'])
                if 'sameSite' in cookie and cookie['sameSite'] in ['Lax', 'Strict', 'None']:
                    clean_cookie['sameSite'] = cookie['sameSite']

                driver.add_cookie(clean_cookie)
            except Exception as e:
                print(f"無法加入 Cookie: {cookie.get('name')}, 原因: {e}")

def run():
    options = uc.ChromeOptions()
    # options.add_argument("--headless=new")          
    options.add_argument("--no-sandbox")             
    options.add_argument("--disable-dev-shm-usage")  
    options.add_argument("--window-size=1920,1080")
    driver = uc.Chrome(version_main=149, options=options)
    
    try:
        driver.get("https://www.blablalink.com/?lang=zh-TW")
        time.sleep(3) 
        load_cookies(driver, "cookies.json")
        driver.refresh()
        time.sleep(5) 
        wait = WebDriverWait(driver, 15)
        
        try:
            welfare_tab_xpath = "//div[@data-cname='index']//div[text()='福利任務']/.."
            welfare_tab = wait.until(EC.presence_of_element_located((By.XPATH, welfare_tab_xpath)))
            
            driver.execute_script("arguments[0].scrollIntoView({inline: 'center', block: 'nearest'});", welfare_tab)
            time.sleep(1.5)
            driver.execute_script("arguments[0].click();", welfare_tab)
            time.sleep(5) 
            
            # 1. 檢查是否簽到成功
            indicator_xpath = "//i[contains(@class, '-skew-x-[30deg]') and contains(@class, 'bg-[var(--fill-1-60)]')]"
            is_signed_in = len(driver.find_elements(By.XPATH, indicator_xpath)) > 0
            
            # 2. 檢查「瀏覽5個貼文」
            browse_xpath = "//div[i[contains(@class, 'border-[color:var(--line-1)]')] and .//div[contains(text(), '瀏覽5個貼文')]]//div[text()='5 / 5']"
            is_browse_completed = len(driver.find_elements(By.XPATH, browse_xpath)) > 0
            
            # 3. 檢查「按讚5個貼文」
            like_xpath = "//div[i[contains(@class, 'border-[color:var(--line-1)]')] and .//div[contains(text(), '按讚5個貼文')]]//div[text()='5 / 5']"
            is_like_completed = len(driver.find_elements(By.XPATH, like_xpath)) > 0
            
            
            if is_signed_in and is_browse_completed and is_like_completed:
                print("今日所有任務皆已完成。")
                driver.quit()
                return 
            
            if not is_signed_in:
                try:
                    checkin_btn_inside = driver.find_element(By.XPATH, "//div[contains(text(), '簽到') or contains(text(), '領取') or contains(text(), '完成')]")
                    driver.execute_script("arguments[0].click();", checkin_btn_inside)
                    time.sleep(2)
                except Exception:
                    print("⚠️ 未找到內部簽到按鈕。")
            
            driver.get("https://www.blablalink.com/?lang=zh-TW")
            time.sleep(4)
            
        except Exception as rollbar_err:
            print(f"❌ 讀取福利任務進度時發生異常: {rollbar_err}，安全起見，直接切換至常規點讚流程...")

        tongren_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='同人']")))
        tongren_tab.click()
        time.sleep(5) 
        
        liked_count = 0     
        post_index = 0      
        max_attempts = 40   
        
        while liked_count < 5 and post_index < max_attempts:
            print(f"\n👉 正在檢查第 {post_index + 1} 則貼文... (目前已成功點讚: {liked_count} / 5)")       
            posts = driver.find_elements(By.XPATH, "//img[contains(@class, 'object-cover')]")
            if post_index >= len(posts):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                posts = driver.find_elements(By.XPATH, "//img[contains(@class, 'object-cover')]")
                if post_index >= len(posts):
                    print("❌ 已經到達網頁底部或無法載入更多貼文，結束任務。")
                    break
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", posts[post_index])
            time.sleep(1.5) 
            try:
                posts[post_index].click()
                like_container_xpath = "//*[@data-cname='like']"
                like_btn = wait.until(EC.presence_of_element_located((By.XPATH, like_container_xpath)))
                time.sleep(1) 
                is_unliked = len(like_btn.find_elements(By.XPATH, ".//*[contains(@clip-path, 'clip0_3_476')]")) > 0
                
                if is_unliked:
                    driver.execute_script("arguments[0].click();", like_btn)
                    liked_count += 1
                    print(f"❤️ 成功點讚！({liked_count} / 5)")
                    time.sleep(2) 
                else:
                    print("💡 這篇貼文之前就讚過了。")
                        
            except Exception as post_err:
                print(f"操作此貼文時發生異常: {post_err}，嘗試跳過...")
            
            back_btn_xpath = "//*[local-name()='svg' and .//*[local-name()='clipPath' and @id='clip0_3949_49548']]"
            try:
                back_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, back_btn_xpath)))
                back_btn.click()
                time.sleep(2)
            except TimeoutException:
                print("❌ 找不到返回鍵！使用瀏覽器內建後退機制...")
                driver.back()
                time.sleep(3)
            
            post_index += 1
            
        if liked_count >= 5:
            print("\n🎉 成功！今日 5 個全新點讚任務已全數達成！")
        else:
            print(f"\n每日任務結束。今日共查看了 {post_index} 篇貼文，成功點了 {liked_count} 個讚。")
        
    except Exception as e:
        print(f"❌ 主程式發生重大錯誤: {e}")
    finally:
        print("正在關閉瀏覽器...")
        driver.quit()

if __name__ == "__main__":
    run()