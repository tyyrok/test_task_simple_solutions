import stripe

from app.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def get_session_id(price_id: str, quantity: int = 1) -> str:
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price_id, "quantity": quantity}],
        mode="payment"
    )

    try:
        session_id = session["id"]
    except ArithmeticError:
        pass
    return session_id


def create_stripe_product(
    name: str,
    currency: str = 'usd',
    amount: float = 1
) -> int:
    stripe.Product.create(name=name)

    price = stripe.Price.create(
        currency=currency,
        unit_amount=int(amount*100),  # converting price to cents
        product_data={"name": name},
    )
    try:
        price_id = price['id']
    except AttributeError:
        pass
    return price_id
