import random
import string
import base64
import hashlib
from pprint import pprint
import requests
import json

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))

code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')

url = f'https://my.casepeer.com/o/authorize/?response_type=code&code_challenge={code_challenge}&code_challenge_method=S256&client_id=vW1RcAl7Mb0d5gyHNQIAcH110lWoOW2BmWJIero8&redirect_uri=https://www.example.com/noexist/callback'
response = requests.get(url)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pprint(code_challenge)
    pprint(response)
    pprint(response.content)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
