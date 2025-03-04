from django.db import models


# Create your models here.
class Challenges(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    flag = models.CharField(max_length=100)
    points = models.IntegerField()
    author = models.CharField(max_length=100)

    CHALLENGE_CATEGORIES = [
        ("websiteExploitation", "Website Exploitation"),
        ("reverseEngineering", "Reverse Engineering"),
        ("binaryExploitation", "Binary Exploitation"),
        ("cryptography", "Cryptography"),
        ("forensics", "Forensics"),
        ("miscellaneous", "Miscellaneous"),
    ]

    category = models.CharField(choices=CHALLENGE_CATEGORIES)

    DIFFICULTIES = [
        ("baby", "Baby"),
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    difficulty = models.CharField(choices=DIFFICULTIES)
    solve_count = models.PositiveIntegerField(default=0)
    attachment = models.URLField(null=True)
    upvote = models.PositiveIntegerField(default=0)
    downvote = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
