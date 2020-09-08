from apiclient.discovery import build
import pickle
from datetime import datetime, timedelta
from .convert_to_gcal import main

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)
result = service.calendarList().list().execute()
calendar_id = result['items'][1]['id']
result = service.events().list(calendarId=calendar_id).execute()
result['items'][0]


# either import this event dictionary(json) from a seperate file, or use it as a formattable template
event = main()
service.events().insert(calendarId=calendar_id, body=event).execute()
