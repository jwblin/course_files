#============================================================================
# An example of a Book, Article, and Bibliography class.
#
# Author: Johnny Lin. 
#
# Copyright (c) 2006-2011 by Johnny Lin.  For licensing, distribution 
# conditions, contact information, and additional documentation see
# the URL http://www.johnny-lin.com/pylib.shtml.
#============================================================================


#- Define the Book class:

class Book(object):
    def __init__(self, authorlast, authorfirst, title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year

    def make_authoryear(self):
        self.authoryear = self.authorlast + '(' + self.year +')'

    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst \
                               + ', ' + self.title + ', ' + self.place \
                               + ':  ' + self.publisher + ', ' \
                               + self.year + '.'

#- Define the Article class:

class Article(object):
    def __init__(self, authorlast, authorfirst, articletitle, journaltitle,
                 volume, pages, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.articletitle = articletitle
        self.journaltitle = journaltitle
        self.volume = volume
        self.pages = pages
        self.year = year

    def make_authoryear(self):
        self.authoryear = self.authorlast + ' (' + self.year +')'

    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst \
                               + ' (' + self.year + '):  ' \
                               + '"' + self.articletitle + '," ' \
                               + self.journaltitle + ', ' \
                               + self.volume + ', ' + self.pages + '.'


#- Define the Bibliography class:

import operator

class Bibliography(object):
    def __init__(self, entrieslist):
        self.entrieslist = entrieslist

    def sort_entries_alpha(self):
        tmp = sorted(self.entrieslist, 
                     key=operator.attrgetter('authorlast', 'authorfirst'))
        self.entrieslist = tmp
        del tmp

    def write_bibliog_alpha(self):
        self.sort_entries_alpha()
        output = ''
        for ientry in self.entrieslist:
            output = output + ientry.write_bib_entry() + '\n\n'
        return output[:-2]


#- Create a few instances of Book and Article classes:

beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty",
               "San Francisco", "Ignatius Press", "1999", )
pynut = Book( "Martelli", "Alex", "Python in a Nutshell",
              "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )

nature = Article( "Smith", "Jane", "My Nobel prize-winning paper",
                  "Nature", "481", "234-236", "2012" )
science = Article( "Doe", "Samuel", "My almost Nobel prize-winning paper",
                  "Science", "500", "36-38", "2011" )
noname = Article( "Doe", "John", "My no-one-has-heard-of paper",
                  "J. Irreproducible Results", "49", "34-36", "2005" )

mybib = Bibliography([beauty, pynut, nature, science, noname])


#- Print some diagnostics:

if __name__ == '__main__':
    print 'Entries list before sort:  \n    ', \
        [i.authorlast for i in mybib.entrieslist]
    mybib.sort_entries_alpha()
    print 'Entries list after sort:  \n    ', \
        [i.authorlast for i in mybib.entrieslist]
    print 'Write out bibliography:  \n', mybib.write_bibliog_alpha()


#===== end file =====
