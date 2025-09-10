import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + f'{query_char}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching {response.status_code}, check the api and try again')
    return response

def get_password_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            print(count)
            return count
    return 0

def pwned_api_check(password):
    #check pass if it exisiet in api responsshe
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #print(f'sha1password = {sha1password}')
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
                print(f'{password} was found {count} times ... you should change passwords')
        else:
            print(f'{password} was not found ... try again')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(['yummy']))







