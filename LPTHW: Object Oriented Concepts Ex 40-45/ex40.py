class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

hack_song = Song(["See if you can hack on this and make it do more things",
                "Don't worry if you have no idea how", "just give it a try",
                " see what happens", "Break it", "trash it", "thrash it", "you can't hurt it"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

hack_song.sing_me_a_song()
