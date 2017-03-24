import fresh_tomatoes
import media

# Define movie data to be displayed on website

toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and some toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "Blue people on planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

dazed_and_confused = media.Movie(
    "Dazed and Confused",
    "People come of age and get paddled",
    "https://upload.wikimedia.org/wikipedia/en/a/af/Dazed_and_Confused_%281993%29_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=caJu4be6O2c")

school_of_rock = media.Movie(
    "School of Rock",
    "Rocking with children",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

# Create list of moves for website
movies = [toy_story, avatar, dazed_and_confused, school_of_rock]

# Generate website
fresh_tomatoes.open_movies_page(movies)
