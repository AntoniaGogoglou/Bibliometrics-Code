#!/usr/bin/env python

import cPickle as pickle
import time
import string
import json
import urllib2
import urllib
import os.path
import os
import sys
from pprint import pprint
from random import randint


appid= open('appID.txt', 'r').read().rstrip()
domid=2
subdomid=7

# form the query URL to MAS
#url = "http://academic.research.microsoft.com/json.svc/search?AppId=%s" % (appid, )
#url += "&StartIdx=1&EndIdx=10"
#url += "&ResultObjects=author"
#url += "&DomainID=%s" % (domid, )  
#url += "&SubDomainID=%s" % (subdomid, )  

with open('json_jounral6.txt', 'w') as outfile:
	outfile.write("")
for i in range(1, 76):
	kk = i+(i-1)*20
	url = "http://academic.research.microsoft.com/json.svc/search?AppId=%s" % (appid, )
	url += "&StartIdx=%s" % (kk)
	url += "&EndIdx=%s"   % (kk+20)
	url += "&ResultObjects=journal"
	url += "&DomainID=%s" % (domid, )  
	#url += "&SubDomainID=%s" % (subdomid, ) 
	#print "querying url: %s..." % (url, )
	js = json.load(urllib2.urlopen(url))
	#pprint(js)
	for jj in range(1,21):
		fullName=str(js["d"]["Journal"]["Result"][jj]["FullName"].encode("utf-8"))
        	shortName=str(js["d"]["Journal"]["Result"][jj]["ShortName"].encode("utf-8"))
		journalID=str(js["d"]["Journal"]["Result"][jj]["ID"])
		#journalISSN=str(js["d"]["Journal"]["Result"][jj]["ISSN"])
		with open('json_jounal6.txt', 'a') as f:
    			f.write("\"%s\"," % fullName)
                	f.write("\"%s\"," % shortName)
			f.write("%s" % journalID)
			#outfile.write("%s" % journalISSN)
			f.write("\n")
	js.clear()
	rr=randint(30,40)
        time.sleep(rr)

# perform request
#print "querying url: %s..." % (url, )
#j = json.load(urllib2.urlopen(url))

#print j
#print type(j)
#pprint(j)

# go down the results...
#rix = 0
#auth = js['d']['Author']['Result']
#while rix<=100:
#  auth = j['d']['Author']['Result'][rix]
#  rix+=1
#print auth
#print js['d']['Author']['Result'][0]['LastName']
#with open('json_author.txt', 'w') as outfile:
#    json.dump(js, outfile)

