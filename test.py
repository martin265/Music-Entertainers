import stripe

# Set your Stripe secret key
stripe.api_key = 'sk_test_51M3Ja4CS2j2b9xFxwTMUlfxDbOMNg9rvkKtCHNMP0uFAYl8PvYh9RrkzIZiOvBZlPjswqyP1Md81GWWQTkI9tDdK001WK9hZ2F'

# Create a charge
try:
    charge = stripe.Charge.create(
        amount=1000,  # Amount in cents
        currency='usd',
        source='tok_visa',  # Replace with a valid token or card ID
        description='Example charge',
    )

    # Charge was successful
    print("Payment successful. Charge ID:", charge.id)

except stripe.error.CardError as e:
    # Card was declined
    error_info = e.json_body
    err_message = error_info['error']['message']
    print("Card was declined:", err_message)

except Exception as e:
    # Other errors
    print("An error occurred:", str(e))
