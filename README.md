# BlablaLink Daily Task Automator / 每日福利任務自動化腳本

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Selenium-4.0+-green?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/Docker-Supported-blue?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
</p>

<p align="center">
  <a href="#-繁體中文">繁體中文</a> •
  <a href="#-english">English</a>
</p>

---

## 🇹🇼 繁體中文

### 📌 專案目的
為了解決因日常疏忽遺忘簽到而錯失平台獎勵的問題[cite: 8]。透過自動化腳本，系統能校對並補全每日福利任務，確保所有獎勵領取不漏接[cite: 8]。

### 🛠️ 系統架構與需求
* **核心語言**：Python 3.10+[cite: 6, 8]。
* **自動化工具**：Selenium WebDriver / `undetected-chromedriver`[cite: 4, 7, 8]。
* **瀏覽器**：最新版本 Google Chrome[cite: 6, 8]。
* **憑證導出**：需於瀏覽器安裝 Chrome 插件（如 Cookie-Editor 或 EditThisCookie）用以導出 `cookies_2.json`[cite: 3, 8]。

### 📁 專案檔案說明
* `daily_checkin_4.py`：主自動化執行程式[cite: 4]。
* `requirements_2.txt`：Python 套件清單[cite: 7]。
* `DockerFile_2` & `docker-compose_2.yml`：Docker 容器部署設定檔[cite: 5, 6]。

### 🚀 運行與部署方式

#### 1. Synology NAS 部署
開發者自身採用 Synology NAS 的 Docker 環境進行全自動化管理[cite: 8]：
* 將專案檔案上傳至 NAS[cite: 5, 8]。
* 透過專案內附的 `DockerFile_2` 與 `docker-compose_2.yml` 構建並啟動容器[cite: 5, 6, 8]。
* 於 Synology NAS 的「控制台」 > 「任務排程器」中，新增一個每日定時執行的排程，藉此實現全自動化每日簽到[cite: 8]。

#### 2. Windows 本地部署
本地 Windows 系統運行[cite: 8]：
* 安裝 Python 環境及最新版 Google Chrome 瀏覽器[cite: 6, 8]。
* 透過 `pip install -r requirements_2.txt` 安裝套件[cite: 6, 7, 8]。
* 配合 Windows 內置的「工作排程器」，建立每日觸發器並設定執行 `python daily_checkin_4.py`，藉此實現每日背景定時簽到[cite: 4, 8]。

### ⚠️ 重要注意事項
> 📝 **學術用途聲明**
> 本專案僅供學術研究、技術交流與自動化測試之用途[cite: 8]。
> 
> 🔄 **Cookie 時效性**
> 若腳本因認證失效而停止，請重新透過 Chrome 插件更新 `cookies_2.json`[cite: 3, 4, 8]。

---

## 🇺🇸 English

### 📌 Purpose
This project is designed to prevent users from missing out on daily platform rewards due to oversight or forgetting to check in manually[cite: 8]. Through this automation script, the system precisely verifies and completes daily welfare tasks to ensure no rewards are missed[cite: 8].

### 🛠️ System Architecture & Requirements
* **Core Language**: Python 3.10+[cite: 6, 8].
* **Automation Framework**: Selenium WebDriver / `undetected-chromedriver`[cite: 4, 7, 8].
* **Browser Environment**: Latest version of Google Chrome[cite: 6, 8].
* **Credential Export**: Requires a Chrome extension (e.g., Cookie-Editor or EditThisCookie) to export `cookies_2.json` for passwordless authentication[cite: 3, 8].

### 📁 File Structure
* `daily_checkin_4.py`: The main automation script[cite: 4].
* `requirements_2.txt`: List of Python dependencies[cite: 7].
* `DockerFile_2` & `docker-compose_2.yml`: Configuration files for Docker containerization[cite: 5, 6].

### 🚀 Deployment & Execution

#### 1. Synology NAS Deployment
The developer personally utilizes a Docker environment on a Synology NAS for fully automated management[cite: 8]:
* Upload the project files to the NAS directory[cite: 5, 8].
* Build and launch the container using the provided `DockerFile_2` and `docker-compose_2.yml`[cite: 5, 6, 8].
* Navigate to Control Panel > Task Scheduler in Synology NAS, and create a daily scheduled task to trigger the script automatically[cite: 8].

#### 2. Windows Local Deployment
For users without a NAS device, the script can be deployed reliably on a local Windows system[cite: 8]:
* Install Python environment and the latest version of Google Chrome[cite: 6, 8].
* Install dependencies via `pip install -r requirements_2.txt`[cite: 6, 7, 8].
* Utilize the built-in Windows Task Scheduler to create a daily trigger that executes `python daily_checkin_4.py` in the background[cite: 4, 8].

### ⚠️ Important Notes
> 📝 **Academic Use Only**
> This project is intended solely for academic research, technical exchange, and automation testing purposes[cite: 8].
> 
> 🔄 **Cookie Expiration**
> If the script stops working due to authentication failure, please re-export and refresh your `cookies_2.json` using the Chrome extension[cite: 3, 4, 8].