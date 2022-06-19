from requests import *

def get_error_message(error_type):
    if error_type == 404:
        return 'red'
    if error_type == 403:
        return 'orange'
    if error_type == 401:
        return 'yellow'
    else:
        return 'blue'

def main():
    res = get('http://api.gethub.events')
    STATUS = res.status_code
    if res.ok:
        print(f"{STATUS}")
    else:
        print(get_error_message(STATUS))

if __name__ == '__main__':
    main()