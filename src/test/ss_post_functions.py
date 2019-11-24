def _shapeshift_post_request(url_path, payload):
    url = BASE_URL % url_path
    response = requests.post(url, data=payload)
    return response.json()

def create_normal_tx(withdrawal_address, input_coin, output_coin,
         return_address=None, destination_tag=None, 
         rs_address=None, api_key=None):
    url_path = "shift"     
    payload = {
        'withdrawal': withdrawal_address,
        'pair': "{}_{}".format(input_coin, output_coin),
        'returnAddress': return_address,
        'destTag': destination_tag,
        'rsAddress': rs_address,
        'apiKey': api_key
    }
    payload = {k: v for k,v in payload.items() if v is not None}    
    return _shapeshift_post_request(url_path, payload)

def request_email_receipt(email, tx_id):
    url_path = "mail"
    payload = {
        'email': email,
        'txid': tx_id
    }
    return _shapeshift_post_request(url_path, payload)
  
def create_fixed_amount_tx(amount, withdrawal_address, input_coin, 
        output_coin, return_address=None, destination_tag=None, 
        rs_address=None, api_key=None):
    
    url_path = "sendamount"
    payload = {
        'amount': amount,
        'withdrawal': withdrawal_address,
        'pair': "{}_{}".format(input_coin, output_coin),
        'returnAddress': return_address,
        'destTag': destination_tag,
        'rsAddress': rs_address,
        'apiKey': api_key
    }
    payload = {k: v for k,v in payload.items() if v is not None} 
    return _shapeshift_post_request(url_path, payload)
  
def cancel_tx(address):
    url_path = "cancelpending"
    payload = {
        'address': address,
    }
    return _shapeshift_post_request(url_path, payload)


