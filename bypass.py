#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from urllib import urlencode
from shitsu import modules


class Bypass(modules.MessageModule):
    args = (1,)
    highlight = False

    def run(self, url):
        """
        Send web proxy alias for url to chat
        """
        data = urlencode({'url': url})
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
        req = urllib2.Request('http://noblockme.ru/go', data, headers)
        return urllib2.urlopen(req).geturl()
