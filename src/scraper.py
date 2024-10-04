from bs4 import BeautifulSoup
import requests 
import json
import re

class Wikipedia_scraper:
    '''
    A class to create a scraper that builds a JSON file   with the political leaders of each country you get from
    the 'https://country-leaders.onrender.com' API
    

    Methods
    -------
    '''
    def __init__(self):
        '''
        Constructs the wikipedia scraper object
        No parameters are required to create the object
        Object has 1 default parameter: a url to the API
        '''
        self.root_url = 'https://country-leaders.onrender.com'

    def __repr__(self):
        '''
        Returns "Wikipedia_scraper()"
        '''
        return "Wikipedia_scraper()"
    
    def get_cookie(self):
        '''
        Returns a valid cookie to query the API        
        '''
        cookie_url = self.root_url + '/cookie'
        cookies=requests.get(cookie_url).cookies
        return cookies
    
    def get_countries(self):
        '''
        Returns a list of the supported countries for the API
        '''
        countries_url = self.root_url + '/countries'
        req_countries = requests.get(countries_url, cookies=self.get_cookie())
        countries = req_countries.json()
        return countries
    
    def get_leaders(self):
        '''
        Retruns a dictionary with the leaders of the countries from the API
        The dictionary keys are the countries from the get_countries list
        The value of those keys is a list dictionaries containing information about the leaders
        '''
        countries = self.get_countries()
        leaders_per_country = {}
        for country in countries:
            req_leaders = requests.get(f"{self.root_url}/leaders?country={country}", cookies=self.get_cookie())
            leaders = req_leaders.json()
            leaders_per_country[country] = leaders
        return leaders_per_country
        
    def get_first_paragraph(self, wikipedia_url):
        '''
        This methods retrieves the first paragraph of the wikipedia page using the Beautiful soup library
        The wikipedia_url parameter needs the be given as a parameter

        The first paragraph contains some Wikipedia references, HTML code, phonetic pronunciation etc.
        We use regex to get rid of those and get a cleaner text
        '''
        session = requests.Session()
        r = session.get(wikipedia_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        bold = []
        for par in soup.find_all("p"):
            bold = par.find_all('b')
            if bold != []:
                first_paragraph = par.text
                break
        cleaned_text = re.sub(r'\[.*?\]|\(.*?ⓘ.*?\)', '', first_paragraph)
        cleaned_text = re.sub(r'<.*?>', '', cleaned_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        return cleaned_text
    
    def add_first_paragraph(self):
        '''
        This methods loops through the dictionary and adds the first wikipedia paragraph to the dictionary
        '''
        leaders_per_country = self.get_leaders()
        for key in leaders_per_country:
            for leader in leaders_per_country[key]:
                first_paragraph = self.get_first_paragraph(leader['wikipedia_url'])
                leader['first_paragraph'] = first_paragraph
        return leaders_per_country
    
    def save_json_file(self, data, name_of_the_file):
        '''
        A method to save the dictionary as a JSON file
        '''
        with open(name_of_the_file, "w") as outputfile:
            json.dump(data, outputfile, indent=4)
    
    def read_json_file(self, file):
        '''
        A method to read a JSON file and extract the information
        '''
        with open(file, "r") as inputfile:
            file_data = json.load(inputfile)
            return file_data

