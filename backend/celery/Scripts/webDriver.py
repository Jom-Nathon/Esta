from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Other imports remain the same

def initialize_driver():
    options = Options()
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    return driver

def getPlotInfo(driver):  # Now driver is passed as a parameter
    driverURL = 'https://asset.led.go.th/newbidreg/'
    driver.get(driverURL)
    # The rest of your function remains the same, using the passed driver

def main():
    driver = initialize_driver()
    getPlotInfo(driver)
    # You can pass the same driver to other functions as needed
    driver.quit()

if __name__ == "__main__":
    main()