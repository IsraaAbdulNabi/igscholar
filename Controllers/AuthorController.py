from Controllers import WebDriverController
from bs4 import BeautifulSoup
from Models import Author
import config as properties
import sys
import time
import pickle
import random as rnd
import requests
import codecs

topic = sys.argv[2]
driver = WebDriverController.create_driver()
driver.get(properties._HOST + properties._KEYWORDSEARCH + topic)

def extract_authoers(elements):
    authors=[]
    for xi in range(len(elements)):
        authors.append(elements[xi].text)
    return authors

def retrieve_authors():
    flag = 1
    page_count = 1
    authors=[]
    while flag:
        elements=driver.find_elements_by_class_name("gs_ai_name")
        author_name=extract_authoers(elements)
        for name in author_name:
         authors.append(name)
        next = driver.find_elements_by_class_name("gs_wr")[2]
        time.sleep(5 + rnd.randint(1,10))
        if (next and page_count<= 1):
            next.click()
            page_count = page_count + 1
        else:
            flag = 0
    #dbfile = open('authoresList.csv', 'ab')
    #pickle.dump(authors, dbfile)
    return authors

def search_author(name):
    """Search by author name and return a generator of Author objects"""
    url =properties._HOST+properties._AUTHSEARCH + name
    driver.get(url)
    temp_ele=driver.find_elements_by_class_name("gs_hlt")
    temp_ele[0].click()
    affiliation_webElement = driver.find_elements_by_class_name("gsc_prf_il")
    affiliation_text = affiliation_webElement[0].text
    role, university = affiliation_text.split(",")
    email_webElement=affiliation_webElement[1]
    email_text=email_webElement.text
    email=email_text[18:]
    interests_webElement = driver.find_elements_by_partial_link_text("/citations?view_op=search_authors&hl=ar&mauthors=")
    intrests = []
    for xi in range(len(interests_webElement)):
        intrests.append(interests_webElement[xi].text)
    numbers=driver.find_elements_by_class_name("gsc_rsb_std")
    h_index_ele= numbers[2]
    citations_ele=numbers[0]
    h_index=h_index_ele.text
    citations= citations_ele.text
    pic_ele=driver.find_element_by_id("gsc_prf_pup-img")
    pic_url=pic_ele.get_attribute("src")
    year_ele = driver.find_element_by_id("gsc_a_ha")
    year_ele.click()
    years_list=driver.find_elements_by_class_name("gsc_a_y")
    last_active_ele=years_list[2]
    last_active=last_active_ele.text
    temp = {'name':name, 'role':role, 'uni':university, 'email':email, 'intrests':intrests, 'h_index':h_index, 'citations':citations ,'pic_url':pic_url, 'last_active_year':last_active}
    author_object=Author.Author(temp)
    return author_object

def store_author_db():
    authors= retrieve_authors()
    for author_name in authors :
        try :
          author_instance =search_author(author_name)
          time.sleep(10 + rnd.randint(1, 10))
          author_instance.print_auther()
        except:
            print("un related researcher")


if __name__ == '__main__':
   store_author_db()

