from django.shortcuts import render

# Create your views here.

from cc_demo_frontend import api


def index(request):
    context = dict()
    if request.POST:
        password = request.POST.get("password")
        email = request.POST.get("email")
        response = api.login(
            password=password,
            username=email
        )
        if response[1]:
            print("this is response,",response[0])
            request.session['token'] = response[0]['token']
            request.session['account_id'] = response[0]['account_id']
            return render(request, 'cc_app/portal.html')
        context['message'] = response[0]
    return render(request, 'cc_app/index.html',context=context)


def sign_up(request):
    context = dict()
    if request.POST:
        api_key = request.POST.get("api_key")
        secret_key = request.POST.get("secret_key")
        first_name = request.POST.get("f_N")
        last_name = request.POST.get("l_n")
        password = request.POST.get("password")
        email = request.POST.get("email")

        response = api.register(
            api_key=api_key,
            secret_key=secret_key,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )

        context['message'] = response[0]
        return render(request, "cc_app/signup.html", context=context)

    return render(request, "cc_app/signup.html")


def portal(request):
    return render(request, 'cc_app/portal.html')
