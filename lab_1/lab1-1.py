import requests  # εισαγωγή της βιβλιοθήκης

url = input('Please enter a valid url')  # προσδιορισμός του url

response = requests.get(url)
param = requests.get(url, timeout=2.01)
print(param)

print('Headers = ', response.headers ,'\n')
print('Server: ', response.headers.get('server') ,'\n')
print('Set-cookie: ', response.headers.get('set-cookie') ,'\n')
print('Expires: ', response.headers.get('expires') ,'\n')

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 10 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    more(html)
