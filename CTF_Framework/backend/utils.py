from django.http import HttpResponseRedirect

def check_fields(input: dict, list: list) -> bool:
    for item in list:
        if not input.get(item):
            return True
    return False


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return HttpResponseRedirect("/login/")
        return view_func(request, *args, **kwargs)
    return wrapper
