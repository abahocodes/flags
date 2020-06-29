import requests
import string

abbreviations = [x+y for x in string.ascii_lowercase for y in string.ascii_lowercase]
for abbreviation in abbreviations:
    url = f'https://media.api-sports.io/flags/{abbreviation}.svg'
    r = requests.get(url)
    if r.status_code == 200:
        with open(f'{abbreviation}.svg', 'wb') as writer:
            writer.write(r.content)
            print(f'Downloaded file for country with abbreviation {abbreviation}')