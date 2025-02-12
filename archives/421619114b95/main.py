from copy import *

class Record:
    contest = ""
    school = ""
    score = ""
    rank = ""
    province = ""
    prize = ""
    
class Oier:
    uid = ""
    enname = ""
    zhname = ""
    # man 1 woman -1
    gender = ""
    year = ""
    dbscore = ""
    ccfscore = ""
    ccfgrade = ""
    recs = {}
    def __init__(self):
        self.recs = {}

file = open("result.txt","r")
content = file.read()
file.close()
content = content.split('\n')

oiers = []

for oier in content:
    oier = oier.split(',')
    toier = Oier()
    toier.uid = oier[0]
    toier.enname = oier[1]
    toier.zhname = oier[2]
    toier.gender = oier[3]
    toier.year = oier[4]
    toier.dbscore = oier[5]
    toier.ccfscore = oier[6]
    toier.ccfgrade = oier[7]
    oier = oier[8].split('/')
    for tmp in oier:
        tmp = tmp.split(':')
        trec = Record()
        trec.contest = tmp[0]
        trec.school = tmp[1]
        trec.score = tmp[2]
        trec.rank = tmp[3]
        trec.province = tmp[4]
        trec.prize = tmp[5]
        toier.recs[trec.contest]=deepcopy(trec)
        
    oiers.append(deepcopy(toier))

for i in oiers:
    # 自行添加约束条件
    print("https://oier.baoshuo.dev/oier/"+i.uid)