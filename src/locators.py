class HomePageLocators:
    WELFARE_TAB = "//div[@data-cname='index']//div[text()='福利任務']/.."
    CDK_TAB     = "//div[@data-cname='index']//div[text()='CDK']/.."  
    TONGREN_TAB = "//span[text()='同人']"


class WelfareLocators:
    TASK_PANEL_INDICATOR = "//div[contains(text(), '每日任務')]|//div[contains(text(), '瀏覽5個貼文')]"
    SIGNED_TEXT = "//div[text()='已簽到' or text()='已領取']"
    SIGNED_VISUAL = "//i[contains(@class, 'bg-[var(--fill-1-60)]')]"
    BROWSE_PROGRESS = "//div[contains(., '瀏覽5個貼文')]//div[text()='5 / 5']"
    LIKE_PROGRESS = "//div[contains(., '按讚5個貼文')]//div[text()='5 / 5']"
    CHECKIN_BUTTON = "//div[text()='簽到' or text()='領取每日福利']/.. | //div[contains(text(), '簽到') or text()='領取']"


class PostLocators:
    POST_IMAGES = "//img[contains(@class, 'object-cover')]"
    LIKE_CONTAINER = "//*[@data-cname='like']"
    UNLIKED_SVG = ".//*[contains(@clip-path, 'clip0_3_476')]"
    FILL_NONE = ".//*[contains(@fill, 'none') or @fill='']"
    BACK_BUTTON = "//*[local-name()='svg' and .//*[local-name()='clipPath' and @id='clip0_3949_49548']]"


class CdkPageLocators:
    PAGE_INDICATOR = "//div[text()='CDKey']"  
    RECOMMENDED_ROWS = "//div[contains(@class, 'cdk-box')]/div[contains(@class, 'py-[10px]')]"
    CDK_CODE_TEXT    = ".//div[contains(@class, 'text-[color:var(--other-6)]')]"