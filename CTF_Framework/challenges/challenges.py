from django.http import JsonResponse
from .models import Challenges
from backend.models import User
from django.shortcuts import get_object_or_404
from backend.utils import login_required, check_fields
from django.http import HttpResponseBadRequest
import json

def main_challenges(request):
    print(request.method)
    if request.method == "GET":
        return view_challenges(request)
    elif request.method == "POST":
        return create_challenge(request)
    elif request.method == "PUT":
        return edit_challenge(request)
    elif request.method == "DELETE":
        return delete_challenge(request)
    return JsonResponse({"error": "Invalid request method."}, status=400)

@login_required
def view_challenges(request):
    category = request.GET.get('category')
    category_choices = [_[0].lower() for _ in Challenges.CHALLENGE_CATEGORIES]
    if not category or (category.lower() not in category_choices):
        return JsonResponse({"categories": category_choices}, status=200)
    
    return JsonResponse({"error": "Invalid request."}, status=400)

@login_required
def create_challenge(request):
    user = User.objects.get(id=request.session.get('user_id'))

    if user.role != "problemsetter":
        return JsonResponse({"error": "You are not a problem setter"}, status=403)

    parameters = json.loads(request.body)
    allowed_fields = ["title","description","points","category","difficulty","attachment"]
    
    if check_fields(parameters, allowed_fields):
        return JsonResponse({"error": "Please input all required parameters.", "allowed fields":allowed_fields}, status=400)

    challenge = Challenges.objects.create(
        title=parameters['title'],
        description=parameters['description'],
        points=parameters['points'],
        author=user,
        category=parameters['category'],
        difficulty=parameters['difficulty'],
        attachment="/media/" + parameters['attachment'],
    )
    
    print(f"==> {user} created challenges {challenge.id} {challenge.title}")
    return JsonResponse({"message": "Challenge created successfully", "challenge_id":challenge.id}, status=200)

# @login_required
def view_challenges_by_category(request, category):
    category_choices = [_[0] for _ in Challenges.CHALLENGE_CATEGORIES]
    print(category, type(category))
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
    if not data:
        return JsonResponse({"error": "Category not found"}, status=404)

    return JsonResponse(data, safe=False)



# @login_required


def edit_challenge(request):
    ...

# @login_required
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
