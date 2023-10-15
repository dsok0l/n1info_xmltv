#! /usr/bin/python

import requests
import json


HOSTNAME = "api-web.ug-be.cdn.united.cloud"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsidWMtaW5mby1zZXJ2aWNlIl0sInNjb3BlIjpbInJlYWQiXSwiZXhwIjoxNjk3NDQyODczLCJhdXRob3JpdGllcyI6WyJST0xFX1BVQkxJQ19FUEciXSwianRpIjoiQ2xmZldvVE53R0taTi1rWDFxQVhkM25iOUVZIiwiY2xpZW50X2lkIjoiMjdlMTFmNWUtODhlMi00OGU0LWJkNDItOGUxNWFiYmM2NmY1In0.fhxlIAP8Kit6UzYzWyt2_ZcHgjmzVt9Az0PZ8GqQ5kA"
EPG_PATH = "/v1/public/events/epg"
COMMUNITY_ID = "n1_hr"
LANG_ID = "181"  # hr
CHANNEL_ID = "448"  # N1 HD (HR)


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
        print(response.content)
    else:
        raise LookupError(response.raw)


if __name__ == '__main__':
    fetch_epg("1697320800000", "1697407199999")