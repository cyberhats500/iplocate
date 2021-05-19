import pygeoip
print("HawkHackers")
print("The exact IP Location tracker")
print("[*] Use Google Earth to find Latitude and Longitude")
ip = input(print("Enter The Ip = "))
gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr(ip)
for key, val in res.items():
    print('%s : %s ' % (key,val))
print("DONE!!!")
