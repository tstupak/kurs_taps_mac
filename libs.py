from selenium import webdriver

driver = webdriver.Chrome('/Users/tstupak/PycharmProjects/kurs_taps_mac/chromedriver')

driver.get('https://fabrykatestow.pl')
driver.close()