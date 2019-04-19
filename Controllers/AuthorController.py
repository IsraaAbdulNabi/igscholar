from Controllers import WebDriverController
import sys
import time
import pickle

def retrieve_authors():
    topic = sys.argv[2]
    driver = WebDriverController.create_driver()
    driver.get("https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors= %s" % topic)
    flag = 1
    page_count = 1
    authors= []
    while flag:
        authors =authors.append(driver.find_elements_by_class_name("gs_ai_name"))
        next = driver.find_elements_by_class_name("gs_wr")[2]

        if (page_count % 10 == 0):
            time.sleep(10)

        if (next and page_count<= 100):
            next.click()
            page_count = page_count + 1
        else:
            flag = 0

    dbfile = open('authoresList', 'ab')
    pickle.dump(authors, dbfile)
    return authors

print (retrieve_authors())