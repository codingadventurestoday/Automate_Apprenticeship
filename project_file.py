import requests 
from bs4 import BeautifulSoup 
import re 

# this dict stores apprenticeship companies names as keys and the urls used to look up availability as the values
apprenticeship_opportunity = {'Barclays': 'https://search.jobs.barclays/foundation-apprenticeships',  
                              'LinkedIn': 'https://careers.linkedin.com/reach/Backend',
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
        bsObj = BeautifulSoup(web_response, 'html.parser')
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
        else:
            position = 'open'            
        return position
    except:
        print('''There is a problem with the the tag searches in the Barclay bsObj. Please ensure these tags are aligned with the webpage's HTML''')
        return None           
              
def linkedIn_availability(linkedIn_bsobj):
    try:
        wrapper_div_list = obj.body.find('div', {'class': 'wrapper'})
        banner_section_list = wrapper_div_list.findAll('div', {'class': 'banner parbase section'})
        p_tag = section_list[1].p
        status = p_tag.get_text()
        try: 
            check = re.findall(r'No longer accepting', status)
            if check[0] == 'No longer accepting':
                position = 'closed'
            else:
                position = 'open'
        return position
        except: 
            print('There was a problem with     
    except:      
        print('''There is a problem with the the tag searches in the LinkedIn bsObj. Please ensure these tags are aligned with the webpage's HTML''')
        return None       
              
def jpMorgan_availability(jpMorgan_bsObj):
    try:
        jpmc_div_tags_list = bsobj.body.findAll('div', {'class': 'jpmc-wrapper'})
        career_section = jpmc_div_tags_list[11]
        info_no_availability_tag = career_section.find('div', {'class': 'info-no-availability'})
        availability = info_no_availability_tag.get_text()
        if availability.lstrip() == 'Applications currently closed':
            position = 'closed'
        else:
            position = 'open'
        return position
    expect: 
        print('''There is a problem with the the tag searches in the JP Morgan bsObj. Please ensure these tags are aligned with the webpage's HTML''')
        return None
              
def twitch_availability(twitch_bsObj):
    try:
        class_c_list = twitch_bsObj.findAll('div', {'c-paragraph c-paragraph--primary c-paragraph--left'})
        strong_tag = class_c_list[3].strong
        position_information = strong_tag.get_text()
        if position_information == 'closed':
            position = 'closed'
        else:
            position = 'open'
        return position
    except:      
        print('''There is a problem with the the tag searches in the Twitch bsObj. Please ensure these tags are aligned with the webpage's HTML''')
        return None 
              
#this section is where each company's bsObj is created              
barclay_bsObj = create_bs_object('barlclays')
linkedIn_bsObj = create_bs_object('LinkedIn')
jpMorgan = create_bs_object('JP Morgan')
twitch_bsObj = create_bs_object('Twitch')
              
              
              
              
#this section is where each company's position status is found through their bsObj              
barclay_position_status = barclay_availability(barclay_bsObj)
linkedIn_position_status = linkedIn_availability(linkedIn_bsObj)
jpMorgan_position_status = jpMorgan_availability(jpMorgan_bsObj)
twitch_position_status = twitch_availability(twitch_bsObj)

print('Barclay: ', barclay_position_status)
print('LinkedIn: ', linkedIn_position_status)
print('JP Morgan: ', jpMorgan_position_status)
print('Twitch: ', twitch_position_status)
