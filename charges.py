# Charge resource
# Example of a charge request

# To get paid in cryptocurrency, you need to create a charge object and provide the user with a cryptocurrency address to which they must send cryptocurrency. Once a charge is created a customer must broadcast a payment to the blockchain before the charge expires.


payload = {
       "name": "Breadstackers LLC",
       "description": "Breadstackers Crypto Investments 101 ebook",
       "local_price": {
         "amount": "20.00",
         "currency": "USD"
       },
       "pricing_type": "fixed_price",
       "metadata": {
         "customer_id": "id_1337",
         "customer_name": "Adeeb Ahmed"
       },
       "redirect_url": "https://charge/completed/page",
       "cancel_url": "https://charge/canceled/page"
     }



     