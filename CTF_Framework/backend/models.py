from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
# primary_key default is non-null able field
# null=False → Prevents NULL values at the database level.
# blank=False → Prevents empty values in forms (for Django Forms and Admin Panel).
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    
    bio = models.TextField(max_length=500)
    website = models.URLField(max_length=100)
    country = models.CharField(max_length = 100)
    language = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    
    ROLE_CHOICES = [
        ("player", "Player"),
        ("problemsetter", "Problem Setter"),
        ("admin", "Admin"),
    ]
    
    role = models.CharField(choices=ROLE_CHOICES, default="player")
    
    def __str__(self):
        return f"[id: {self.id}] {self.name} {self.email}"
    
    def get_user_by_name(username):
        try:
            return User.objects.get(name=username)
        except:
            return None


class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"[team_id: {self.id}] {self.name}"

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="players")
    
    rank = models.PositiveIntegerField(default=0)
    total_point = models.PositiveIntegerField(default=0)

class Challenge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    
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


class ProblemSetter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    challenges = models.ManyToManyField(Challenge, related_name="problem_setters")
    ...

@receiver(post_save, sender=User)
def create_role_model(sender, instance, created, **kwargs):
    if created:
        if instance.role == "player":
            Player.objects.create(user=instance)
        elif instance.role == "problemsetter":
            ProblemSetter.objects.create(user=instance)
