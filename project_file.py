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
              
def barclay_availability(barclay_bsObj):
    try:
        span_tag = barclay_bsObj.find('div', {'class': 'card-layout--card'}).span
        span_tag_text = span_tag.get_text()
        if span_tag_text.lower() == 'roles are closed':
            position = 'closed'
            return 
        else:
            position = 'open'            
            return position
    except:
        print('''There is a problem with the the tag searches in the Barclay bsObj. Please ensure these tags are aligned with the webpage's HTML''')
                          
def spotify_availability(spotify_bsObj):
    return None            
              
def linkedIn_availability(linkedIn_bsobj):
    return None
              
def lyft_availability(lyft_bsObj):
    return None
              
def jpMorgan_availability(jpMorgan_bsObj):
    return None
              
def twitch_availability(twitch_bsObj):
    return None 
              
#this section is where each company's bsObj is created              
barclay_bsObj = create_bs_object('barlclays')
#spotify_bsObj = create_bs_object('spotify')
#linkedIn_bsObj = create_bs_object('LinkedIn')
#lfyt_bsObj = create_bs_object('Lfty')
#jpMorgan = create_bs_object('JP Morgan')
#twitch_bsObj = create_bs_object('Twitch')
              
              
              
              
#this section is where each company's position status is found through their bsObj              
barclay_position_status = barclay_availability(barclay_bsObj)
#spotify_position_status = spotify_availability(spotify_bsObj)
#linkedIn_position_status = linkedIn_availability(linkedIn_bsObj)
#lyft_position_status = lyft_availability(lyft_bsObj)
#jpMorgan_position_status = jpMorgan_availability(jpMorgan_bsObj)
#twitch_position_status = twitch_availability(twitch_bsObj)
              
