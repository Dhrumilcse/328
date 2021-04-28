from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from nft.models import Nft
from django.conf import settings
from django.http.response import JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
import stripe
import random

#Log in required for buy view
@login_required
def buyView(request, id):
    all_nft = Nft.objects.all()
    random_nft = random.sample(list(all_nft), 3)
    nft = Nft.objects.get(id=id)

    context = {
        'nft': nft,
        'all_nft': random_nft
    }

    return render(request, 'buy.html', context)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'NFT',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': '9900',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

class SuccessView(TemplateView):
    template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'