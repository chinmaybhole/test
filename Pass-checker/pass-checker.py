import requests
tail = '61DDCC5E8A2DABEDE0F3B482CD9AEA9434D'
url = "https://api.pwnedpasswords.com/range/" + 'AAF4C'
# Pwned website uses k-anonymity so we give first 5
# char of our password
r = requests.get(url)
# In response the website will match the password(hashes) in its 
# database and returns remaining hash(tail) and its index.
print(r.text)
r = (line.split(':') for line in r.text.splitlines())
for h, count in r:
    if h == tail:
      print(count)
