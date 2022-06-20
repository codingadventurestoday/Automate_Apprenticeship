import urllib.request 
import beautifulSoup 

# this dict stores apprenticeship companies names as keys and the urls used to look up availability as the values
apprenticeship_opportunity = {'google': *****, 
                              'dts': *****, 
                              'spotify': ****,
                              '': ****,
                              '': ****,
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
