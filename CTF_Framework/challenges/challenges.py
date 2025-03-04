from django.http import JsonResponse
from .models import Challenges
from backend.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest


@login_required
def challenges_by_category(request, category):
    category_choices = [_[0] for _ in Challenges.CHALLENGE_CATEGORIES]
    if category not in category_choices:
        return JsonResponse({"error": "Invalid category"}, status=404)

    challenges = get_object_or_404(Challenges, category=category)

    data = []

    for challenge in challenges:
        data.append(
            {
                "id": challenge.id,
                "title": challenge.title,
                "description": challenge.description,
                "points": challenge.points,
                "author": User.objects.get(id=challenge.author).name,
                "category": challenge.category,
                "difficulty": challenge.difficulty,
                "solve_count": challenge.solve_count,
                "attachment": challenge.attachment,
                "upvote": challenge.upvote,
                "downvote": challenge.downvote,
            }
        )
    if data == []:
        return JsonResponse({"error": "Category not found"}, status=404)

    return JsonResponse(data, safe=False)


@login_required
def view_category(request):
    category_choices = [_[0] for _ in Challenges.CHALLENGE_CATEGORIES]
    return JsonResponse({"categories": category_choices})


@login_required
def create_challenge(request):
    if request.method != "POST":
        return JsonResponse({"Error": "Invalid request method"}, status=405)

    user = User.objects.get(username=request.user.username)

    if user.role != "problemsetter":
        return JsonResponse({"error": "You are not a problem setter"}, status=403)

    title = request.POST.get("title")
    description = request.POST.get("description")
    points = request.POST.get("points")
    author = user.id
    category = request.POST.get("category")
    difficulty = request.POST.get("difficulty")
    attachment = request.POST.get("attachment")

    challenge = Challenges(
        title=title,
        description=description,
        points=points,
        author=author,
        category=category,
        difficulty=difficulty,
        attachment="/media/" + attachment,
    )
    challenge.save()
    return JsonResponse({"message": "Challenge created successfully"}, status=200)


@login_required
def delete_challenge(request):
    if request.method != "DELETE":
        return HttpResponseBadRequest()

    challenge_id = request.POST.get("id")
    challenge = Challenges.objects.get(id=challenge_id)

    if challenge is None:
        return JsonResponse({"error": "Challenge not found"}, status=400)

    if challenge.author != request.user.id:
        return JsonResponse(
            {"error": "You are not the author of this challenge"}, status=403
        )

    challenge.delete()
    return JsonResponse({"message": "Challenge deleted successfully"}, status=200)
