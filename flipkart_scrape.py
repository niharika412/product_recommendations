from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import chromedriver_binary 

names=[]
brands=[]
prices=[]
ogprices=[]
img_urls=[]
discounts=[]

driver = webdriver.Chrome()
for i in range(1,21):
	driver.get("https://www.flipkart.com/womens-clothing/western-wear/pr?sid=2oq%2Cc1r%2Cha6&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_Women_0_Western+Wear&sort=popularity&page=" +str(i))

	content = driver.page_source
	soup = BeautifulSoup(content, features="html.parser")
	for item in soup.findAll('div',href=False, attrs={'class':'_2LFGJH'}):
		brand=item.find('div', attrs={'class':'_2B_pmu'})
		try:
			brands.append(brand.text)
		except:
			brands.append("NaN")
		name=item.find('a', attrs={'class':'_2mylT6'})
		try:
			names.append(name.text)
		except:
			try:
				name=item.find('a', attrs={'class':'_2mylT6 _3Ockxk'})
				names.append(name)
			except:
				names.append('NaN')
		price=item.find('a', attrs={'class':'_2W-UZw'}).find('div', attrs={'class':'_1vC4OE'})
		try:
			prices.append(price.text)
		except:
			prices.append("NaN")
		ogprice=item.find('a', attrs={'class':'_2W-UZw'}).find('div', attrs={'class':'_3auQ3N'})
		try:
			ogprices.append(ogprice.text)
		except:
			ogprices.append("NaN")
		disc=item.find('a', attrs={'class':'_2W-UZw'}).find('div', attrs={'class':'VGWI6T'})
		try:
			discounts.append(disc.span.text)
		except:
			discounts.append("NaN")
	#price=a.find('div', attrs={'class':'_1vC40E'})
	#prices.append(price.text)
	for item in soup.findAll('a',href=True,attrs={'class':'_3dqZjq'}):
		im=item.find('img', attrs={'class':'_3togXc'})
		try:
			img_urls.append(im.get('src'))
		except:
			img_urls.append("NaN")
		

df = pd.DataFrame({'Product Name':names,'Price':prices,'Original Prices':ogprices,'Discount rates':discounts,'Brand':brands, 'Image URLS':img_urls})
df.to_csv('women_westernwear.csv', index=False, encoding='utf-8')