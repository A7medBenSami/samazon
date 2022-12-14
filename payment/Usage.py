from accept.payment import *

API_KEY = "ZXlKaGJHY2lPaUpJVXpVeE1pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmpiR0Z6Y3lJNklrMWxjbU5vWVc1MElpd2libUZ0WlNJNkltbHVhWFJwWVd3aUxDSndjbTltYVd4bFgzQnJJam8yTWpJNE1UQjkuTnNEVHNsTlgwYVg3ck5GUy1IX2NWUF85LVM3a1V3YjhST295czlyQkkzc1ktRGNFYVpQczA5cFlqWUhNOTJ1cGlSSUVGd0NFUGNZZS13Q3Z2UW40VHc="

accept = AcceptAPI(API_KEY)

# Authentication Request
auth_token = accept.retrieve_auth_token()
print(auth_token)

# Order Registration
OrderData = {
    "auth_token": auth_token,
    "delivery_needed": "false",
    "amount_cents": "1100",
    "currency": "EGP",
    "merchant_order_id": 622810,  # UNIQUE
    "items": [
        {
            "name": "ASC1515",
            "amount_cents": "500000",
            "description": "Smart Watch",
            "quantity": "1"
        },
        {
            "name": "ERT6565",
            "amount_cents": "200000",
            "description": "Power Bank",
            "quantity": "1"
        }
    ],
    "shipping_data": {
        "apartment": "803",
        "email": "claudette09@exa.com",
        "floor": "42",
        "first_name": "Clifford",
        "street": "Ethan Land",
        "building": "8028",
        "phone_number": "+86(8)9135210487",
        "postal_code": "01898",
        "extra_description": "8 Ram , 128 Giga",
        "city": "Jaskolskiburgh",
        "country": "CR",
        "last_name": "Nicolas",
        "state": "Utah"
    },
    "shipping_details": {
        "notes": " test",
        "number_of_packages": 1,
        "weight": 10,
        "weight_unit": "Kilogram",
        "length": 100,
        "width": 100,
        "height": 100,
        "contents": "product of some sorts"
    }
}
order = accept.order_registration(OrderData)
print(order)

# Payment Key Request
Request = {
    "auth_token": auth_token,
    "amount_cents": "1500",
    "expiration": 3600,
    "order_id": order.get("id"),
    "billing_data": {
        "apartment": "803",
        "email": "claudette09@exa.com",
        "floor": "42",
        "first_name": "Clifford",
        "street": "Ethan Land",
        "building": "8028",
        "phone_number": "+86(8)9135210487",
        "shipping_method": "PKG",
        "postal_code": "01898",
        "city": "Jaskolskiburgh",
        "country": "CR",
        "last_name": "Nicolas",
        "state": "Utah"
    },
    "currency": "EGP",
    "integration_id": 3078702,  # https://accept.paymob.com/portal2/en/PaymentIntegrations
    "lock_order_when_paid": "false"
}
payment_token = accept.payment_key_request(Request)
print(payment_token)

# Payments API [Kiosk, Mobile Wallets , Cash, Pay With Saved Token]
identifier = "cash"
payment_method = "CASH"
transaction = accept.pay(identifier, payment_method, payment_token)
print(transaction)

# Auth-Capture Payments
transaction00 = accept.capture_transaction(transaction_id="123", amount_cents=1000)
print(transaction00)

# Refund Transaction
transaction01 = accept.refund_transaction(transaction_id="123", amount_cents=10)
print(transaction01)

# Void Transaction
transaction02 = accept.void_transaction(transaction_id="123")
print(transaction02)

# Retrieve Transaction
transaction03 = accept.retrieve_transaction(transaction_id="123")
print(transaction03)

# Inquire Transaction
transaction_inquire = accept.inquire_transaction(merchant_order_id="622810", order_id="1221")
print(transaction_inquire)

# Tracking
order_10883471_track = accept.tracking(order_id="10883471")
print(order_10883471_track)

# Preparing Package
# This will return a pdf file url to be printed.
package = accept.preparing_package(order_id="10883471")
print(package)

# IFrame URL
iframeURL = accept.retrieve_iframe(iframe_id="699644", payment_token=payment_token)
print(iframeURL)

# Loyalty Checkout
response = accept.loyalty_checkout(transaction_reference='', otp='622810', payment_token=payment_token)
print(response)