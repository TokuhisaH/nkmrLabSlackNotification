# coding:utf-8
from __future__ import print_function
import httplib2
import os
import requests
import json
import re 

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from datetime import datetime, timedelta
 
import datetime

 
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
 
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'scopes'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'
 
 #認証情報
def get_credentials():
    """Gets valid user credentials from storage.
 
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
 
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')
 
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials
 
 #取得して通知するまで
def main():
    """Shows basic usage of the Google Calendar API.
 
    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

 
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='calenderId', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    slack_url='hooks.slack.com~'

    if not events:
        print('No upcoming events found.')
 
    now_str=str(datetime.datetime.now())
    now=datetime.datetime.now()
    print(now)
    

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        
        start_str=str(start[:4]+start[5:7]+start[8:10]+start[11:13]+start[14:16])
        
        
        try:
            start_time=datetime.datetime.strptime(start_str,'%Y%m%d%H%M')

            
        
            if len(start_str)>8 and str(start_time)[:10]==str(now)[:10]: #時間指定のない、日付の異なるイベントは無視する
                
                #print(start,event['summary'])
                td_start=start_time-now#イベントの開始時刻と現時刻の差分計算用
                
                #print(type(td_start))
                if td_start.seconds <= 600: #10分以内だったら通知飛ばす
                    schedule_time=start[:4]+"年"+start[5:7]+"月"+start[8:10]+"日 "+start[11:13]+"時"+start[14:16]+"分"
                    schedule_name=event['summary']
                    print(schedule_time,schedule_name)
                    
            

        

                    
                #    if datetime.(start[:4],start[5:7],start[8:10],start[11:13]:start[14:16]:0)=datetime.now() + timedelta(seconds=-15)
                    go=True
                    if go==True: #とりあえずSlackへの投稿を止めたいとき用
                        #徳久弘樹
                        if schedule_name.find("徳久")>=1 or schedule_name.find("M1")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m1_tokuhisa',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))
                            

                        #細谷
                        if schedule_name.find("細谷")>=1 or schedule_name.find("B3")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_hosoya',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))


                        #桑原
                        if schedule_name.find("桑原")>=1 or schedule_name.find("B3")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_kuwabara',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #南里
                        if schedule_name.find("南里")>=1 or schedule_name.find("B3")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_nanri',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))


                        #菅野
                        if schedule_name.find("菅野")>=1 or schedule_name.find("B3")>=1 or schedule_name.find("いっぺぇ")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_sugano',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #古市
                        if schedule_name.find("古市")>=1 or schedule_name.find("B3")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_furuichi',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))
                        
                        #木頃
                        if schedule_name.find("木頃")>=1 or schedule_name.find("B3")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_kigoro',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #松山
                        if schedule_name.find("松山")>=1 or schedule_name.find("B3")>=1 or schedule_name.find("まつけん")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_matsuyama',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #野中
                        if schedule_name.find("野中")>=1 or schedule_name.find("B3")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b3_nonaka',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))    
                        
                        
                        #上西
                        if schedule_name.find("上西")>=1 or schedule_name.find("B4")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b4_kaminishi',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 

                        #又吉
                        if schedule_name.find("又吉")>=1 or schedule_name.find("B4")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b4_matatsuna',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 
                        
                        #佐々木
                        if schedule_name.find("佐々木")>=1 or schedule_name.find("B4")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b4_mikako',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 
                
                        #水の
                        if schedule_name.find("水野")>=1 or schedule_name.find("B4")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b4_mizuno',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 


                        #斎藤
                        if schedule_name.find("斎藤")>=1 or schedule_name.find("光")>=1 or schedule_name.find("B4")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b4_saito',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 

                        #高橋
                        if schedule_name.find("高橋")>=1 or schedule_name.find("B4")>=1 or schedule_name.find("Otoniwa")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_b4_takahashi',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 

                        #阿部
                        if schedule_name.find("阿部")>=1 or schedule_name.find("M1")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m1_abe',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 

                        #樋川
                        if schedule_name.find("樋川")>=1 or schedule_name.find("M1")>=1 or schedule_name.find("Otoniwa")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m1_hikawa',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 


                        #絢基
                        if schedule_name.find("斉藤")>=1 or schedule_name.find("絢基")>=1 or schedule_name.find("M1")>=1 or schedule_name.find("Otoniwa")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m1_junki',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 


                        #山浦
                        if schedule_name.find("山浦")>=1 or schedule_name.find("M1")>=1 or schedule_name.find("Otoniwa")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m1_yamanotami',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 

                        #神山
                        if schedule_name.find("神山")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_karmine',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            })) 

                        #田島
                        if schedule_name.find("田島")>=1 or schedule_name.find("M2")>=1 or schedule_name.find("Uniotto")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_kazu',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                            
                        #白鳥
                        if schedule_name.find("白鳥")>=1 or schedule_name.find("M2")>=1 or schedule_name.find("Uniotto")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_yujishiratori',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #松田
                        if schedule_name.find("松田")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_kouhei_matsuda',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #田村
                        if schedule_name.find("田村")>=1 or schedule_name.find("M2")>=1 or schedule_name.find("Uniotto")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_masayuki',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'ジェスチャーマン', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))


                        #松井
                        if schedule_name.find("松井")>=1 or schedule_name.find("まつこ")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_matsuko',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #今城
                        if schedule_name.find("今城")>=1 or schedule_name.find("大野")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_naoki_imajo',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #新納
                        if schedule_name.find("新納")>=1 or schedule_name.find("M2")>=1 or schedule_name.find("Uniotto")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_ninoshin',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #前島
                        if schedule_name.find("前島")>=1 or schedule_name.find("レミ")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_remi',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #佐藤
                        if schedule_name.find("佐藤")>=1 or schedule_name.find("サトケン")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_satoken',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #土屋
                        if schedule_name.find("土屋")>=1 or schedule_name.find("駿貴")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_shunki',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))


                        #牧
                        if schedule_name.find("牧")>=1 or schedule_name.find("M2")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'ww_m2_youtubermaki',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))

                        #中村先生
                        if schedule_name.find("中村")>=1 or schedule_name.find("先生")>=1:
                            res = requests.post(slack_url, data = json.dumps({
                                'channel':'www_nakamura',
                                'text':"まもなく"+str(schedule_time)+"より、"+str(schedule_name)+ "です！！", # 投稿するテキスト
                                'username': u'予定お知らせbot', # 投稿のユーザー名
                                'icon_emoji': u':abe_guruguru:', # 投稿のプロフィール画像に入れる絵文字
                                'link_names': 1, # メンションを有効にする
                            }))
                    
        except:
            pass



if __name__ == '__main__':
    main()