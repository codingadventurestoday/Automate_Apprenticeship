import urllib.request 
import beautifulSoup 

# this dict stores apprenticeship companies names as keys and the urls used to look up availability as the values
apprenticeship_opportunity = {'Barclays': 'https://search.jobs.barclays/foundation-apprenticeships', 
                              'Tandem': 'https://madeintandem.com/about/apprenticeship-program/', 
                              'Spotify': 'https://fellowship.spotify.com',
                              'LinkedIn': 'https://careers.linkedin.com/reach/Backend',
                              'Lyft': 'https://www.lyft.com/careers/university',
                              'JP Morgan': 'https://careers.jpmorgan.com/global/en/students/programs/financial-services-apprenticeship?search=&tags=location__Americas__UnitedStatesofAmerica',
                              'Twitch': 'https://www.twitch.tv/jobs/en/early-career/#apprentice'
                              }




# this function is used to create a beautiful soup object for each url give 
def bbsObject(url):
    link = urllib.request(url) # look up the correct method for this 

    return 
#this function converts the bbsobject into the a json structure 
def jsonStructure(bbsObject):

    return 

# this function takes the json structure and prints the infomation related to the apprenticeship
def relatedInformation(company, jsonStructure):
    print(apprenticeship_opportunity[company]':')
