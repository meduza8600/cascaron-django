from django.shortcuts import redirect, reverse


def not_production(condition, redirect_to):
    def wrapper(view_func):
        def wrapped(request, *args, **kwargs):
            host = request.get_host()
            if condition in host:
                return redirect(reverse(redirect_to))
            else:
                return view_func(request, *args, **kwargs)

        return wrapped

    return wrapper
