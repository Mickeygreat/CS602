'''
Dictionary of Lists Example 
Based on https://canvas.instructure.com/courses/1133362/pages/book-5-dot-5-python-layers-of-abstraction
'''
import pprint as pp
pp = pp.PrettyPrinter(indent=2)
weather = []

def readweather():
    ''' return a list of dicts with weather info '''

    weather =  [ 
        { 'place': {'city' : "Blacksburg, VA", 'zip code' : 24061} , 'temps' : [76, 72, 64] } , 
        { 'place': {'city' : "Seattle, WA",    'zip code' : 98101} , 'temps' : [53, 53, 59] } ,
        { 'place': {'city' : "Miami, FL",      'zip code' : 33101} , 'temps' : [86, 87, 88] } , 
        { 'place': {'city' : "San Jose, CA",   'zip code' : 95103} , 'temps' : [79, 82, 83] } , 
        { 'place': {'city' : "New York, NY",   'zip code' : 10036} , 'temps' : [85, 88, 92] }
    ]
    return weather

def cityandzip(weather):
    ''' Print City and Zip Codes '''
    for forecast in weather: 
        city = forecast['place']['city']
        zip = forecast['place']['zip code'] 
        print (f"{city:14s}\t\t {zip:5d}")

def hightemps(weather):
    print ("\nHigh Temps\n")
    for forecast in weather:
        city = forecast['place']['city']
        hightemp = max(forecast['temps'])
        print (f"{city:14s}\t\t {hightemp:5d}")

        
        
def sortedbycity(weather):
    dict = {}
    print ("\nSorted By City\n")
    for forecast in weather:
        city = forecast['place']['city']
        hightemp = max(forecast['temps'])
        dict[city] = hightemp
    
    cities = list(dict.keys())
    cities.sort()
    for city in cities:
        print (f"{city:14s}\t\t {dict[city]:5d}")

        

def sortedbytemp(weather):


    dict = {}
    print ("\nSorted By Temp\n")
    for forecast in weather:
        city = forecast['place']['city']
        hightemp = max(forecast['temps'])
        dict[city] = hightemp
    
    cities = list (dict.keys())
    temps = list(dict.values())
    temps.sort(reverse=True)
    for temp in temps:
        for city in cities:
            if dict[city] == temp:
                print (f"{city:14s}\t\t {dict[city]:5d}")
                break


def sortedbytemp_clever(weather):
    print ("\nClever Sorted By Temp\n")

    dict = {}

    for forecast in weather:
        city = forecast['place']['city']
        hightemp = max(forecast['temps'])
        dict[city] = hightemp

    temps = list(dict.values())
    temps_sorted = sorted(temps, reverse= True) # sorted(temps, reverse=True)

    print("Temps Sorted:", temps_sorted)
    cities = list(dict.keys())
    print(cities)
    for temp in temps_sorted:
        print(f"{cities[temps.index(temp)]:14s}\t\t{temp:5d}")


def main(): 
    
    print ("Cities and Zip Codes")
    weather = readweather()
    pp.pprint(weather)

    cityandzip(weather)
    
    hightemps(weather)
    
    sortedbycity(weather)


    sortedbytemp(weather)


    sortedbytemp_clever(weather)

    
main()
