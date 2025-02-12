from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
import time

edge_driver_path = 'D:\\edgedriver_win64\\msedgedriver.exe'
options = Options()
options.add_argument("--headless=new")
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

count = 47

for i in range(1, count+1):
    print('Group '+str(i))
    driver.get('https://www.zhihu.com/collection/920424365?page='+str(i))

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html_content = driver.page_source
    with open(str(i)+'.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
driver.quit()

linkid = 0
output = ''
for i in range(1, count + 1):
    path = str(i)+'.html'
    htmlfile = open(path, 'r', encoding = 'utf-8')
    htmlhandle = htmlfile.read()
    soup = BeautifulSoup(htmlhandle, 'lxml')
    links = soup.find_all('a')
    for link in links:
        if link.get('data-za-detail-view-element_name') == 'Title':
            linkid = linkid+1
            output = output+str(linkid)+'. ['+link.get_text()+'](https:'+link.get('href')+')\n'

with open('zhihu.md', 'w', encoding = 'utf-8') as file:
    file.write(output)
