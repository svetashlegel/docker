import stripe
from django.conf import settings


def create_product(payment):
    stripe.api_key = settings.STRIPE_API_KEY

    product = stripe.Product.create(
        name='Оплата обучения',
        description=payment.cours,
    )
    print(payment.cours)
    print(payment.summ)
    product.save()
    price = stripe.Price.create(
        unit_amount=payment.summ * 10,
        currency="usd",
        recurring={"interval": "month"},
        product=product['id'],
    )
    price.save()
    return price['id']


def get_url(price):
    stripe.api_key = settings.STRIPE_API_KEY
    print(price)
    payment = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price,
                "quantity": 1,
            },
        ],
        mode="subscription",
    )
    return payment['url']
