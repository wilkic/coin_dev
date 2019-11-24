
import sys
sys.path.append('../libs')
import shapeshift as ss
import subprocess

#######

# btc address where you want funds to go
# e.g. Jaxx
to_addr = 'example'


# Amount of zec to send
amt = 7.9

# ZADDR2
zaddr = 'zBLAH_use a sapling addr'

########

return_addr_line = subprocess.Popen("zcash-cli getnewaddress", shell=True, stdout=subprocess.PIPE).stdout.read()
return_addr = return_addr_line.rstrip()


#return_stdout = subprocess.Popen(['zcash-cli','getnewaddress'], shell=True, stdout=subprocess.PIPE)
#line = return_stdout.stdout.readline


resp = ss.create_normal_tx(to_addr, 'zec', 'btc',return_address=return_addr)

deposit_addr = resp['deposit']

cmd = "zcash-cli z_sendmany %s \"[{\\\"address\\\":\\\"%s\\\",\\\"amount\\\":%f}]\"" % (zaddr,deposit_addr,amt)

send_stdout = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in iter(send_stdout.stdout.readline,''):
    print line

print "Check 'https://shapeshift.io/#/status/%s' for status" % resp['orderId']

print "Return address: %s" % return_addr.rstrip()

f = open('outgoing_log.csv','a')
f.write('%s,%s,%s,%s,%f\n' % ( resp['orderId'].rstrip(), return_addr.rstrip(), deposit_addr.rstrip(), to_addr, amt ) )
f.close()

