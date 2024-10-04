from bs4 import BeautifulSoup
import requests 

class Wikipedia_scraper:

    def __init__(self):
        self.root_url = 'https://country-leaders.onrender.com'

    def __repr__(self):
        return "Wikipedia_scraper()"
    
    def get_cookie(self):
        cookie_url = self.root_url + '/cookie'
        cookies=requests.get(cookie_url).cookies
        return cookies
    
    def get_countries(self):
        countries_url = self.root_url + '/countries'
        req_countries = requests.get(countries_url, cookies=self.get_cookie())
        countries = req_countries.json()
        return countries
    
    def get_leaders(self):
        countries = self.get_countries()
        leaders_per_country = {}
        for country in countries:
            req_leaders = requests.get(f"{self.root_url}/leaders?country={country}", cookies=self.get_cookie())
            leaders = req_leaders.json()
            leaders_per_country[country] = leaders
            return leaders_per_country
        
    def get_first_paragraph(self, wikipedia_url):
        r = requests.get(wikipedia_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(wikipedia_url) # keep this for the rest of the notebook
    #   [insert your code]
        bold = []
        for par in soup.find_all("p"):
            bold = par.find_all('b')
            if bold != []:
                first_paragraph = par.text
                break
        return first_paragraph
    



wiki = Wikipedia_scraper()
#print(wiki.get_cookie())
#print(wiki.get_countries())
#print(wiki.get_leaders())

washington = 'https://en.wikipedia.org/wiki/George_Washington'
first_paragraph_washington = wiki.get_first_paragraph(washington)
print(first_paragraph_washington)