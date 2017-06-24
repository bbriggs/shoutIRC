#!/usr/bin/env python
# -*- coding: utf-8 -*-

swiss = {
    'bot_owner': ['Deshi'],
    'start_bot': 'screen -dmS swiss',
    'kill_bot': 'screen -X -S swiss kill',
    'mode': 'standard'
}

network = {
    'server': 'irc.0x00sec.org',
    'port': 6667,
    'SSL': False,
    'ipv6': False,
    'channels': ['#radio'],
    'bot_nick': 'ShoutIRC',
    'bot_name': 'shoutcast to IRC by Deshi  Version 1.19',
    'password': 'XXXX'
}

shoutcast = {
    'server': 'http://janus.shoutca.st:9632/stats',
    'pull_delay': 1,
    'channels': ['#radio']

}


mail = {
    'server': "smtp.gmail.com",
    'port': "465",
    'password': "password",
    'username': "email address for gmail"
}

