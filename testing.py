# read the csv file and extract important data like dates and assignments

import csv 
from datetime import datetime, timedelta

def convertToDate(mo):
    dates = {'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    for key, value in dates.items():
        if key == mo:
            return value


def convertToJson(summary, descr, dom):
    today = datetime.today()
    start_time = datetime(today.year, int(convertToDate(dom['mo'])), 9, 6, 30, 0)
    end_time = start_time + timedelta(hours=1)

    event = {
        'summary': summary,                                       # Summary here
        'description': descr,                                     # Desciption here
        'start': {
        'dateTime': start_time.strftime("%Y-%m-%d %H:%M:%S"),   # Start time here
        'timeZone': 'America/Los_Angeles',
            },
        'end': {
        'dateTime': end_time.strftime("%Y-%m-%d %H:%M:%S"),
        'timeZone': 'America/Los_Angeles',
            },
        'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
                ],
            },
        }

    return event


with open('output.csv', 'r') as f:
    dates = ['Sept', 'Oct', 'Nov', 'Dec']
    dom = {'month': '', 'day': '', 'event': ""}
    inputfile = csv.reader(f)
    start_month = ''
    for row in inputfile:
        for i in dates:
        # does the current datelist item match anything in the string row?
            if i in str(row):
          #add the row splitting on whitespace to the test var
                if str(row).split(maxsplit=2)[0].strip("[',]") in dates:
                    dom['mo'] = str(row).split(maxsplit=2)[0].strip("[',]")
                    dom['day'] =  str(row).split(maxsplit=2)[1].strip("[',]")
                    summary = str(row).split(maxsplit=2)[2].strip("[',]")
                elif str(row).split(maxsplit=2)[0].strip("[',]") == 'Mid-Term':
                    summary = str(row).split(maxsplit=2)[0].strip("[']")
                    dom['mo'] = str(row).split()[5].strip("[',]")
                    dom['day'] = str(row).split()[6].strip("[',]")

                (convertToJson(summary, '', dom))
                




#print(str(event_array))

#return the dictionary for main_app.py to send to calendar