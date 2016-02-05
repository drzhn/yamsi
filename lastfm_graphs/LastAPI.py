# -*- coding: utf-8 -*-

import requests
import json


def similar_artists(artist, API_KEY):
    params = {
        "method": "artist.getSimilar",
        "artist": artist,
        "api_key": API_KEY,
        "format": 'json'
    }
    r = requests.get('http://ws.audioscrobbler.com/2.0/', params=params)
    similar = {}
    if 'similarartists' in r.json().keys():
        for simArtist in r.json()['similarartists']['artist']:
            # print simArtist['name'], simArtist['match']
            # if float(simArtist['match']) in similar.keys():
            #     similar[float(simArtist['match'])].append(simArtist['name'])
            # else:
            #     similar[float(simArtist['match'])] = []
            #     similar[float(simArtist['match'])] = simArtist['name']
            similar[float(simArtist['match'])] = simArtist['name']
    else:
        print(r.json())
    return similar
#
# sim = similar_artists("Mr.Kitty","6d44fe32b4be725146401adc08001305")
# for i in sim.keys():
#     if i > 0.8:
#         print(sim[i])