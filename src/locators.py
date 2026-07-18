class HomePageLocators:
    INITIAL_BUTTON = "//button[@data-cname='pc-layout-switch']"
    INITIAL_SUB_BUTTON = "//div[contains(@class, 'w-[85%]') and contains(@class, 'h-[50%]') and contains(@class, 'cursor-pointer')]"
    WELFARE_TAB = "//div[@data-cname='index']//div[text()='福利任務']/.."
    CDK_TAB     = "//div[@data-cname='index']//div[text()='CDK']/.."  
    TONGREN_TAB = "//span[text()='同人']"

class WelfareLocators:
    TASK_PANEL_INDICATOR = "//div[contains(text(), '每日任務')]|//div[contains(text(), '瀏覽5個貼文')]"
    SIGNED_TEXT = "//div[text()='已簽到' or text()='已領取']"
    SIGNED_VISUAL = "//i[contains(@class, 'bg-[var(--fill-1-60)]')]"
    CHECKIN_BUTTON = "//div[text()='簽到' or text()='領取每日福利']/.. | //div[contains(text(), '簽到') or text()='領取']"
    SIGNED_GIFT_ICON = "//div[contains(@class, \"bg-[url('@/assets/imgs/common/icon-gift-true.png')]\")]"
    UNLIT_GIFT_ICON = "//div[contains(@class, 'w-[24px]') and contains(@class, 'h-[24px]') and contains(@class, 'mr-[19px]') and not(contains(@class, 'icon-gift-true.png'))]"
    BROWSE_DONE = "//div[text()='瀏覽5個貼文']/../..//div[text()='5 / 5']"
    LIKE_DONE = "//div[text()='按讚5個貼文']/../..//div[text()='5 / 5']"
    
class PostLocators:
    POST_IMAGES = "//img[contains(@class, 'min-h-[50px]') and contains(@class, 'object-cover')]"
    LIKE_CONTAINER = "//*[@data-cname='like']"
    UNLIKED_ICON = ".//span[@data-cname='svg-icon' and contains(@style, 'var(--text-3)')]"
    BACK_BUTTON = "//*[local-name()='svg' and .//*[local-name()='clipPath' and @id='clip0_3949_49548']]"

class CdkPageLocators:
    PAGE_INDICATOR = "//div[text()='CDKey']"  
    RECOMMENDED_ROWS = "//div[contains(@class, 'cdk-box')]/div[contains(@class, 'py-[10px]')]"
    CDK_CODE_TEXT    = ".//div[contains(@class, 'text-[color:var(--other-6)]')]"