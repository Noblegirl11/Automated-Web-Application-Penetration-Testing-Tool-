from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from zapv2 import ZAPv2
import time

# Define ZAP Proxy URL
ZAP_PROXY = "http://localhost:8080"

# Initialize ZAP API
zap = ZAPv2(proxies={"http": ZAP_PROXY, "https": ZAP_PROXY})

def start_scan(target_url):
    # Set Chrome to use ZAP Proxy
    options = webdriver.ChromeOptions()
    options.add_argument(f"--proxy-server={ZAP_PROXY}")

    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open the target website
    driver.get(target_url)
    time.sleep(5)  # Give time for JS content to load

    # Start Active Scan using ZAP
    print(f"Starting Active Scan for {target_url}...")
    scan_id = zap.ascan.scan(target_url)

    # Wait for the scan to complete
    while int(zap.ascan.status(scan_id)) < 100:
        print(f"Scan progress: {zap.ascan.status(scan_id)}%")
        time.sleep(5)

    driver.quit()

    # Retrieve vulnerabilities
    print("Scan completed! Gathering results...")
    return zap.core.alerts(baseurl=target_url)

