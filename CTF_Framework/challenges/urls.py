from django.urls import path
from . import challenges

urlpatterns = [
    path("", challenges.main_challenges, name="main_challenges"), # CREATE + VIEW
    # path("challenges/create/", challenges.create_challenge, name="create_challenge"),
    # path(
    #     "challenges/<str:category>/",
    #     challenges.challenges_by_category,
    #     name="challenges_by_category",
    # ), # VIEW PER CATEGORIES
    # path("challenges/<int:id>/")
    # path("challenges/")
]
