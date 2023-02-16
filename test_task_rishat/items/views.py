import stripe
from test_task_rishat import settings
from django.http import JsonResponse
from django.views import View
from .models import Item
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyView(View):
    def post(self, request, *args, **kwargs):

        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'item_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                'item_id': item.id,
            },
            mode='payment',
            success_url='http://127.0.0.1:8000/success/',
            cancel_url='http://127.0.0.1:8000/cancel/',
        )

        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):

    template_name = 'success.html'


class CancelView(TemplateView):

    template_name = 'cancel.html'
