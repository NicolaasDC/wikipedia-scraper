from src.scraper import Wikipedia_scraper

#Create a Wikipedia_scraper class object and print it
wiki = Wikipedia_scraper()
print(wiki)

#Get the countries from the API in a list and print them
countries = wiki.get_countries()
print(countries)

#Get all the leaders from the API in a dictionay and print them
leaders = wiki.get_leaders()
print(leaders)

#Add all the first paragraphs of their wikipedia article in the dictionary
leaders_first_paragraph = wiki.add_first_paragraph()
print(leaders_first_paragraph)

#Save the dictionary in a json file
wiki.save_json_file(data=leaders_first_paragraph, name_of_the_file='leaders.json')

#Read a json file and store the data in a variable
data = wiki.read_json_file('leaders.json')
print(data)