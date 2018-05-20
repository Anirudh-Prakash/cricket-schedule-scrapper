#Code to add Event to google Calendar
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime


class event:
    
    def add_date(self,summary,starttime,endtime,description):
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = build('calendar', 'v3', http=creds.authorize(Http()))

        EVENT={ 'summary': summary,
                'start':{'dateTime':starttime} ,
                'end': {'dateTime':endtime },
                'description':description}

        event = service.events().insert(calendarId='primary', body=EVENT).execute()
        return (str(event.get('htmlLink')))

