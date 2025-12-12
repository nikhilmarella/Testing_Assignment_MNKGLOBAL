import os
from datetime import datetime

def save_screenshot(driver, folder="screenshots", prefix="screenshot"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"{folder}/{prefix}_{timestamp}.png"
    driver.save_screenshot(path)
    return path
