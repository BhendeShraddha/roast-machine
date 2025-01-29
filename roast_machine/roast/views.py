import random
from django.http import JsonResponse
from django.shortcuts import render

ROASTS = [
    "You're like a cloud. When you disappear, it's a beautiful day. ☀️",
    "You're proof that even evolution takes a step backward. 🦧",
    "If I had a dollar for every smart thing you said, I'd be broke. 💸",
    "You bring everyone so much joy… when you leave the room. 🚪",
    "Your secrets are safe with me. I never even listen when you tell me them. 😴",
]

def roast_me(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'roast': random.choice(ROASTS)})
    return render(request, 'roast/index.html')
