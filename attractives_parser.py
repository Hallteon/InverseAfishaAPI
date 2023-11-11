import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

API_KEY = '5ae2e3f221c38a28845f05b61e9871acfa940c8d8073e83925042c84'
categories = {'towers': 'Башни', 'architecture': 'Архитектура', 'historic': 'История',
              'interesting_places': 'Интересные места', 'monuments': 'Монументы', 'cultural': 'Культура'}


def get_objects():
    places_data = []
    city = requests.get('https://api.opentripmap.com/0.1/ru/places/geoname', params={'name': 'город Смоленск',
                                                                                     'lang': 'ru',
                                                                                     'apikey': API_KEY}).json()
    city_lon = city['lon']
    city_lat = city['lat']
    places = requests.get('https://api.opentripmap.com/0.1/ru/places/radius', params={'lat': city_lat,
                                                                                      'lon': city_lon,
                                                                                      'radius': 30000,
                                                                                      'lang': 'ru',
                                                                                      'apikey': API_KEY})
    for place in places.json()['features']:
        places_data.append(place['properties']['xid'])

    return places_data


def get_place(xid):
    place = requests.get(f'https://api.opentripmap.com/0.1/ru/places/xid/{xid}', params={'lang': 'ru', 'apikey': API_KEY}).json()

    if 'wikipedia_extracts' in place.keys() and 'image' in place.keys():
        if 'road' in place['address'].keys() and 'house_number' in place['address'].keys():
            place_data = {'name': place['name'],
                          'cover': place['image'],
                          'description': place['wikipedia_extracts']['text'],
                          'address': f'г. {place["address"]["city"]}, {place["address"]["road"]}, '
                                     f'{place["address"]["house_number"]}'}

        elif 'city' in place['address'].keys():
            place_data = {'name': place['name'],
                          'cover': place['image'],
                          'description': place['wikipedia_extracts']['text'],
                          'address': f'г. {place["address"]["city"]}'}
        else:
            place_data = {'name': place['name'],
                          'cover': place['image'],
                          'description': place['wikipedia_extracts']['text']}

        place_data['lon'] = place['point']['lon']
        place_data['lat'] = place['point']['lat']

        if [x for x in place_data['cover'].split('/') if x][1] == 'commons.wikimedia.org':
            wiki_page = requests.get(place_data['cover'])
            wiki_soup = BeautifulSoup(wiki_page.text, 'lxml')
            cover_url = wiki_soup.find('div', class_='fullImageLink').find('a').get('href')

            place_data['cover'] = cover_url

        for kind in place['kinds'].split(','):
            if kind in categories.keys():
                place_data['category'] = categories[kind]
                return place_data

        if 'category' not in place_data.keys():
            place_data['category'] = 'Разное'

        return place_data

    else:
        return None


def create_place(place_data):
    place = requests.post('https://inverse-tracker.store/api/attractions/generate/', json=place_data)

    return place


if __name__ == '__main__':
    places = get_objects()

    for place_id in places[1:]:
        place = get_place(place_id)

        if place:
            print(create_place(place).json())

        else:
            continue
