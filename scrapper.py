import requests
from bs4 import BeautifulSoup

class Scrapper:

    def gen_link(self,team):
        team_link={'01':'http://www.cricbuzz.com/cricket-team/india/2/schedule',
                   '02':'http://www.cricbuzz.com/cricket-team/pakistan/3/schedule',
                   '03':'http://www.cricbuzz.com/cricket-team/australia/4/schedule',
                   '04':'http://www.cricbuzz.com/cricket-team/sri-lanka/5/schedule',
                   '05':'http://www.cricbuzz.com/cricket-team/bangladesh/6/schedule',
                   '06':'http://www.cricbuzz.com/cricket-team/england/9/schedule',
                   '07':'http://www.cricbuzz.com/cricket-team/windies/10/schedule',
                   '08':'http://www.cricbuzz.com/cricket-team/south-africa/11/schedule',
                   '09':'http://www.cricbuzz.com/cricket-team/zimbabwe/12/schedule',
                   '10':'http://www.cricbuzz.com/cricket-team/new-zealand/13/schedule',
                   '11':'http://www.cricbuzz.com/cricket-team/ireland/27/schedule',
                   '12':'http://www.cricbuzz.com/cricket-team/afghanistan/96/schedule'}

        return team_link[team]

    def scrape(self,team):
        page=requests.get(str(self.gen_link(team)))
        soup = BeautifulSoup(page.content, 'html.parser')

        page=soup.find_all('div',class_='cb-series-brdr')

        items=[]
        month={'Jan':'01', 'Feb':'02' ,'Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
        
        for x in page:
            d=(x.find('div',class_='schedule-date')).find('span')
            date=d.get_text()

            d1=x.find('a')
            name_match=d1.get_text().strip()
            d2=x.find('div',class_='text-gray')
            name_tournament=d2.get_text()
            d3=x.find('div',class_='text-gray cb-ovr-flo')
            name_venue=d3.get_text()
            mon=month[date[:3]]

            t=x.find('div',class_='cb-font-12 text-gray')
            if t != None:
                time=t.get_text().strip()[:8]+' GMT'
            
            dict_items={'date':date, 'name_match':name_match, 'name_tournament':name_tournament,
                  'name_venue':name_venue, 'time':time, 'month':mon, 'year': name_tournament[-4:], 'day':date[4:6]}
            items.append(dict_items)

        return(items)
