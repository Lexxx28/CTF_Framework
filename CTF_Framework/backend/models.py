from django.db import models

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


# class Player(User):
#     ...
    
# class ProblemSetter(User):
#     ...
    


# class Team(models.Model):
#     ...
    
# class Challenge(models.Model):
#     ...