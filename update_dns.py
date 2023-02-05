from datetime import datetime
import os
import requests

KEY = os.environ['API_KEY']
DOMAIN = os.environ['DOMAIN']
TYPE = 'A'


def get_ip():
    res = requests.get('https://wtfismyip.com/text')
    return res.text.strip()


def request(cmd, **kwargs):
    params = {
        'key': KEY,
        'format': 'json',
        'cmd': cmd
    }
    for key in kwargs:
        params[key] = kwargs[key]
    res = requests.get('https://api.dreamhost.com', params=params)
    res.raise_for_status()
    return res.json()


def list_dns():
    return request('dns-list_records')


def remove_dns(record, type, value):
    return request('dns-remove_record', record=record, type=type, value=value)


def add_dns(record, type, value):
    return request('dns-add_record', record=record, type=type, value=value, comment=datetime.now().__str__())


if __name__ == '__main__':
    my_ip = get_ip()
    entries = list_dns()
    need_update = True
    for domain in DOMAIN.split(','):
        found = False
        for entry in entries['data']:
            if entry['type'] == TYPE and entry['record'] == domain:
                found = True
                if entry['value'] != my_ip:
                    # Need to update
                    remove_dns(entry['record'], entry['type'], entry['value'])
                    break
                else:
                    need_update = False
        if not found or need_update:
            print('Updating {} IP to {}'.format(domain, my_ip))
            add_dns(domain, TYPE, my_ip)
        else:
            print('No change for {}'.format(domain))
