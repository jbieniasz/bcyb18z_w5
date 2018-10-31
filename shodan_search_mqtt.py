import shodan
import time
import os

def search_shodan():
    SHODAN_API_KEY = "your API key from Shodan"
    search_query = "mqtt alarm"
    
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        results = api.search(search_query)
        file = open("mqtt-results.txt", "w")
        for result in results['matches']:
            searching = result['ip_str']
            file.write(searching + '\n')
        file.close()
    except shodan.APIError, e:
        pass

search_shodan()
