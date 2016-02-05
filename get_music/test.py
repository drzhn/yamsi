# -*- coding: utf-8 -*-
import requests
import time

def get_music(user_id, access_token):
    f = open("audiolists/"+str(user_id),"w")
    offset = 0
    count = 100

    params = {
        "owner_id": str(user_id),
        "need_user": "0",
        "offset": str(0),
        "count": str(1),
        "version": "5.44",
        "access_token": access_token
    }
    response = requests.get("https://api.vk.com/method/audio.get", params=params)
    #print response.json()
    number_of_audio = int(response.json()['response'][0])
    #print number_of_audio

    for i in range((number_of_audio // count) + 2):
        params = {
            "owner_id": str(user_id),
            "need_user": "0",
            "offset": str(offset),
            "count": str(count),
            "version": "5.44",
            "access_token": access_token
        }
        response = requests.get("https://api.vk.com/method/audio.get", params=params)
        # print response.json()
        if 'response' in response.json().keys():
            audiolist = response.json()['response'][1:]
            for song in audiolist:
                pass
                # print song['artist'], song['title']
                f.write(str(song['artist'])+ "\n")# " - " + str(song['title'])+ "\n")
            offset += count
            print(offset)
            time.sleep(0.5)
        if 'error' in response.json().keys():
            i -= 2
            time.sleep(1)
    print("\nMUSIC IS READY.\n")

get_music(97333924, "be53acd798702d1d9fa104d0b778dce36482104fb7c811d94697754a40d09c9e1c28d2aaca315845ebc8b")