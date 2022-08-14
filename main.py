from bs4 import BeautifulSoup

with open('home.html', 'r') as html:
    content = html.read()
    
    soup = BeautifulSoup(content,'lxml')
    # tags = soup.find('h5') #search for first h5 tag
    # tags = soup.find_all('h5') #search for all h5 tag
    # for tag in tags :
    #     print(tag.text)
    # # print(tags)

    course_cards = soup.find_all('div',class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'course name : {course_name} and its price : {course_price}')

