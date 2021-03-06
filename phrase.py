import sqlite3
import os

from shitsu import modules

PATH = os.path.dirname(os.path.abspath(__file__))


class Chains:
    def __init__(self, connection):
        self.__result = ''
        self.__conn = connection

    def _collocation(self, arg, counter=5):
        """
        Logic of generation words based on discrete-time Markov chain.
        """
        if not counter:
            return
        self.__result += arg + " "
        for phrase in self.sentences:
            words = phrase[0].split()
            for i, word in enumerate(words):
                if word != arg:
                    continue
                # https://docs.python.org/2/glossary.html#term-eafp
                try:
                    next_word = words[i+1]
                except IndexError:
                    break
                counter -= 1
                return self._collocation(next_word, counter)

    def collocation(self, arg):
        """
        Receives seed word and returns a sequence of words.
        """
        self.__result = ''
        self._collocation(arg)
        return self.__result

    @property
    def sentences(self):
        """
        Returns sentences from table phrase as tuples.
        It's used for passing words from database.
        """
        st_curs = self.__conn.cursor()
        respond = st_curs.execute('SELECT * FROM phrases ORDER BY RANDOM()')
        sentences = respond.fetchall()
        return sentences

    @property
    def keyword(self):
        """
        Returns random keyword from keyword table.
        It's used as seed for generate a sequence of words.
        """
        kw_curs = self.__conn.cursor()
        respond = kw_curs.execute('SELECT * FROM keywords ORDER BY RANDOM() LIMIT 1')
        keyword = respond.fetchone()[0]
        return keyword.replace('\n', '')

    @property
    def random(self):
        """
        Returns random word sequence using keyword as seed.
        """
        self.collocation(self.keyword)
        return self.__result


class Phrase(modules.MessageModule):
    highlight = False
    args = (0,)

    def run(self):
        """
        Send funny phrase from My Little Pony through discrete-time Markov chain.
        """
        # Russian dictionary with MLP phrases.
        conn = sqlite3.connect(PATH + '/mlp.db')
        chains = Chains(conn)
        return chains.random
