import requests as reqs
import os
import sys


 url = input("Enter Link:")
 r = reqs.get(url)
 rstr = str(r.content)
 rstr = rstr[rstr.find("\\'ideoolink\\'"):rstr.find("\\'robotlink\\'")]
 rstr = rstr[rstr.find('"')+ 1:]
 link = rstr[:rstr.find('"')]
 link = "https:/"+link+rstr[rstr.find("xcdb")+4:rstr.find(".substring")-3]
 print(link)
 print("All downloads are complete")
