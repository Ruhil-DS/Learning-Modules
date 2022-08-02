from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

prod_name = []
prod_link = []

driver.get("https://www.magmabrakes.com/catalog/")