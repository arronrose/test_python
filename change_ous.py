__author__ = 'ZXC'
# -*- coding: utf8 -*-

from pymongo import MongoClient
import re

def getMongoClient(host,port):
    replset=host.split("/")
    reptype=replset[0]
    master=replset[1]
    slave=replset[2]
    mport=str(port)
    mongoUrl="mongodb://"+master+":"+mport+","+slave+":"+mport+"/?replicaSet="+reptype
    client = MongoClient(mongoUrl,w=0)
    # client = MongoClient(host, port,w=0)
    return client

def get_user_list(users):
    users.find( {}, {'_id':0,'uid':1,'devs':1})



if __name__=="__main__":
    # mongo_host = "repset/192.168.1.15/192.168.1.16"
    mongo_host = "192.168.1.15"
    mongo_port = 27017
    client = MongoClient(mongo_host,mongo_port)
    db = client["wcloud_o"]
    users = db["user"]

    result = users.find({"oudn":{"$in":[re.compile(u'/*ou=肇庆市委办,ou=肇庆市,dc=test,dc=com')]}})
    count = 0
    for item in result:
        count+=1
        print str(count)+":"+item['username']
        db.user.update({"uid":item['uid']},{"$set":{"oudn":"ou=肇庆市委办,ou=肇庆市委,ou=肇庆市,dc=test,dc=com"}})



