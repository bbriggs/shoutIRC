#!/usr/bin/env python
# -*- coding: utf-8 -*-

swiss = {
    'bot_owner': ['Deshi'],
    'start_bot': 'screen -dmS swiss',
    'kill_bot': 'screen -X -S swiss kill',
    'mode': 'standard'
}

network = {
    'server': 'irc.hackmonkey.us',
    'port': 6667,
    'SSL': False,
    'ipv6': False,
    'channels': ['#ctf'],
    'bot_nick': 'Meow',
    'bot_name': 'Swiss Army IRC bot by Deshi & Arisance  Version 1.19',
    'password': ''
}

shoutcast = {
    'server': 'shoutcast url for stats',
    'pull_delay': 1,
    'channels': ['#channel']

}

freeswitch = {
    'server': '127.0.0.1',
    'port': 8021,
    'password': 'auth password for event socket',
    'conference': '1234',
    'pin': 1234,
    'sip': 'sip address',
    'did': '(xxx)xxx-xxxx',
    'channels': ['#channel']
}

mail = {
    'server': "smtp.gmail.com",
    'port': "465",
    'password': "password",
    'username': "email address for gmail"
}
