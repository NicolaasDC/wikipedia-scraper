# Wikipedia Scraper 

A project to create a scraper with the political leaders of each country you get from the 'https://country-leaders.onrender.com' API

## Usage

1 .Clone the repository to your local machine

The repository contains a wikipedia_scraper.ipynb file. This file was to learn and test out all the code necessary to use later in the OOP part.

The requirements.txt is what libraries you need to install in your virtual enviroment

2 .To run the script, you can execute the main.py file from your command line:

```python
python main.py
```

The main program creates a Wikipedia_scraper object and calls its methods

```python
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
```
# Timeline
This project took two days for completion.

# Personal Situation
This project was done as part of the AI Boocamp at BeCode.org.
