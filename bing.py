import json
import urllib
import urllib2
from shitsu import modules


class Bing(modules.MessageModule):
    raw_query = True

    def run(self, query):
        """Add bing_api_key to shitsu.cfg"""
        api_key = self._bot.cfg.get('bing_api_key', '')
        query = urllib.urlencode({
            'Query': "'{0}'".format(query.encode('utf-8')),
            'Adult': "'{0}'".format('Off'),
            '$format': 'json'
        })
        base_url = 'https://api.datamarket.azure.com/Bing/Search/v1/'
        url = '{0}Web?{1}'.format(base_url, query)
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, base_url, '', api_key)
        auth_handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(auth_handler)
        urllib2.install_opener(opener)
        response = urllib2.urlopen(url).read()
        data = json.loads(response)
        results = data['d']['results']
        if not results:
            return 'nothing :<'
        result = results[0]
        output = u'{0}\n{1}\n{2}'.format(
            result['Title'],
            result['Description'],
            result['Url']
        )
        return output
