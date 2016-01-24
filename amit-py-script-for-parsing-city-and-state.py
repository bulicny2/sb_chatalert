from bs4 import BeautifulSoup    
import urllib2

def parseCityState(url):
    """Parse the city and state from sexguide info page"""
    
    response = urllib2.urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    printState = False
    printCity = False
    for div in soup.findAll('div', { "class" : "breadcrumb" }):
        for li in div.findAll('li'):

            if printState == True:

                state = li.get_text()

                printCity = True
                printState = False
                continue


            if printCity == True:
                city = li.get_text()
                break

            if 'States' in li.get_text():
                printState = True
    
        break
    
    if city == '':
        city = '-1'
    if state == '':
        state = '-1'
        
    return city, state

cityAndStateDataFrame = []
for idx, url in enumerate(new_df.url):
    if 'usasexguide' in url.lower():
        city, state = parseCityState(url)
        cityAndStateDataFrame.append((idx, url, city, state))
        print url, city, state
