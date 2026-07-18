import json
import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from config import COOKIE_FILE_PATH

class BrowserManager:
    def __init__(self):
        self.driver = None
        self.wait = None
        self._init_driver()

    def _init_driver(self):
        options = uc.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        self.driver = uc.Chrome(version_main=149, options=options)
        self.wait = WebDriverWait(self.driver, 15)

    def load_cookies(self):
        if not os.path.exists(COOKIE_FILE_PATH):
            return False

        with open(COOKIE_FILE_PATH, 'r') as f:
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

                    self.driver.add_cookie(clean_cookie)
                except Exception:
                    continue
        return True

    def safe_js_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({inline: 'center', block: 'nearest'});", element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", element)

    def close(self):
        if self.driver:
            self.driver.quit()