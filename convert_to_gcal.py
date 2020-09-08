import csv 
import tabula
from datetime import datetime, timedelta
pdf_path = "c:/Users/cello/OneDrive/Documents/example_syllabus.pdf"
dfs = tabula.read_pdf(pdf_path, pages='all')
print(len(dfs))
tabula.convert_into(pdf_path, "output.csv", output_format="csv", pages='all')

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

def main():
  with open('output.csv', 'r') as f:
      dates = ['Sept', 'Oct', 'Nov', 'Dec']
      dom = {'month': '', 'day': '', 'event': ""}
      inputfile = csv.reader(f)
      start_month = ''
      for row in inputfile:
          for i in dates:
              if i in str(row):
                  if str(row).split(maxsplit=2)[0].strip("[',]") in dates:
                      dom['mo'] = str(row).split(maxsplit=2)[0].strip("[',]")
                      dom['day'] =  str(row).split(maxsplit=2)[1].strip("[',]")
                      summary = str(row).split(maxsplit=2)[2].strip("[',]")
                  elif str(row).split(maxsplit=2)[0].strip("[',]") == 'Mid-Term':
                      summary = str(row).split(maxsplit=2)[0].strip("[']")
                      dom['mo'] = str(row).split()[5].strip("[',]")
                      dom['day'] = str(row).split()[6].strip("[',]")

      return convertToJson(summary, '', dom)
                
if __name__ == "__main__":
    main()
