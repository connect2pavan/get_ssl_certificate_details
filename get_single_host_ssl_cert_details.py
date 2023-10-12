import ssl
import socket
import datetime

#hostname = "google.com"
hostname = "*.adelaidenow.com.au"
hostname=hostname.lstrip('*.')
port = 443

context = ssl.create_default_context()
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()
        for key, value in cert.items():
            print(f"Key: {key}, Value: {value}")
        issued_on = datetime.datetime.strptime(cert["notBefore"], '%b %d %H:%M:%S %Y GMT')
        expires_on = datetime.datetime.strptime(cert["notAfter"], '%b %d %H:%M:%S %Y GMT')
        serial_number = cert.get('serialNumber')

print("Issued On:", issued_on)
print("Expires On:", expires_on)
print("serialNumber On:", serial_number)
