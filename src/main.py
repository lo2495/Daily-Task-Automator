from browser_manager import BrowserManager
from bot_tasks import BotTasks
from notifier import send_discord_message

def run():
    browser = None
    try:
        browser = BrowserManager()
        tasks = BotTasks(browser)
        
        try:
            tasks.run_cdk_task()
        except Exception:
            pass
        
        try:
            if not tasks.run_welfare_task():
                tasks.run_like_task()
        except Exception as e:
            send_discord_message(f"❌ 任務執行錯誤: {e}")
            
    except Exception as e:
        send_discord_message(f"❌ 系統啟動錯誤: {e}")
    finally:
        if browser:
            browser.close()

if __name__ == "__main__":
    run()