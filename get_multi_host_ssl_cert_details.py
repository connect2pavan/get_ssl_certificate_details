import ssl
import socket
import json
import datetime
from tabulate import tabulate

# List of host names
host_names = [
    'news.com.au', '*.adelaidenow.com.au', '*.api.news', '*.bestrecipes.com.au', '*.cnivogue.com.au', '*.gq.com.au',
    '*.heraldsun.com.au', '*.kidspot.com.au', '*.myaccount.newsconcierge.com.au', '*.newcastlenewslocal.com.au',
    '*.news.com.au', '*.news.net.au', '*.newsadds.com.au', '*.newscdn.com.au', '*.newsconcierge.com.au',
    '*.placemyad.com.au', '*.savvyshopper.net.au', '*.talk.news.com.au', '*.taste.com.au', '*.theaustralian.com.au',
    '*.thechronicle.com.au', '*.vogue.com.au', 'adelaidenow.com.au', 'api.coles.taste.nlm.io', 'api.img.nlm.io',
    'assets-samp.nlm.io', 'bestrecipes.com.au', 'beta.couriermail.com.au', 'beta.dailytelegraph.com.au',
    'bodyandsoul.com.au', 'cairnspost.com.au', 'cdn.newsapi.com.au', 'couriermail.com.au', 'dailytelegraph.com.au',
    'delicious.com.au', 'escape.com.au', 'futureenergysummit.com.au', 'geelongadvertiser.com.au',
    'goldcoastbulletin.com.au', 'gq.com.au', 'greataustraliandreams.com.au', 'heraldsun.com.au', 'img.delicious.com.au',
    'insights.whimn.com.au', 'intheknow.com.au', 'kidspot.com.au', 'm.weather.news.com.au', 'newsadds.com.au',
    'newsconcierge.com.au', 'newscorpaustralia.com', 'newsxtend.com.au', 'ntnews.com.au', 'placemyad.com.au',
    'resources.news.com.au', 'taste.com.au', 'theaustralian.com.au', 'thechronicle.com.au', 'themercury.com.au',
    'townsvillebulletin.com.au', 'vogue.com.au', 'weeklytimesnow.com.au', 'whimn.com.au', 'www.1degree.com.au',
    'www.bodyandsoul.com.au', 'www.cairnspost.com.au', 'www.couriermail.com.au', 'www.dailytelegraph.com.au',
    'www.delicious.com.au', 'www.escape.com.au', 'www.futureenergysummit.com.au', 'www.geelongadvertiser.com.au',
    'www.goldcoastbulletin.com.au', 'www.greataustraliandreams.com.au', 'www.intheknow.com.au', 'www.nativeincolour.com.au',
    'www.newscorpaustralia.com', 'www.newsprestigenetwork.com.au', 'www.newsxtend.com.au', 'www.ntnews.com.au',
    'www.themercury.com.au', 'www.townsvillebulletin.com.au', 'www.weeklytimesnow.com.au', 'www.whereilive.com.au',
    'www.whimn.com.au', 'www.yourvoice2023.com.au', 'yourvoice2023.com.au'
]

# Function to retrieve certificate information
def get_certificate_info(host):
    try:
        context = ssl.create_default_context()
        hostname=host.lstrip('*.')
        port=443
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                serial_number = cert.get('serialNumber', 'NA')
                #issued_date = datetime.datetime.strptime(cert["notBefore"], '%b %d %H:%M:%S %Y GMT')
                #expiry_date = datetime.datetime.strptime(cert["notAfter"], '%b %d %H:%M:%S %Y GMT')
                issued_date = datetime.datetime.strptime(cert.get('notBefore'), "%b %d %H:%M:%S %Y %Z")
                expiry_date = datetime.datetime.strptime(cert.get('notAfter'), "%b %d %H:%M:%S %Y %Z")
                return serial_number, issued_date, expiry_date
    except Exception as e:
        string = str(e)
        part1 = string[:len(string)//3]
        part2 = string[len(string)//3:2*(len(string)//3)]
        part3 = string[2*(len(string)//3):]
        return part1, part2, part3
# Create a list to store certificate information
certificate_info = []

# Iterate through the host names and retrieve certificate information
for host in host_names:
    serial_number, issued_date, expiry_date = get_certificate_info(host)
    certificate_info.append({
        "Hostname": host,
        "Serial Number": serial_number,
        "Issued Date": issued_date,
        "Expiry Date": expiry_date
    })

# Print the certificate information in a table format
print(tabulate(certificate_info, headers="keys", tablefmt="grid"))


            
            
'''

import ssl
import socket
import datetime

hostname = "news.com.au"
port = 443

context = ssl.create_default_context()
with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        cert = ssock.getpeercert()
        for key, value in cert.items():
            print(f"Key: {key}, Value: {value}")
            
            
Key: subject, Value: ((('countryName', 'AU'),), (('stateOrProvinceName', 'New South Wales'),), (('localityName', 'Surry Hills'),), (('organizationName', 'News Corp Australia Pty Limited'),), (('commonName', 'news.com.au'),))
Key: issuer, Value: ((('countryName', 'US'),), (('organizationName', 'DigiCert Inc'),), (('commonName', 'DigiCert TLS RSA SHA256 2020 CA1'),))
Key: version, Value: 3
Key: serialNumber, Value: 05F2D27CF575681A7EC66DED894B057C
Key: notBefore, Value: Sep 12 00:00:00 2023 GMT
Key: notAfter, Value: Sep 12 23:59:59 2024 GMT
Key: subjectAltName, Value: (('DNS', 'news.com.au'), ('DNS', '*.adelaidenow.com.au'), ('DNS', '*.api.news'), ('DNS', '*.bestrecipes.com.au'), ('DNS', '*.cnivogue.com.au'), ('DNS', '*.gq.com.au'), ('DNS', '*.heraldsun.com.au'), ('DNS', '*.kidspot.com.au'), ('DNS', '*.myaccount.newsconcierge.com.au'), ('DNS', '*.newcastlenewslocal.com.au'), ('DNS', '*.news.com.au'), ('DNS', '*.news.net.au'), ('DNS', '*.newsadds.com.au'), ('DNS', '*.newscdn.com.au'), ('DNS', '*.newsconcierge.com.au'), ('DNS', '*.placemyad.com.au'), ('DNS', '*.savvyshopper.net.au'), ('DNS', '*.talk.news.com.au'), ('DNS', '*.taste.com.au'), ('DNS', '*.theaustralian.com.au'), ('DNS', '*.thechronicle.com.au'), ('DNS', '*.vogue.com.au'), ('DNS', 'adelaidenow.com.au'), ('DNS', 'api.coles.taste.nlm.io'), ('DNS', 'api.img.nlm.io'), ('DNS', 'assets-samp.nlm.io'), ('DNS', 'bestrecipes.com.au'), ('DNS', 'beta.couriermail.com.au'), ('DNS', 'beta.dailytelegraph.com.au'), ('DNS', 'bodyandsoul.com.au'), ('DNS', 'cairnspost.com.au'), ('DNS', 'cdn.newsapi.com.au'), ('DNS', 'couriermail.com.au'), ('DNS', 'dailytelegraph.com.au'), ('DNS', 'delicious.com.au'), ('DNS', 'escape.com.au'), ('DNS', 'futureenergysummit.com.au'), ('DNS', 'geelongadvertiser.com.au'), ('DNS', 'goldcoastbulletin.com.au'), ('DNS', 'gq.com.au'), ('DNS', 'greataustraliandreams.com.au'), ('DNS', 'heraldsun.com.au'), ('DNS', 'img.delicious.com.au'), ('DNS', 'insights.whimn.com.au'), ('DNS', 'intheknow.com.au'), ('DNS', 'kidspot.com.au'), ('DNS', 'm.weather.news.com.au'), ('DNS', 'newsadds.com.au'), ('DNS', 'newsconcierge.com.au'), ('DNS', 'newscorpaustralia.com'), ('DNS', 'newsxtend.com.au'), ('DNS', 'ntnews.com.au'), ('DNS', 'placemyad.com.au'), ('DNS', 'resources.news.com.au'), ('DNS', 'taste.com.au'), ('DNS', 'theaustralian.com.au'), ('DNS', 'thechronicle.com.au'), ('DNS', 'themercury.com.au'), ('DNS', 'townsvillebulletin.com.au'), ('DNS', 'vogue.com.au'), ('DNS', 'weeklytimesnow.com.au'), ('DNS', 'whimn.com.au'), ('DNS', 'www.1degree.com.au'), ('DNS', 'www.bodyandsoul.com.au'), ('DNS', 'www.cairnspost.com.au'), ('DNS', 'www.couriermail.com.au'), ('DNS', 'www.dailytelegraph.com.au'), ('DNS', 'www.delicious.com.au'), ('DNS', 'www.escape.com.au'), ('DNS', 'www.futureenergysummit.com.au'), ('DNS', 'www.geelongadvertiser.com.au'), ('DNS', 'www.goldcoastbulletin.com.au'), ('DNS', 'www.greataustraliandreams.com.au'), ('DNS', 'www.intheknow.com.au'), ('DNS', 'www.nativeincolour.com.au'), ('DNS', 'www.newscorpaustralia.com'), ('DNS', 'www.newsprestigenetwork.com.au'), ('DNS', 'www.newsxtend.com.au'), ('DNS', 'www.ntnews.com.au'), ('DNS', 'www.themercury.com.au'), ('DNS', 'www.townsvillebulletin.com.au'), ('DNS', 'www.weeklytimesnow.com.au'), ('DNS', 'www.whereilive.com.au'), ('DNS', 'www.whimn.com.au'), ('DNS', 'www.yourvoice2023.com.au'), ('DNS', 'yourvoice2023.com.au'))
Key: OCSP, Value: ('http://ocsp.digicert.com',)
Key: caIssuers, Value: ('http://cacerts.digicert.com/DigiCertTLSRSASHA2562020CA1-1.crt',)
Key: crlDistributionPoints, Value: ('http://crl3.digicert.com/DigiCertTLSRSASHA2562020CA1-4.crl', 'http://crl4.digicert.com/DigiCertTLSRSASHA2562020CA1-4.crl')

'''
