import os
#os.system("echo 'deb http://deb.torproject.org/torproject.org #wheezy main' >> /etc/apt/sources.list")
#os.system("gpg --keyserver keys.gnupg.net --recv 886DDD89")
#os.system("gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -")
#os.system("apt-get update")
#os.system("apt-get install deb.torproject.org-keyring")
#######INSTALL TOR & PRIVOXY ############
try:
	os.system("apt-get install tor -y")
	print 'Tor installed successful...\n'
except:
	print 'Tor intallation failed!'
	exit
try:
	os.system('apt-get install privoxy -y')
	print 'Privoxy installed successful...\n'
except:
	print 'Privoxy intallation failed!'
	exit
#try:
#	os.system('apt-get install vidalia -y')
#	print 'Vidalia installed successful...\n'
#except:
#	print 'Vidalia intallation failed!'
#	exit

#######SET CONFIGURATION FILE#################
try:
	with open('/etc/privoxy/config','w') as privoxy_conf_file, open('privoxy_conf','r') as conf_file:
		privoxy_conf_file.write(conf_file.read())
		privoxy_conf_file.close()
		conf_file.close()
	print 'Configuration file changed successful...\n'
except Exception as e:
	print 'Configuration file failed!'
	print e
	exit
#######START TOR##########################
try:
	os.system('service tor start')
	print 'Tor start on Socks5 port 9050 successful...\n'
except:
	print 'Tor start failed!'
	exit

#######START PRIVOXY######################
try:
	os.system('service privoxy start')
	print 'Privoxy start successful...\n'
except: 
        print 'Privoxy start failed!'
        exit

os.system('service tor restart')
os.system('service privoxy restart')

print 'Proxy tools has been installed succesful!'
print "Don't forget to set network settings:"
print 'HTTP:	127.0.0.1	8118'
print 'HTTPS:	127.0.0.1	8118'
print 'Socks:	127.0.0.1	9050'
exit


