import ssl 

address = ("wikipedia.org", 443)
certificate = ssl.get_server_certificate(address)
print(certificate)