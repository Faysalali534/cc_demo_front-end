from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

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
            print("this is response,", response[0])
            request.session['token'] = response[0]['token']
            request.session['account_id'] = response[0]['account_id']
            return redirect(reverse('portal'))
        context['message'] = response[0]
    return render(request, 'cc_app/index.html', context=context)


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
    if not request.session.get('token'):
        return redirect(reverse('index'))
    return render(request, 'cc_app/portal.html')


def logout(request):
    del request.session['token']
    del request.session['account_id']
    return redirect(reverse('index'))


def setting(request):
    context = dict()
    token = request.session.get('token')
    if not token:
        return redirect(reverse('index'))

    response = api.get_currency(token=token)
    if response[1]:
        context['currencies'] = response[0]
    if request.POST:
        start_date = request.POST.get("start_date")
        Currency = request.POST.get("currency_capture")
        end_date = request.POST.get("end_date")
        category = request.POST.get("category") or 'inverse'
        print("this is the date",start_date)
        print("this is the Currency",Currency)
        print("this is the end_date",end_date)
        print("this is the category",category)



    return render(request, 'cc_app/settings.html', context=context)
