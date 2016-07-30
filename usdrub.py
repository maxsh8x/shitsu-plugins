from shitsu import xmpp
from shitsu import modules
from shitsu.utils.BeautifulSoup import BeautifulSoup
from shitsu import utils
from base64_images import images


class Usd(modules.MessageModule):
    args = (0,)
    highlight = False

    @staticmethod
    def _animation(currency):
        result = unicode()
        for c in currency:
            c = int(c) if c != '.' else 10
            img = xmpp.Node('img', attrs={
                'alt': 'img',
                'src': 'data:image/gif;base64,{0}'.format(images[c])
            })
            result += unicode(img)
        return result

    @property
    def currency(self):
        url = 'https://tinyurl.com/hgezblc'
        data = utils.get_url(url)
        soup = BeautifulSoup(data)
        result = soup.query.results.ask.string
        return result, self._animation(result[:5])

    def run(self):
        """
        Dollar currency.
        For Psi+ (webkit version)  https://sourceforge.net/projects/psiplus/files/:
        Options -> Plugins -> Extended Options Plugin -> Groupchat -> Enable HTML rendering
        shitsu.cfg -> max_groupchat_length = 50000
        """
        return self.currency[0], ' <br />'.format(self.currency[1])
