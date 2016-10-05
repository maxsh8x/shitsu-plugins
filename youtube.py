import urlparse
from shitsu import xmpp
from shitsu import modules
from base64 import b64encode
from urllib2 import urlopen


class Youtube(modules.MessageModule):
    args = (1,)
    highlight = False

    def run(self, url):
        """
        Youtube preview.
        For Psi+ (webkit version)  https://sourceforge.net/projects/psiplus/files/:
        Options -> Plugins -> Extended Options Plugin -> Groupchat -> Enable HTML rendering
        shitsu.cfg -> max_groupchat_length = 50000
        """
        url_data = urlparse.urlparse(url)
        query = urlparse.parse_qs(url_data.query)
        video = query['v'][0]
        data = urlopen('http://img.youtube.com/vi/{0}/mqdefault.jpg'.format(video))
        encoded_data = b64encode(data.read())
        img = xmpp.Node('img', attrs={
            'alt': 'img',
            'src': 'data:image/jpeg;base64,{0}'.format(encoded_data)
        })
        return 'Enable HTML rendering to see this preview', ' <br />'.format(unicode(img))
