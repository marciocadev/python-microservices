#~/movie-service/app/api/service.py

import os
import httpx

CAST_SERVICE_HOST_URL = 'http://192.168.40.116:8080/api/v1/casts/'
url = os.environ.get('CAST_SERVICE_HOST_URL') or CAST_SERVICE_HOST_URL

def is_cast_present(cast_id: int):
    print(cast_id)
    print(url)
    r = httpx.get(f'{url}{cast_id}')
    return True if r.status_code == 200 else False