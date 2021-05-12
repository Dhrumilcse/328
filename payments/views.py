# Model
from nft.models import Nft

# View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

# Request, Response, Render, Decorators
from django.shortcuts import render
import requests, random
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

# Misc, Payment(Stripe)
from django.conf import settings
import stripe

@login_required
def buyView(request, id):
    """ Returns an item object to buy (given ID) and object list of recommended NFTs"""
    
    all_nft = Nft.objects.all()
    random_nft = random.sample(list(all_nft), 3)
    buy_nft = Nft.objects.get(id=id)

    # TODO: Basic Recommendation using tags

    context = {
        'buy_nft': buy_nft,
        'random_nft': random_nft,
    }

    return render(request, 'buy.html', context)

@csrf_exempt
def stripe_config(request):
    """ Stripe Setup, returns json containing public key """
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    """ Returns Json response containing session ID if successful """
    if request.method == 'GET':
        domain_url = 'https://nft328.herokuapp.com/'
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
    """ Redirects to success.html upon completion of payment """
    template_name = 'success.html'

class CancelledView(TemplateView):
    """ Redirects to cancelled.html upon cancelled payment """
    template_name = 'cancelled.html'