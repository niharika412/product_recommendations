from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import chromedriver_binary 

names=[]
brands=[]
prices=[]
ogprices=[]
img_urls=[]
ratings=[]
discounts=[]

driver = webdriver.Chrome()
for i in range(1,28):
	driver.get("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&otracker=categorytree&page=" +str(i))

	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	for a in soup.findAll('div',href=False, attrs={'class':'_1UoZlX'}):
		#print(a)
		name=a.find('div', attrs={'class':'_3wU53n'})
		price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
		rating=a.find('div', attrs={'class':'hGSR34'})
		names.append(name.text)
		prices.append(price.text)
		try:
			ratings.append(rating.text)
		except:
			ratings.append("NaN")
		ogp=a.find('div', attrs={'class':'_3auQ3N _2GcJzG'})
		try:
			ogprices.append(ogp.text)
		except:
			ogprices.append("NaN")
		disc=a.find('div', attrs={'class':'VGWI6T'})
		try:
			discounts.append(disc.span.text)
		except:
			discounts.append("NaN")
		#print(names,ratings,ogprices,discounts)

df = pd.DataFrame({'Product Name':names,'Price':prices,'Original Prices':ogprices,'Discount rates':discounts, 'Ratings':ratings})
df.to_csv('laptops.csv', index=False, encoding='utf-8')