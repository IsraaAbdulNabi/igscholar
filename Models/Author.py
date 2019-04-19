from Models import Publication
import re
import pprint
import config


class Author(object):
    """Returns an object for a single author"""
    def __init__(self, __data):
        if isinstance(__data, str):
            self.id = __data
        else:
            self.id = re.findall(config._CITATIONAUTHRE, __data('a')[0]['href'])[0]
            self.url_picture = __data('img')[0]['src']
            self.name = __data.find('h3', class_='gsc_1usr_name').text
            affiliation = __data.find('div', class_='gsc_1usr_aff')
            if affiliation:
                self.affiliation = affiliation.text
            email = __data.find('div', class_='gsc_1usr_emlb')
            if email:
                self.email = email.text
            self.interests = [i.text.strip() for i in __data.findAll('a', class_='gsc_co_int')]
            citedby = __data.find('div', class_='gsc_1usr_cby')
            if citedby:
                self.citedby = int(citedby.text[9:])
        self._filled = False

    def fill(self):
        """Populate the Author with information from their profile"""
        url_citations =config._CITATIONAUTH.format(self.id)
        soup =config._get_soup('{0}&pagesize={1}'.format(url_citations,config._PAGESIZE))
        self.name = soup.find('div', id='gsc_prf_in').text
        self.affiliation = soup.find('div', class_='gsc_prf_il').text
        self.interests = [i.text.strip() for i in soup.findAll('a', class_='gsc_prf_ila')]
        self.url_picture = soup.find('img')['src']

        # h-index, i10-index and h-index, i10-index in the last 5 years
        index = soup.findAll('td', class_='gsc_rsb_std')
        self.hindex = int(index[2].text)
        self.hindex5y = int(index[3].text)
        self.i10index = int(index[4].text)
        self.i10index5y = int(index[5].text)

        self.publications = list()
        pubstart = 0
        while True:
            for row in soup.findAll('tr', class_='gsc_a_tr'):
                new_pub = Publication(row, 'citations')
                self.publications.append(new_pub)
            if 'disabled' not in soup.find('button', id='gsc_bpf_next').attrs:
                pubstart += config._PAGESIZE
                soup = config._get_soup('{0}&cstart={1}&pagesize={2}'.format(url_citations, pubstart, _PAGESIZE))
            else:
                break
        self._filled = True
        return self

    def __str__(self):
        return pprint.pformat(self.__dict__)
