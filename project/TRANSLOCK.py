# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 20:20:25 2019

@author: Eesh Gupta
"""

import json
import requests
from datetime import datetime
from .send_message import sendSMS

#input: two buildings (src and dest)
#then, find possible bus routes and closest bus stops
# i.e. BUSCH to CA, two possible routes?? also EE and F??
#look up bus stop for next bus
#find the next bus in that bus stop and time.

def building_to_stop(build_1, build_2, d, weekend):
    """
    Input: 2 buildings (strings), d is from route
    Output: (list of strings) Routes connecting the stops closest to the buildings, 
            (string) pickup stop
    """
    
    #creating a dict of buildings (keys) and stop closest to them (value)
    build_and_stops = {'AB':'Scott Hall', 'ARC':'Allison Road Classrooms', 'ARH':'College Hall', 'BE':'Livingston Plaza', 'BH':'Student Activities Center Northbound', 'BIO': 'Public Safety Building on Commercial Southbound', 'BME': 'Busch Student Center', 'BL': 'Lipman Hall', 'BT': 'Lipman Hall', 'CA': 'Student Activities Center', 'CCB' : 'Science Building', 'CDL' : 'Lipman Hall', 'CI': 'Student Activities Center Northbound', 'COR': 'Hill Center (NB)', 'DAV': 'Red Oak Lane', 'ED': 'Student Activities Center Northbound', 'EN': 'Hill Center (NB)', 'FBO': 'Busch Student Center', 'FH': 'Scott Hall', 'FNH': 'Red Oak Lane', 'FOR': 'Red Oak Lane', 'FS': 'Red Oak Lane', 'HC': 'Student Activities Center Northbound', 'HCK': 'Gibbons', 'HH': 'Gibbons', 'HLL': 'Hill Center (NB)', 'HSB': 'Public Safety Building on Commercial Southbound' , 'LOR': 'Red Oak Lane', 'LSH' : 'Quads', 'LSH-AUD': 'Quads', 'KLG': 'College Hall','MI': 'Zimmerli Arts Museum','MU': 'Zimmerli Arts Museum', 'PH' : 'Allison Road Classrooms', 'RAB': 'College Hall', 'RC': 'Livingston Plaza', 'RWH': 'Busch Student Center', 'SC': 'Scott Hall', 'SEC': 'Hill Center (NB)', 'TH': 'Red Oak Lane', 'TIL': 'Quads', 'VD': 'Scott Hall', 'VH': 'Zimmerli Arts Museum', 'WAL': 'Red Oak Lane', 'WL': 'Science Building', 'ZAM': 'Zimmerli Arts Museum' }
    stopA = build_and_stops[build_1]
    stopB = build_and_stops[build_2]
    
    #getting an array of the elements of the following form (route name, route id, [list of stops])
    url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"
    querystring = {"agencies": "1323"}
    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "a8fa08437amsh7c55452dc71bc6bp1a6351jsn8a5ebd3a1ba3"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    a = [(a['long_name'], a['route_id'], [d[x] for x in a['stops']]) for a in data['data']['1323']]
    #finding the which routes contain stop a and stop b
    alpha_routes =[]
    alpha_alpha_routes = []
    
    for route in a:
        if (stopA in route[2]) and (stopB in route[2]):
            alpha_routes.append(route[0])
    
    if weekend:
        for route in alpha_routes:
            if "Weekend" in route:
                alpha_alpha_routes.append(route)
    else:
        for route in alpha_routes:
            if "Weekend" not in route:
                alpha_alpha_routes.append(route) 
    #only considering the first element
    alpha_alpha_routes = alpha_alpha_routes[0]
    return (alpha_alpha_routes, stopA)


#returns dictionary, key is stop id and value is the string name
def stops():
    url = "https://transloc-api-1-2.p.rapidapi.com/stops.json"
    querystring = {"callback":"call","agencies":"1323"}
    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "a8fa08437amsh7c55452dc71bc6bp1a6351jsn8a5ebd3a1ba3"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    a = [(a['name'], a['stop_id']) for a in data['data']]
    
    d = {x[1]: x[0] for x in a}
    return d

#returns list of routes and the bus stops on them
def routes(d):
    url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"
    querystring = {"agencies": "1323"}
    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "a8fa08437amsh7c55452dc71bc6bp1a6351jsn8a5ebd3a1ba3"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    a = [(a['long_name'], a['route_id'], [d[x] for x in a['stops']]) for a in data['data']['1323']]
    #print ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
   # print (a)
    #print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    d2 = {a['route_id']: a['long_name'] for a in data['data']['1323']}
    #for x in a: print (x)
    return d2

def eta(d, d2):
    url = "https://transloc-api-1-2.p.rapidapi.com/arrival-estimates.json"
    querystring = {"callback": "call", "agencies": "1323"}
    headers = {
        'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
        'x-rapidapi-key': "a8fa08437amsh7c55452dc71bc6bp1a6351jsn8a5ebd3a1ba3"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    d2 = {d[a['stop_id']]: [(d2[x['route_id']], str(((datetime.strptime(x['arrival_at'], "%Y-%m-%dT%H:%M:%S-04:00") - datetime.now()).total_seconds()//60)) + " min " + str(((datetime.strptime(x['arrival_at'], "%Y-%m-%dT%H:%M:%S-04:00") - datetime.now()).total_seconds()%60//1)) + " s") for x in a['arrivals']] for a in data['data']}
    #print(d2)
    return d2
    #a = [(d[a['stop_id']], ) for a in data['data']]

def main(buildA_='ARC', buildB_='SC', phone_number="+18482562066", weekend = True):
    """
    Input: 2 buildings and a phone number
    Output: Message to the inputted phone telling user how much time to which bus to which stop
    """
    stop_dict = stops()
    route_dict = routes(stop_dict)
    stops_to_routes=eta(stop_dict, route_dict)
    route_and_stop = building_to_stop(buildA_, buildB_, stop_dict, weekend)
    
    for stop, routes_ in stops_to_routes.items():
        if stop == route_and_stop[1]:
            print(stop)
            for route in routes_:
#                print(route[0])
#                print(route[1] + "maybe")
#                print(route_and_stop[0])
                if route[0] == route_and_stop[0]:
                    
                    #value = stops_to_routes[stop]
                    time = route[1]
                    print(time)
                    key_stop = stop
                    key_route = route[0]
    message= "You have " + str(time) + " to catch "+ str(key_route)+ " bus from " + str(key_stop)
    sendSMS(phone_number, message)
    print(time)
#TRANSLOCK.main('SC', 'RC', '+18482562066')
    

#if __name__ == '__main__':
#    main()
