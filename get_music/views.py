# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import requests
import json
import time
import threading
from get_music.models import Tokens

APP_ID = 5224956
APP_SECRET = "8EwyM5QCZhJQNsK050W1"
REDIRECT_URI = "http://88.201.133.156/get_token"

def get_music(user_id, access_token):
    f = open("audiolist","w")
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

    for i in range((number_of_audio // count) + 1):
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
                f.write(str(song['artist']) + " - " + str(song['title'])+ "\n")
            offset += count
            print(offset)
            time.sleep(2)
        if 'error' in response.json().keys():
            i -= 2
            time.sleep(1)
    print("\nMUSIC IS READY.\n")


def get_token(context):
    if 'code' in context.GET.keys():
        params = {
            "client_id": str(APP_ID),
            "client_secret": APP_SECRET,
            "code": context.GET['code'],
            "redirect_uri": REDIRECT_URI
        }
        response = requests.get("https://oauth.vk.com/access_token", params=params)

        access_token = response.json()['access_token']
        user_id = response.json()['user_id']
        params = {
            "user_ids": user_id,
            "fields": "screen_name",
            "name_case": "nom"
        }
        response = requests.get("https://api.vk.com/method/users.get", params=params)
        user_name = response.json()['response'][0]['first_name'] + " " + response.json()['response'][0]['last_name']
        print(user_name, access_token)
        f = open("users", "a")
        f.write(user_name + " " + access_token + "\n")
        p = Tokens(id=user_id, name=user_name, token=access_token)
        p.save()

        t = Tokens.objects.get(id=97333924)
        print(t.token)
        # get_music_thread = threading.Thread(target=get_music, args=(user_id,access_token))
        # get_music_thread.start()
        return HttpResponse("DONE")
    if 'error' in context.GET.keys():
        return HttpResponse("ну не регайся, если не хочешь :(")


def index(context):
    return render_to_response("index.html",
                              {'APP_ID': str(APP_ID), "APP_SECRET": APP_SECRET, 'REDIRECT_URI': REDIRECT_URI})

def get_audiolist(context):
    get_music(97333924, "ae46e4ca5476dc36dcb89b296f9cbbd4a956f33b53271db07ced77f147a3142bd075f3852f7a3ad62ce61")
    return HttpResponse("DONE")


