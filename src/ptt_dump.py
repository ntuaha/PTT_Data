# -*- coding: utf-8 -*-
#處理掉unicode 和 str 在ascii上的問題
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')
import datetime


if __name__ == "__main__":
  a = ["Bank_Service", "CFP", "FUND", "ForeignEX", "Foreign_Inv", "IC-Card", "LOAN", "Lifeismoney", "boy-girl", "creditcard", "e-coupon", "finance", "food", "foreign_ex", "gay",  "tax"]
  print len(a)
  #a=['Bank_Service']
  for b in a:
    #os.system('mongoexport --db ptt --collection %s --jsonArray  --out /home/aha/Project/PTT_Data/data/article/%s.json'%(b,b))
    #print 'mongoexport --db ptt --collection %s --jsonArray  --out /home/aha/Project/PTT_Data/data/article/%s.json'%(b,b)
    os.system('python /home/aha/Project/PTT_Data/src/ptt_json2csv.py %s'%b)



