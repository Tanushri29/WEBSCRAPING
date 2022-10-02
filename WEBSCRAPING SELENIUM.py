#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().system('pip install selenium')

import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

#connect to the driver
driver= webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe")

#open the naukri page on automated chrome browser
driver.get("https://www.naukri.com/")

#entering designation and location as required
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Analyst')

location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Banglore')

search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()

#Scraping JOB TITLE, JOB LOCATION, COMPANY NAME and EXPERIENCE

job_title=[]
job_location=[]
company_name=[]
experience=[]

title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience.append(exp)
    
#creating data frame of above data
df=pd.DataFrame({'Job_Title':job_title,'Job_Location':job_location,'Company_Name':company_name,'Experience':experience})
df  


# In[14]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

#connect to the driver
driver= webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe")

#open the naukri page on automated chrome browser
driver.get("https://www.naukri.com/")

#entering designation and location as required
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')

location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Banglore')

search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()

#Scraping JOB TITLE, JOB LOCATION, COMPANY NAME and EXPERIENCE

job_title=[]
job_location=[]
company_name=[]
experience=[]

title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi experience"]')
for i in experience_tags[0:10]:
    exp=i.text
    experience.append(exp)
    
#creating data frame of above data
df=pd.DataFrame({'Job_Title':job_title,'Job_Location':job_location,'Company_Name':company_name,'Experience':experience})
df


# In[53]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

#connect to the driver
driver= webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe")

#open the naukri page on automated chrome browser
driver.get("https://www.naukri.com/")

#entering designation as required
designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys('Data Scientist')

search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[62]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time

#connect to the driver
driver= webdriver.Chrome(r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe")

#open the Flipkart page on automated chrome browser
driver.get("https://www.flipkart.com/")

product=driver.find_element(By.CLASS_NAME,"_3704LK ")
product.send_keys('Sunglasses')

search=driver.find_element(By.CLASS_NAME,"L0Z3Pu")
search.click()

#Scraping Brand, Product Description, Price and Discount


Brand=[]
Product_Description=[]
Price=[]
Discount=[]

start=0
end=3
for page in range(start, end):
    
    brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_tags[0:40]:
        Brand.append(i.text)
    
    
    Description=driver.find_elements(By.XPATH,'//a[@class="IRpwTa"]')
    for i in Description[0:40]:
        Product_Description.append(i.text)
   
    
    price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_tags[0:40]:
        Price.append(i.text)
    
    
    discount_tags=driver.find_elements(By.XPATH,'//div[@class="_3Ay6Sb"]')
    for i in discount_tags[0:40]:
        Discount.append(i.text)
        
next_button=driver.find_element(By.XPATH,'//a[@class="_1LKTO3"]')
next_button.click()
    
    
#creating data frame of above data
df=pd.DataFrame({'brand_name':Brand,'Product_Dscrptn':Product_Description,'PRICE':Price,'DISCOUNT':Discount})
print(df)   


# In[ ]:




