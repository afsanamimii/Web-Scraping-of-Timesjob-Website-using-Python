from bs4 import BeautifulSoup

with open('demo.html', 'r') as html_file:
    content=html_file.read()
    #print(content)



    soup=BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    tags= soup.find('body') 
     #find search for only 1st element

    courses_html_tags=soup.find_all('h5')
    #for courses in courses_html_tags:
        #print(courses.text)

    

    course_cards=soup.find_all('div', class_='card')  
    #Here card is the class name

    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]

        #We are splitting the tags so that we can acess only the last element.
        #[-1] means last element

        #print(course_name)
        #print(course_price)
        print(f'{course_name} costs {course_price}')
