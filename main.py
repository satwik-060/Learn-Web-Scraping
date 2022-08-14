from bs4 import BeautifulSoup

with open('home.html', 'r') as html:
    content = html.read()
    
    soup = BeautifulSoup(content,'lxml')
    tags = soup.find('h5') #search for first h5 tag
    tags = soup.find_all('h5') #search for all h5 tag
    for tag in tags :
        print(tag.text)
    # print(tags)
