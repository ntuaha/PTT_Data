__author__ = 'ESB13240'
#encoding=utf-8


import datetime
#處理掉unicode 和 str 在ascii上的問題
import sys
import json
import os
reload(sys)
sys.setdefaultencoding('utf8')


def parseContent(s):
    return "\"%s\""%str(s).replace("\"","\'")

def getDatetime(d):
    return datetime.datetime.fromtimestamp(long(d['$date']['$numberLong'])/1000)

if __name__=="__main__":
    '''
    輸入版名
    '''
    board = sys.argv[1].strip()
    os.chdir('/home/aha/Project/PTT_Data/data/article/')
    path = './%s.json'%board
    out_path = './%s.csv'%board
    out_path_push = './%s_push.csv'%board
    with open(path,'r') as f:
        data_json = json.loads("".join(f.readlines()),encoding="utf8")

    out_f = open(out_path,'w+')
    out_f.write(",".join(["id","author","author_ip","category","hot_level","time","title","content","link"])+"\n")

    with open(out_path_push,'w+') as f_push:
        f_push.write(",".join(["id","user","content","tag","push_time"])+"\n")
        for datum in data_json:
            d={}
        #    print datum['edittime']
            if len(datum['edittime'])>0:
                d["time"] = datum['edittime'][0]['$date'].split(".")[0].replace('T'," ")
                year = int(datetime.datetime.strptime(d["time"],"%Y-%m-%d %H:%M:%S").strftime("%Y"))
                d["author"] = datum['author']
                if len(datum['author_ip'])>0:
                    d["author_ip"] = datum['author_ip'][0]
                else:
                    d["author_ip"]=""
                d["title"] = datum['title']
                d["hot_level"] = len(datum['pushs'])
                if 'category' in datum:
                    d["category"] = datum['category']
                else:
                    d["category"] = ''
                d["link"] = datum['link']
                content = ''
                for c in datum['content']:
                    content = content+c['text']
                d["content"] = content.replace("\n","||")
                d["id"] = datum['_id']['$oid']
                #print d["id"]
                for push in datum['pushs']:
                    if 'user' in push:
                        push['user'] = push['user'].replace(":","")
                    else:
                        continue
                    if 'content' in push:
                        push['content'] = push['content'].replace(":","")
                    else:
                        push['content'] = ''

                    if 'tag' not in push:
                        push['tag'] = 0

                    if 'time' in push:
                        push['push_time'] = '%d-%s'%(year,getDatetime(push['time']).strftime('%m-%d %H:%M:%S'))
                    else:
                        push['push_time'] = ''
                    f_push.write(",".join(map(parseContent,[d['id'],push['user'].replace(":",""),push['content'].replace(":",""),push['tag'],push['push_time']]))+"\n");
                #data.append(d)
                out_f.write(",".join(map(parseContent,[d['id'],d["author"],d["author_ip"],d["category"],d["hot_level"],d["time"],d["title"],d["content"],d['link']]))+"\n")

    out_f.close()



