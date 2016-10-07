#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
from urlparse import urlparse
from urllib import urlencode
from shitsu import modules


class Bypass(modules.MessageModule):
    regexp = r"(https?://[^'\"\s>]{1,500})"
    types = ("groupchat",)
    highlight = False

    def run(self, url):
        domain = urlparse(url).netloc
        api_url = 'https://api.antizapret.info/get.php?type=small&item={0}'.format(domain)
        response = urllib2.urlopen(api_url)
        if int(response.read()) == 0:
            return ""
        data = urlencode({'url': url})
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
        request = urllib2.Request('http://noblockme.ru/go', data, headers)
        return urllib2.urlopen(request).geturl()
