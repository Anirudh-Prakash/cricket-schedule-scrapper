import os
from flask import Flask, render_template, request
import scrapper
import Event
app=Flask(__name__)

@app.route('/')
def index():
    teams={'01':'India', '02':'Pakistan','03':'Australia', '04':'Sri Lanka','05':'Bangladesh', '06':'England',
           '07':'Windies', '08':'South Africa','09':'Zimbabwe', '10':'New Zealand','11':'Ireland', '12':'Afghanistan'}
    return render_template('index.html', teams=teams)
    

@app.route('/schedule', methods=['GET','POST'])
def schedule():
    team=request.form.get('team_select')
    sc=scrapper.Scrapper()
    items=sc.scrape(team)
    return render_template('schedule.html',content=items)
    
@app.route('/add_to_calendar',methods=['GET','POST'])
def calendar():
    summary=request.form.get('name_match')
    day=request.form.get('day')
    month=request.form.get('month')
    year=request.form.get('year')
    desc=request.form.get('name_tournament')
    t=request.form.get('time')
    time=t[0:5]
    if t[6:7] == 'P':
        time=str(int(t[:2])+12)+t[2:5]
        

    starttime=year+'-'+month+'-'+day+'T'+time+':00+05:30'

    if int(time[:2])+1 < 24:
        time=str(int(time[:2])+1)+time[2:5]
    else:
        time=str(int(time[:2])+1-24)+time[2:5]

    endtime=year+'-'+month+'-'+day+'T'+time+':00+05:30'

    e=Event.event()
    res=e.add_date(summary,starttime,endtime,desc)

    return render_template('success.html', link=res)
        
if __name__ == '__main__':
    host=os.environ.get('IP','127.0.0.1')
    port= int(os.environ.get('PORT', 5000))
    app.run(host=host,port=port)
