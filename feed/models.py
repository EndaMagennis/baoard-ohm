from django.db import models
from django.contrib.auth.models import User

# Constant to hold the genre choices of game genre
GENRES = [
    ("camp", "Campaign"),
    ("card", "Card Game"),
    ("class", "Classic"),
    ("dex", "Dexterity"),
    ("draft", "Drafting"),
    ("edu", "Educational"),
    ("party", "Party"),
    ("puz", "Puzzle"),
    ("rpg", "Role-Playing Game"),
    ("strat", "Strategy"),
    ("war", "Wargame"),
    ("oth", "Other")
]

# Constant to hold the player count choices of game genre
PLAYER_COUNT = [
    ("any", "Any"),
    ("one_to_two", "1-2 Players"),
    ("one_to_four", "1-4 Players"),
    ("one_to_six", "1-6 Players"),
    ("two_to_four", "2-4 Players"),
    ("two_to_six", "2-6 Players"),
    ("two_to_eight", "2-8 Players"),
    ("two_to_fifteen", "2-15 Players"),
    ("two_to_six", "3-6 Players"),
    ("two_to_eight", "3-8 Players"),
    ("two_to_fifteen", "3-15 Players"),
    ("oth", "Other")
]

# Constant to hold the age range choices of game genre
AGE_RANGE = [
    ("all", "All ages"),
    ("four_plus", "4 +"),
    ("twelve_plus", "12 +"),
    ("fifteen_pus", "15 +"),
    ("eigtheen_plus", "18 +"),
    ("oth", "Other")
]

# Constant to hold the play time choices of game genre
PLAY_TIME = [
    ("under_one", "10-30mins"),
    ("hour_to_two", "1-2 hours"),
    ("two_to_four", "2-4 hours"),
    ("over_four", "4 + hours"),
    ("rest_of", "The rest of your life"),
    ("oth", "Other")
]

# Constant to hold the experience choices of game genre
EXPERIENCE = [
    (1, "Casual"),
    (2, "Medium"),
    (3, "Not Suitable for Beginners"),
    (3, "Hardcore"),
    (4, "Friendship Ender")
]

# Constant to hold the price range choices of game genre
PRICE_RANGE = [
    (1, "$"),
    (2, "$$"),
    (3, "$$$"),
    (4, "$$$$"),
]

# Constant to hold the rating choices of game genre
RATING = [
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_posts')
    content = models.TextField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    genre = models.CharField(max_length=20, choices=GENRES, default="camp")
    number_of_players = models.CharField(
        max_length=100, choices=PLAYER_COUNT, default="one_to_four")
    age_range = models.CharField(
        max_length=20, choices=AGE_RANGE, default="four_plus")
    play_time = models.CharField(
        max_length=20, choices=PLAY_TIME, default="under_one")
    experience = models.IntegerField(choices=EXPERIENCE, default=1)
    price_range = models.IntegerField(choices=PRICE_RANGE, default=1)
    rating = models.IntegerField(choices=RATING, default=1)
    number_of_likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"
        


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes", null=True)

    class Meta:
        # Prevents a user from liking a post more than once
        unique_together = ("user", "post")

    def __str__(self):
        return f"{self.user} likes {self.post}"

    

