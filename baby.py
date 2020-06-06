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
for i in range(1,21):
	driver.get("https://www.flipkart.com/baby-care/pr?sid=kyh&otracker=categorytree&page=" +str(i))

	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	for a in soup.findAll('a',href=True, attrs={'class':'_2cLu-l'}):
		try:
			names.append(a.text)
		except:
			names.append('NaN')
	for a in soup.findAll('a',href=True, attrs={'class':'_1Vfi6u'}):
		price=a.find('div', attrs={'class':'_1vC4OE'})
		try:
			prices.append(price.text)
		except:
			prices.append("NaN")
		ogprice=a.find('div', attrs={'class':'_3auQ3N'})
		try:
			ogprices.append(ogprice.text)
		except:
			ogprices.append("NaN")
		disc=a.find('div', attrs={'class':'VGWI6T'})
		try:
			discounts.append(disc.span.text)
		except:
			discounts.append("NaN")

#print(len(names),len(prices),len(ogprices),len(discounts),len(ratings))
df = pd.DataFrame({'Product Name':names,'Price':prices,'Original Prices':ogprices,'Discount rates':discounts})
df.to_csv('baby.csv', index=False, encoding='utf-8')