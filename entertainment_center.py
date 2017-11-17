import media

# entertainment_center.py contains instances of Movie from media.py.
# Movies should be retrieved with the get_movies() function

interstellar = media.Movie(
    "Interstellar",
    "Astronauts travel through a wormhole in order to find a new habitable"
    " planet.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

two_thousand_one = media.Movie(
    "2001: A Space Odyssey",
    "Astronauts travel to Jupiter to investigate a mysterious object in its"
    " orbit. An AI makes decisions.",
    "https://bostonhassle.com/wp-content/uploads/2017/09/2001.jpg",
    "https://www.youtube.com/watch?v=lfF0vxKZRhc")

tropic_thunder = media.Movie(
    "Tropic Thunder",
    "A group of narccicistic actors try to make the most realistic Vietnam"
    " war movie ever.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/d/d6/Tropic_thunder_ver3.jpg/220px-Tropic_thunder_ver3.jpg",
    "https://www.youtube.com/watch?v=T-6YhRZowgc")

sherlock_holmes = media.Movie(
    "Sherlock Holmes",
    "The best private detective of the 1800s teams up with a guy named"
    " Watson to solve some crimes.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0NjEwNjUxM15BMl5BanBnXkFtZTcwMzk0MjQ5Mg@@._V1_UY1200_CR86,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=ZSUiBVfvqhc")

a_clockwork_orange = media.Movie(
    "A Clockwork Orange",
    "Some youths of the future do hood rat things.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3MjM1Mzc4N15BMl5BanBnXkFtZTgwODM0NzAxMDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
    "https://www.youtube.com/watch?v=xHFPi_3kc1U")

john_wick = media.Movie(
    "John Wick",
    "Somebody kills John Wick's dog. Everyone they know, love, or associate"
    " with dies.",
    "http://is2.mzstatic.com/image/thumb/Video2/v4/3b/ea/a4/3beaa4a6-611c-cbc2-6718-fd2578abf363/source/1200x630bb.jpg",
    "https://www.youtube.com/watch?v=RllJtOw0USI")

totoro = media.Movie(
    "My Neighbor Totoro",
    "A Japanese family moves to the countryside. Their children discover a"
    " mysterious, adorable forest spirit named Totoro",
    "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",
    "https://www.youtube.com/watch?v=TuLX50_5UAI")

it = media.Movie(
    "It",
    "A coming of age story, with a killer clown.",
    "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",
    "https://www.youtube.com/watch?v=7no56Zw1e20")

blade_runner = media.Movie(
    "Blade Runner",
    "Do androids dream of electric sheep?",
    "https://vignette.wikia.nocookie.net/bladerunner/images/e/e0/Blade-runner-directors-cut-poster--large-msg-119325148375.jpg/revision/latest/scale-to-width-down/350?cb=20110425200646",
    "https://www.youtube.com/watch?v=eogpIG53Cis")


def get_movies():
    """ Returns a list of all Movies in the entertainment center """
    return [interstellar, two_thousand_one, tropic_thunder, sherlock_holmes,
            a_clockwork_orange, john_wick, totoro, it, blade_runner]
