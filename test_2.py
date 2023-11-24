import stripe

# Set your secret key
stripe.api_key = "sk_test_51OFGafFuspposRdyZiOJojteaDcZnTVtiNdeXcifEkR4z2az10MAJtRWfHlvyEBygaYwo9CAecVLsB1nQ3NT4WYe00sokapQVl"

# Create a customer
customer = stripe.Customer.create(
    email="zaithwazonke@gmail.com",
    source="tok_visa"  # Use a test card token from Stripe
)

# Create a charge
charge = stripe.Charge.create(
    amount=1000,  # Amount in cents
    currency="usd",
    description="Example charge",
    customer=customer.id
)

print(f"Charge ID: {charge.id}")
