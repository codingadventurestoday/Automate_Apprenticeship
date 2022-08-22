import requests 
from bs4 import BeautifulSoup 

# this dict stores apprenticeship companies names as keys and the urls used to look up availability as the values
apprenticeship_opportunity = {'Barclays': 'https://search.jobs.barclays/foundation-apprenticeships', 
                              'Tandem': 'https://madeintandem.com/about/apprenticeship-program/', 
                              'Spotify': 'https://fellowship.spotify.com',
                              'LinkedIn': 'https://careers.linkedin.com/reach/Backend',
                              'Lyft': 'https://www.lyft.com/careers/university',
                              'JP Morgan': 'https://careers.jpmorgan.com/global/en/students/programs/financial-services-apprenticeship?search=&tags=location__Americas__UnitedStatesofAmerica',
                              'Twitch': 'https://www.twitch.tv/jobs/en/early-career/#apprentice'
                              }

#function that creates a beautifulsoup obj as in ouput. which we can parse through. Input is the company's name which website's will be scraped
#first company_webpage is set to the http which is the value to the companies name key in the apprenticeship_opportunity dict
#Second web_response is set to the webpage's HTML with the requests library's get function and content function
#third bsObj is set to the a BeautifulSoup object with the content of the website's HTML then returned
def create_bs_obj(company_name):
    try:
        company_webpage = apprenticeship_opportunity[company_name]
        web_response = requests.get(company_webpage).content
        bsObj = BeautifulSoup(web_response)
        return bsObj
    except: 
        print(f'''There is a problem with creating a BeauitfulSoup object with {company_name}. The problems may be: 
        1. The company is not in our apprenticeship_opportunity dictionary. Solution is to add the company and it's website. 
        2. The company's website address has changed. Please ensure the http is correct.
        3. The script could not connect to the server. Ensure that you are connected to the internet. Then try again.'''
        return None 
