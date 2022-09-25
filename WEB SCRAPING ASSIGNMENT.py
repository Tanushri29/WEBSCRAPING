#!/usr/bin/env python
# coding: utf-8

# # 1.) Python Program to display all the Header Tags from Wikipedia.org

# In[26]:


#install all the requirements
get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')

#import requests
from bs4 import BeautifulSoup
import requests

#getting source code of the webpage
url= requests.get('https://en.wikipedia.org/wiki/Main_Page')
url

#page content
htmlcontent= BeautifulSoup(url.content)
htmlcontent

#extracting and displaying all the header tags
header_tags= htmlcontent.find_all(["h1","h2","h3"])
for i in header_tags:
    print (i)


# # 2.)Python Program to display IMDB's top rated 100 movies

# In[165]:


#import requests

from bs4 import BeautifulSoup
import requests
import pandas as pd

#Requestpage source from URL 
url= "https://www.imdb.com/chart/top/"
page= requests.get(url)
page

#Display the page source code
page.content
soup= BeautifulSoup(page.content)
soup

#Scrape movie names
scraped_movies= soup.find_all('td',class_="titleColumn")
scraped_movies

#parse movie names
movies= [] 
for movie in scraped_movies[0:100]:
    movie= movie.get_text().replace('\n'," ")
    movie= movie.strip("  ")
    movies.append(movie)
movies

#scrape rating for movies
scraped_ratings= soup.find_all('td', class_="ratingColumn imdbRating")
scraped_ratings

#parse ratings
ratings= [] 
for rating in scraped_ratings [0:100]:
    rating= rating.get_text().replace("\n", ' ')
    ratings.append(rating)
ratings

#store the scraped data
data= pd.DataFrame()
data['Movie Names']= movies
data['Ratings']= ratings
data


# # 3.)Python Program to display IMDB's top rated 100 INDIAN movies

# In[94]:


#import requests

from bs4 import BeautifulSoup
import requests
import pandas as pd

#Requestpage source from URL 
url= "https://www.imdb.com/india/top-rated-indian-movies/"
page= requests.get(url)
page

#Display the page source code
page.content
soup= BeautifulSoup(page.content)
soup

#Scrape movie names
scraped_movies= soup.find_all('td',class_="titleColumn")
scraped_movies

#parse movie names
movies= [] 
for movie in scraped_movies[0:100]:
    movie= movie.get_text().replace('\n'," ")
    movie= movie.strip("  ")
    movies.append(movie)
movies

#scrape rating for movies
scraped_ratings= soup.find_all('td', class_="ratingColumn imdbRating")
scraped_ratings

#parse ratings
ratings= [] 
for rating in scraped_ratings [0:100]:
    rating= rating.get_text().replace("\n", ' ')
    ratings.append(rating)
ratings

#store the scraped data
data= pd.DataFrame()
data['Movie Names']= movies
data['Ratings']= ratings
data


# # 4.) Python program to display list of respected former presidents of India(i.e. Name , Term of office)

# In[28]:


#import requests
from bs4 import BeautifulSoup
import requests


#getting source code of the webpage
URL= requests.get('https://presidentofindia.nic.in/former-presidents.htm')
URL

#page content
soup= BeautifulSoup(URL.content)
soup

list=[]

#extracting and displaying list of former presidents
for i in soup.find_all('div',class_="presidentListing"):
    list.append((i.text).replace('\n', ' ').strip("  "))
list                


# # 5.)Python program to scrape cricket rankings of
#    a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.   

# In[183]:


#import requests
from bs4 import BeautifulSoup
import requests

#getting source code of the webpage
page= requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')
page

#page content
soup1= BeautifulSoup(page.content)
soup1

team = []
matches=[]
point=[]
rating=[]
tem=[]
sp=" "

for i in soup1.find_all('span', class_="u-hide-phablet")[0:10]:
    team.append(i.text)

for i in soup1.find_all('td', class_="table-body__cell u-center-text")[0:18]:
    matches.append(i.text)

for i in soup1.find_all('td', class_="table-body__cell u-text-right rating")[0:9]:
    rating.append(i.text)

for i in soup1.find_all('td', class_="rankings-block__banner--matches")[0:1]:
    tem.append(i.text)

for i in soup1.find_all('td', class_="rankings-block__banner--points")[0:1]:
    tem.append(i.text)

for i in soup1.find_all('td', class_="rankings-block__banner--rating u-text-right")[0:1]:
    sp= i.findAll(text=True)
    sp= [item.strip() for item in sp if str(item)]

print("Solution:")
print(team)
matches1=[matches[i] for i in range(len(matches)) if i % 2 == 0]
matches1.insert(0,tem[0])
print(matches1)
point = [matches[i] for i in range(len(matches)) if i % 2 != 0]
point.insert(0,tem[1])
print(point)
rating.insert(0,sp[0])
print(rating)


# # 5.)Python program to scrape cricket rankings of
# b) Top 10 ODI Batsmen along with the records of their team and rating
# c)Top 10 ODI bowlers along with the records of their team and rating.

# In[93]:


#import requests
from bs4 import BeautifulSoup
import requests
#getting source code of the webpage
page= requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi')
page
#page content
soup1= BeautifulSoup(page.content)
soup1

batsmen=[]
team=[]
rating=[]

for i in soup1.find_all('td',class_="table-body__cell name")[0:9]:
    batsmen.append((i.text).replace('\n'," "))
    
for i in soup1.find_all('span',class_="table-body__logo-text")[0:9]:
    team.append(i.text)
    
for i in soup1.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
     rating.append(i.text)
print("------------------------------------------------------------------")
print("Top 10 ODI Batsmen along with the records of their team and rating")
print("------------------------------------------------------------------")
print(batsmen)
print(team)
print(rating)
print("------------------------------------------------------------------")
print("Top 10 ODI bowlers along with the records of their team and rating")
print("------------------------------------------------------------------")
bowler=[]
bowler_team=[]
bowler_rating=[]

for i in soup1.find_all('td',class_="table-body__cell name")[9:18]:
    bowler.append((i.text).replace('\n'," "))
    
for i in soup1.find_all('span',class_="table-body__logo-text")[9:18]:
    bowler_team.append(i.text)
    
for i in soup1.find_all('td',class_="table-body__cell u-text-right rating")[9:18]:
     bowler_rating.append(i.text)
        
print(bowler)
print(bowler_team)
print(bowler_rating)


# ## 5.)Python program to scrape cricket rankings of
#    a) Top 10 ODI teams in womens cricket along with the records for matches, points and rating. 

# In[89]:


#import requests
from bs4 import BeautifulSoup
import requests

#getting source code of the webpage
page= requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')
page

#page content
soup1= BeautifulSoup(page.content)
soup1

team = []
matches=[]
point=[]
rating=[]
tem=[]
sp=" "

for i in soup1.find_all('span', class_="u-hide-phablet")[0:10]:
    team.append(i.text)

for i in soup1.find_all('td', class_="table-body__cell u-center-text")[0:18]:
    matches.append(i.text)

for i in soup1.find_all('td', class_="table-body__cell u-text-right rating")[0:9]:
    rating.append(i.text)

for i in soup1.find_all('td', class_="rankings-block__banner--matches")[0:1]:
    tem.append(i.text)

for i in soup1.find_all('td', class_="rankings-block__banner--points")[0:1]:
    tem.append(i.text)

for i in soup1.find_all('td', class_="rankings-block__banner--rating u-text-right")[0:1]:
    sp= i.findAll(text=True)
    sp= [item.strip() for item in sp if str(item)]

print("Solution:")
print(team)
matches1=[matches[i] for i in range(len(matches)) if i % 2 == 0]
matches1.insert(0,tem[0])
print(matches1)
point = [matches[i] for i in range(len(matches)) if i % 2 != 0]
point.insert(0,tem[1])
print(point)
rating.insert(0,sp[0])
print(rating)


# # 6.)Python program to scrape cricket rankings of
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[92]:


#import requests
from bs4 import BeautifulSoup
import requests
#getting source code of the webpage
page= requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
page
#page content
soup1= BeautifulSoup(page.content)
soup1

batswomen=[]
team=[]
rating=[]

for i in soup1.find_all('td',class_="table-body__cell name")[0:9]:
    batswomen.append((i.text).replace('\n'," "))
    
for i in soup1.find_all('span',class_="table-body__logo-text")[0:9]:
    team.append(i.text)
    
for i in soup1.find_all('td',class_="table-body__cell u-text-right rating")[0:9]:
     rating.append(i.text)
print("------------------------------------------------------------------")
print("Top 10 ODI Batswomen along with the records of their team and rating")
print("------------------------------------------------------------------")
print(batswomen)
print(team)
print(rating)
print("------------------------------------------------------------------")
print("Top 10 ODI Allrounder along with the records of their team and rating")
print("------------------------------------------------------------------")
allrounder=[]
allrounder_team=[]
allrounder_rating=[]

for i in soup1.find_all('td',class_="table-body__cell name")[18:29]:
    allrounder.append((i.text).replace('\n'," "))
    
for i in soup1.find_all('span',class_="table-body__logo-text")[18:29]:
    allrounder_team.append(i.text)
    
for i in soup1.find_all('td',class_="table-body__cell u-text-right rating")[18:29]:
     allrounder_rating.append(i.text)
        
print(allrounder)
print(allrounder_team)
print(allrounder_rating)


# # 7.)python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# #i) Headline
# #ii) Time
# #iii) News Link

# In[54]:


#import requests
from bs4 import BeautifulSoup
import requests
import pandas as pd

#getting source code of the webpage
url= requests.get('https://www.cnbc.com/world/?region=world')
url

#page content
soup= BeautifulSoup(url.content)
soup

headline=[]
news_link=[]

for i in soup.find_all('a',class_="LatestNews-headline"):
    headline.append(i.text)   
for i in soup.find_all('a',class_="LatestNews-headline"):
    news_link.append(i.get('href'))

#store the scraped data
data= pd.DataFrame()
data['HEADLINE']= headline
data['NEWS_LINK']= news_link
data


# # 8.) Python program to scrape the details of most downloaded articles from AI

# In[53]:


#import requests
from bs4 import BeautifulSoup
import requests
import pandas as pd

#getting source code of the webpage
url= requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
url

#page content
soup= BeautifulSoup(url.content)
soup

#creating empty list
paper_title=[]
authors=[]
published_date=[]
paper_url=[]

for i in soup.find_all('h2', class_="sc-1qrq3sd-1 MKjKb sc-1nmom32-0 sc-1nmom32-1 hqhUYH ebTA-dR"):
     paper_title.append(i.text)
for i in soup.find_all('span', class_="sc-1w3fpd7-0 pgLAT"):
      authors.append(i.text)
for i in soup.find_all('span', class_="sc-1thf9ly-2 bKddwo"):
     published_date.append(i.text)
for i in soup.find_all('a', class_="sc-5smygv-0 nrDZj"):
     paper_url.append(i.get('href'))


#store the scraped data
data= pd.DataFrame()
data['Paper Title']= paper_title
data['Authors']= authors
data['Published Date']= published_date
data['Paper URL']= paper_url
data


# # 9.) Python program to scrape mentioned details from dineout.co.in :
#  i) Restaurant name
#  ii) Cuisine
#  iii) Location
#  iv) Ratings
#  v) Image URL

# In[98]:


#import requests
from bs4 import BeautifulSoup
import requests

#getting source code of the webpage
url= requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
url

#page content
soup= BeautifulSoup(url.content)
soup

restaurant_name=[]
cuisine= []
location=[]
ratings=[]
image_url=[]


for i in soup.find_all('a', class_= "restnt-name ellipsis"):
    restaurant_name.append(i.text)


for i in soup.find_all('span', class_="double-line-ellipsis"):
     cuisine.append(i.text.split("|")[1])


for i in soup.find_all('div',class_='restnt-loc ellipsis'):
    location.append(i.text)


for i in soup.find_all('div',class_="restnt-rating rating-4"):
    ratings.append(i.text)


for i in soup.find_all('img',class_="no-img"):
    image_url.append(i.get('data-src'))
    

print(restaurant_name)
print("------------------------------------------------------------------------------------------------------------")
print(cuisine)
print("------------------------------------------------------------------------------------------------------------")
print(location)
print("------------------------------------------------------------------------------------------------------------")
print(ratings)
print("------------------------------------------------------------------------------------------------------------")
print(image_url)
    
    


# # 10) Python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en
# i) Rank
# ii) Publication
# iii) h5-index
# iv) h5-median

# In[47]:


#import requests
from bs4 import BeautifulSoup
import requests
import pandas as pd

#getting source code of the webpage
url= requests.get('https://scholar.google.com/citations?view_op=top_venues&hl=en')
url

#page content
soup= BeautifulSoup(url.content)
soup

#creating empty list
ranking= []
publication= []
h5_index= []
h5_median= []

#scraping and parsing the ranking, publication, h5_index, h5_median
for i in soup.find_all('td',class_="gsc_mvt_p"):
    ranking.append(i.text)
ranking    
for i in soup.find_all('td',class_="gsc_mvt_t"):
    publication.append(i.text)
publication    
for i in soup.find_all('a',class_="gs_ibl gsc_mp_anchor"):
    h5_index.append(i.text)
h5_index    
for i in soup.find_all('span',"gs_ibl gsc_mp_anchor"):
    h5_median.append(i.text)
h5_median    
    

#store the scraped data
data= pd.DataFrame()
data['Rank']= ranking
data['Publication']= publication
data['H5_INDEX']= h5_index
data['H5_MEDIAN']= h5_median
data

