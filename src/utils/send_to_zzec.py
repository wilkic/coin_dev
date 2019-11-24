
import qrcode

import sys
sys.path.append('../libs')
import shapeshift as ss
import subprocess


########


# return address (just get some receive addr)
return_addr = 'example'
########


# create a destination (where you want funds to end up)
tmp_dest_addr_line = subprocess.Popen("zcash-cli getnewaddress", shell=True, stdout=subprocess.PIPE).stdout.read()
tmp_dest_addr = tmp_dest_addr_line.rstrip()

# create a transaction to that addr (with return specified)
resp = ss.create_normal_tx(tmp_dest_addr, 'btc', 'zec',return_address=return_addr)

# this is where the funds need to be sent
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

# Send btc to that qr... it'll show up in 
# one of your t_addrs


