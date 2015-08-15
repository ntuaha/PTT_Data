# -*- coding: utf-8 -*-
#處理掉unicode 和 str 在ascii上的問題
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
import datetime


def dumpData(s):
  '''
  資料輸出
  '''
  year = int(s[0:4])
  month = int(s[4:6])
  day = int(s[6:8])
  d = datetime.datetime(year,month,day)
  start_dt = d.strftime("%Y-%m-%d 0:0:0")
  end_dt = (d+datetime.timedelta(days=1)).strftime("%Y-%m-%d 0:0:0")
  filename = '/home/aha/Project/PTT_Data/data/user_list/%s.csv.gz'%s.strip()
  e = 'psql -d ptt_user -c "\copy (select * from users_backup where record_time>=\'%s\' and record_time<\'%s\') to stdout WITH (FORMAT CSV, HEADER TRUE, FORCE_QUOTE *)"  | gzip > %s'%(start_dt,end_dt,filename)
  print e
  os.system(e)
  del_sql = 'psql -d ptt_user -c "delete from users_backup where record_time>=\'%s\' and record_time<\'%s\'"'%(start_dt,end_dt)
  os.system(del_sql)

def pushData(s):
  '''
  上傳到github
  '''
  GH_REF = 'github.com/ntuaha/PTT_Data.git'
  GH_TOKEN = os.environ.get('AHA_GITHUB_AUTH').strip()
  os.chdir('/home/aha/Project/PTT_Data/')
  os.system('git config user.name "ntuaha"');
  os.system('git config user.email "ntuaha@gmail.com"');
  os.system('git add .')
  os.system('git commit -m "Automatic commit %s.csv.gz"'%s)
  os.system('git push "https://ntuaha:' + GH_TOKEN +'@' + GH_REF + '" master');
  with open ('/home/aha/Project/PTT_Data/.gitignore','a+') as f:
    f.write('%s.csv.gz\n'%s.strip())
  #os.system('rm /home/aha/Project/PTT_Data/data/user_list/%s.csv.gz'%s.strip())


if __name__ == "__main__":
  dumpData(sys.argv[1])
#  pushData(sys.argv[1])


