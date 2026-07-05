import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from locators import HomePageLocators, WelfareLocators, PostLocators, CdkPageLocators
from notifier import send_discord_message

class BotTasks:
    def __init__(self, browser):
        self.browser = browser
        self.driver = browser.driver
        self.wait = browser.wait

    def run_cdk_task(self):
        self.driver.get("https://www.blablalink.com/?lang=zh-TW")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
        self.browser.load_cookies()
        self.driver.refresh()
        
        cdk_tab = self.wait.until(EC.presence_of_element_located((By.XPATH, HomePageLocators.CDK_TAB)))
        self.browser.safe_js_click(cdk_tab)
        self.wait.until(EC.presence_of_element_located((By.XPATH, CdkPageLocators.PAGE_INDICATOR)))
        time.sleep(3)

        success_list = []
        rows = self.driver.find_elements(By.XPATH, CdkPageLocators.RECOMMENDED_ROWS)
        for row in rows:
            btns = row.find_elements(By.XPATH, ".//div[text()='兌換']")
            if btns:
                code = "未知序號"
                try:
                    code = row.find_element(By.XPATH, CdkPageLocators.CDK_CODE_TEXT).text.strip()
                except:
                    pass
                self.browser.safe_js_click(btns[0])
                success_list.append(code)
                time.sleep(2)

        if success_list:
            send_discord_message(f"🎁 **[BlablaLink CDK報告]** 已成功點擊兌換序號: {', '.join(success_list)}")

    def run_welfare_task(self):
        self.driver.get("https://www.blablalink.com/?lang=zh-TW")
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
        tab = self.wait.until(EC.presence_of_element_located((By.XPATH, HomePageLocators.WELFARE_TAB)))
        self.browser.safe_js_click(tab)
        self.wait.until(EC.presence_of_element_located((By.XPATH, WelfareLocators.TASK_PANEL_INDICATOR)))
        time.sleep(2)

        signed = len(self.driver.find_elements(By.XPATH, WelfareLocators.SIGNED_TEXT)) > 0 or \
                 len(self.driver.find_elements(By.XPATH, WelfareLocators.SIGNED_VISUAL)) > 0
        
        if signed and len(self.driver.find_elements(By.XPATH, WelfareLocators.BROWSE_PROGRESS)) > 0 and \
           len(self.driver.find_elements(By.XPATH, WelfareLocators.LIKE_PROGRESS)) > 0:
            send_discord_message("🎉 **[BlablaLink 狀態報告]** 今日所有任務皆已完成。")
            return True

        if not signed:
            try:
                btn = self.driver.find_element(By.XPATH, WelfareLocators.CHECKIN_BUTTON)
                self.browser.safe_js_click(btn)
                time.sleep(2)
            except:
                pass
        return False

    def run_like_task(self, max_attempts=40):
        self.driver.get("https://www.blablalink.com/?lang=zh-TW")
        tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, HomePageLocators.TONGREN_TAB)))
        tab.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, PostLocators.POST_IMAGES)))
        
        liked = 0
        idx = 0
        while liked < 5 and idx < max_attempts:
            posts = self.driver.find_elements(By.XPATH, PostLocators.POST_IMAGES)
            if idx >= len(posts):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(3)
                posts = self.driver.find_elements(By.XPATH, PostLocators.POST_IMAGES)
                if idx >= len(posts): break
            
            post = posts[idx]
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", post)
            time.sleep(1)
            
            try:
                post.click()
                btn = self.wait.until(EC.presence_of_element_located((By.XPATH, PostLocators.LIKE_CONTAINER)))
                time.sleep(0.5)
                if len(btn.find_elements(By.XPATH, PostLocators.UNLIKED_SVG)) > 0 or \
                   len(btn.find_elements(By.XPATH, PostLocators.FILL_NONE)) > 0:
                    self.driver.execute_script("arguments[0].click();", btn)
                    liked += 1
                    time.sleep(2)
            except:
                pass
            
            try:
                back = self.wait.until(EC.element_to_be_clickable((By.XPATH, PostLocators.BACK_BUTTON)))
                back.click()
                self.wait.until(EC.presence_of_element_located((By.XPATH, PostLocators.POST_IMAGES)))
            except:
                self.driver.back()
                self.wait.until(EC.presence_of_element_located((By.XPATH, PostLocators.POST_IMAGES)))
            idx += 1
            
        msg = f"🎉 **[BlablaLink 狀態報告]** 成功！今日 5 個點讚與瀏覽任務已全數達成！" if liked >= 5 else \
              f"ℹ️ **[BlablaLink 狀態報告]** 每日任務結束。共查看 {idx} 篇貼文，點讚 {liked} 個。"
        send_discord_message(msg)