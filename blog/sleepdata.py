import fitbit
import datetime
import pandas as pd
from ast import literal_eval

# tokenファイルを上書きする関数
def updateToken(token):
    f = open(TOKEN_FILE, 'w')
    f.write(str(token))
    f.close()
    return

# ユーザ情報の定義
CLIENT_ID =  '23BLMQ'
CLIENT_SECRET  = '7866106913a8621c649162cb20e6e942'
TOKEN_FILE = "token.txt"

# ファイルからtoken情報を読み込む
tokens = open(TOKEN_FILE).read()
token_dict = literal_eval(tokens)
access_token = token_dict['access_token']
refresh_token = token_dict['refresh_token']

# .FitbitでClient情報を取得
# refresh_cbに関数を定義する事で期限切れのtokenファイルを自動更新する
client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET,
                       access_token = access_token,
                       refresh_token = refresh_token,
                       refresh_cb = updateToken)

# 日付
now = datetime.datetime.now()
today = str(now.year) + "-" + str(now.month) + "-" + str(now.day)

#今日のデータが取れなかったとき用
#today='2021-10-28'

# 睡眠時間情報の取得
dataTxt = str(client.sleep(date = today))

#睡眠情報の表示
print(dataTxt)

#睡眠時間の長さ
minutesAsleepAd = dataTxt.find('minutesAsleep')
minutesAsleep = dataTxt[minutesAsleepAd+16:minutesAsleepAd+19]

#ベッドにいた長さ
timeInBedAd = dataTxt.find('timeInBed')
timeInBed = dataTxt[timeInBedAd+12:timeInBedAd+15]

#中途覚醒時間の長さ(=minutesAwake-minutesToFallAsleep-minutesAfterWakeup)
#minutesAwakeAd = dataTxt.find('minutesAwake')
#minutesToFallsleepAd=dataTxt.find('minutesToFallAsleep')
#minutesAfterWakeupAd=dataTxt.find('minutesAfterWakeup')

#minutesAwake = dataTxt[minutesAwakeAd+15:minutesAwakeAd+17]
#minutesToFallAsleep=dataTxt[minutesToFallsleepAd+22:minutesToFallsleepAd+23]
#minutesAfterWakeup=dataTxt[minutesAfterWakeupAd+21:minutesAfterWakeupAd+22]

#文字データを数値データに変換
#minutesAwake=int(minutesAwake)
#minutesToFallAsleep=int(minutesToFallAsleep)
#minutesAfterWakeup=int(minutesAfterWakeup)

minutesAsleep=int(minutesAsleep)
timeInBed=int(timeInBed)

#睡眠効率
sleepefficiency=minutesAsleep/timeInBed*100
print(minutesAsleep)
print(timeInBed)

#文字データにして小数点以下切り捨て
sleepefficiency=int(sleepefficiency)

#minutesAwaketime=minutesAwake-minutesToFallAsleep-minutesAfterWakeup

#print(minutesAsleep)
#print(minutesAwaketime)

print(sleepefficiency)