from django.urls import path
from . import challenges

urlpatterns = [
    path(
        "challenges/<str:category>/",
        challenges.challenges_by_category,
        name="challenges_by_category",
    ),
    path("challenges/", challenges.view_category, name="view_category"),
    path("challenges/create/", challenges.create_challenge, name="create_challenge"),
]
