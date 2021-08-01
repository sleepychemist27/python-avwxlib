from json.decoder import JSONDecodeError
import requests
from avwxStatus import status

url = 'https://avwx.rest/api/'
api_key = 'REPLACE YOU KEY'



class Station:
    """A station class"""
    def __init__(self, ident):
        self.ident = ident
    def get_info(self):
        headers = {
        'Authorization':api_key
        }
        station_info_request = requests.get(url + f'/station/{self.ident}?format=json', headers=headers)
        if station_info_request.status_code == 200:
            try:
                self.info = station_info_request.json()
            except JSONDecodeError:
                print(f'Error in decoding JSON response. Information might not be available for {self.ident}')
        else:
            print(f'API Error: HTTP {station_info_request.status_code},{status(station_info_request.status_code)}.')
    
    def get_metar(self):
        headers = {
        'Authorization':api_key
        }
        station_metar_request = requests.get(url + f'/metar/{self.ident}?options=summary', headers=headers)
        if station_metar_request.status_code == 200:
            try:
                self.metar = station_metar_request.json()
            except JSONDecodeError:
                print(f'Error in decoding JSON response. METAR might not be available for {self.ident}')
        else:
            print(f'API Error: HTTP {station_metar_request.status_code},{status(station_metar_request.status_code)}.')
        self.flightrules = self.metar['flight_rules']

    def get_taf(self):
        headers = {
        'Authorization':api_key
        }
        station_taf_request = requests.get(url + f'/taf/{self.ident}?options=summary', headers=headers)
        if station_taf_request.status_code == 200:
            try:
                self.taf = station_taf_request.json()
            except JSONDecodeError:
                print(f'Error in decoding JSON response. TAF might not be available for {self.ident}')
        else:
            print(f'API Error: HTTP {station_taf_request.status_code},{status(station_taf_request.status_code)}.')
        self.taf = station_taf_request.json()

    def update(self):
        self.get_metar()
        self.get_taf() 

    '''
    The following features require a subscription from avwx.rest
    '''

    def get_pirep(self):
        headers = {
            'Authorization':api_key,
            'Content-Type':'text/plain'
        }
        station_pirep_request = requests.get(url + f'/pirep/{self.ident}', headers = headers)
        self.pirep = station_pirep_request.json()
        if station_pirep_request.status_code == 200:
            try:
                self.pirep = station_pirep_request.json()
            except JSONDecodeError:
                print(f'Error in decoding JSON response. Information may not be available for {self.ident}')
        elif station_pirep_request.status_code == 403:
            raise Exception('Error in authentication. To obtain Pirep, you need a subscription, visit: avwx.rest.')
        else:
            print(f'API Error: HTTP {station_pirep_request.status_code},{status(station_pirep_request.status_code)}.')
        self.pirep = station_pirep_request.json()

class Metar:
    def __init__(self, data):
        self.data = data
    
    def parse(self):
        body_length = len(self.data)
        headers = {
            'content-type':'text/plain',
            'Authorization':api_key,
        }
        METAR_parse_request = requests.post(url + f'/parse/metar?options=summary', data=self.data, headers=headers)
        if METAR_parse_request.status_code == 200:
            try:
                self.info = METAR_parse_request.json()
            except JSONDecodeError:
                print(f'Error in decoding JSON response')
        else:
            print(f'API Error: HTTP {METAR_parse_request.status_code},{status(METAR_parse_request.status_code)}.')
        self.parsed = METAR_parse_request.json()
        self.text = self.parsed['summary']
class Taf:
    def __init__(self, data):
        self.data = data
    def parse(self):
        body_length = len(self.data)
        headers = {
            'content-type':'text/plain',
            'authorization':api_key,
        }
        taf_parse_request = requests.post(url + f'/parse/taf?', data=self.data, headers=headers)
        if taf_parse_request.status_code == 200:
            try:
                self.info = taf_parse_request.json()
            except JSONDecodeError:
                print(f'Error in decoding JSON response')
        else:
            print(f'API Error: HTTP {taf_parse_request.status_code},{status(taf_parse_request.status_code)}.')
        self.parsed = taf_parse_request.json()

if __name__ == "__main__":
    print('Use this as a package!')
