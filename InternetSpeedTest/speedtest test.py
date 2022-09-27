import speedtest 
s = speedtest.Speedtest(secure=1)
upload_test = round((round(s.upload()) / 1048576), 2) #converts to Mb/s
print(upload_test)