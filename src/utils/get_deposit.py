
import qrcode

# ghetto : should change ss to a module (__init__.py in src)
import os, sys
sys.path.insert('../libs')
import shapeshift as ss


# destination (where you want funds to end up)
# $ withdrawl_addr = system('zcash-cli get_newaddress')
withdrawl_addr = 'tAddr'


# return address
# $ return_addr is provided by tx creator
return_addr = 'example'


# get address to deposit into
#resp = ss.create_normal_tx(withdrawl_addr, 'btc', 'zec',return_address=return_addr)
### temp: just so don't need to create a ss tx every time in dev
resp = {'deposit':return_addr}

deposit_addr = resp['deposit']


# Show deposit address as a QR code (png)
qr = qrcode.QRCode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )

qr.add_data(deposit_addr)
qr.make(fit=True)
img = qr.make_image()
img.save('send_here.png')


#
# Now, wait till funds show up in local withdrawl and
# ... once there, mark wallet for clean up later in the day
# ... Cleanup means transfering into a z - wallet
#
# TODO : come up with a smart way to do this
# zcash-cli getbalance $withdrawl_addr > tbal
# with open('tbal','r') as tb:
#    tbal = tb.read()
# zcash-cli z_sendmany $withdrawl_addr "[{\"address\":\"$ZADDR\",\"amount\":tbal}]"


# Take out more than you put in
# TODO use a real RNG : maybe os.urandom()
from random import *
mult = 1 + random()
# outgoing_addr = system('zcash-cli get_newaddress')
# TMP : TODO : use above... go to a new address
outgoing_addr = withdrawl_addr
tmp_wd = tbal * mult
# zcash-cli z_sendmany $ZADDR "[{\"address\":\"$outgoing_addr\",\"amount\":tmp_wd}]"


# Determine fees ( max of 1% )
fee = random() / 100
# Now just send the amount that was originally requested : minus fees
final_val = tbal - fee
# zcash-cli z_sendmany $outgoing_addr "[{\"address\":\"$final_destination_addr\",\"amount\":final_val}]"


# Mark that addr for cleanup later
# TODO : same smart thing needed here as above for later cleanup

