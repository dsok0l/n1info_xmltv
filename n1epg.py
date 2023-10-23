#! /usr/bin/python

import requests
import json
from datetime import datetime, timedelta


HOSTNAME = "api-web.ug-be.cdn.united.cloud"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsidWMtaW5mby1zZXJ2aWNlIl0sInNjb3BlIjpbInJlYWQiXSwiZXhwIjoxNjk3NDQyODczLCJhdXRob3JpdGllcyI6WyJST0xFX1BVQkxJQ19FUEciXSwianRpIjoiQ2xmZldvVE53R0taTi1rWDFxQVhkM25iOUVZIiwiY2xpZW50X2lkIjoiMjdlMTFmNWUtODhlMi00OGU0LWJkNDItOGUxNWFiYmM2NmY1In0.fhxlIAP8Kit6UzYzWyt2_ZcHgjmzVt9Az0PZ8GqQ5kA"
EPG_PATH = "/v1/public/events/epg"
COMMUNITY_ID = "n1_hr"
LANG_ID = "181"  # hr
CHANNEL_ID = "448"  # N1 HD (HR)
LIMIT_DAYS = 5  # TODO: add as command parameter
now = datetime.now()
increment = timedelta(days=LIMIT_DAYS)


def fetch_epg(fromTime, toTime, session=None):
    if not session:
        session = requests.Session()
    url = f'https://{HOSTNAME}{EPG_PATH}'
    headers = {'Accept': 'application/json',
               'X-UCP-TIME-FORMAT': 'timestamp',
               'Authorization': f'Bearer {TOKEN}'
               }
    params = {'cid': CHANNEL_ID,
              'fromTime': fromTime,
              'toTime': toTime,
              'communityIdentifier': COMMUNITY_ID,
              'languageId': LANG_ID
              }
    response = session.get(url, headers=headers, params=params)
    if response.ok:
        return response.content
    else:
        raise LookupError(response.raw)


def day_start_timestamp(datetime_obj):
    day_start = datetime_obj.replace(hour=0, minute=0, second=0, microsecond=0)
    return int(day_start.timestamp() * 1000)


def day_end_timestamp(datetime_obj):
    day_start = datetime_obj.replace(hour=23, minute=59, second=59, microsecond=999999)
    return int(day_start.timestamp() * 1000)




if __name__ == '__main__':
    epg_json = fetch_epg(day_start_timestamp(now),
                         day_end_timestamp(now + increment))
    print(epg_json)
    