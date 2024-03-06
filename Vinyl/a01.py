class Vinyl:
    def __init__(self, album, artist, year):
        self.album = album
        self.artist = artist
        self.year = year

    def display(self):
        print(' Album_info : ' + self.album + ' , ' + self.artist + ' , ' + self.year)


def run():
    jason_zhang_album01 = Vinyl('Its love', 'Jason_Zhang', '21/11/2010')
    jason_zhang_album02 = Vinyl('Future_live', 'Jason_Zhang', '12/10/2018')
    jason_zhang_album01.display()
    jason_zhang_album02.display()
