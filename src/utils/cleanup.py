
import sys
sys.path.append('../libs')
import shapeshift as ss
import subprocess
import json
import ipdb

###
def cloak(tAddr,amt):
    amt_to_xfer = amt - tx_fee
    cmd = "zcash-cli z_sendmany %s \"[{\\\"address\\\":\\\"%s\\\",\\\"amount\\\":%.8f}]\"" % (tAddr,zaddr,amt_to_xfer)
    send_stdout = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    #for line in iter(send_stdout.stdout.readline,''):
    #    print line

###

#######


# ZADDR2
zaddr = 'USE A SAPLING ADDR'

tx_fee = 0.0001


########
fout = '../../logs/taddrs.json'
return_addr_line = subprocess.Popen("zcash-cli listaddressgroupings > " + fout, shell=True, stdout=subprocess.PIPE).stdout.read()

with open(fout) as json_data:
    d = json.load(json_data)

for a in d:
    for aa in a:
        if aa[1] > 0:
            cloak(aa[0],aa[1])
            #ipdb.set_trace()
            print '%s, %.8f' % (aa[0],aa[1])



