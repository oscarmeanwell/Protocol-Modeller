import requests
Breaker = True
Choice = input("\nDo you want to view the specs for SMTP (S), IMAP (I), TELNET (T), Or FTP (F): ").upper()
print()
print()
if Choice == "S":
    url = "https://www.ietf.org/rfc/rfc2821.txt"
    
elif Choice == "I":
    url = "http://tools.ietf.org/html/rfc3501"
    
elif Choice == "T":
    url = "http://tools.ietf.org/html/rfc854"

elif Choice == "F":
    url = "https://www.ietf.org/rfc/rfc959.txt"

else:
    print("\nPlease enter ever S, I, T, OR F!")
    Breaker = False

if Breaker:
    request = requests.get(url)
    print(request.text.strip())
