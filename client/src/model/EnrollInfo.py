from datetime import datetime
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from src.model.firedb import firedb

class EnrollInfo():
    def __init__(self,dbRef):
        self._itemList={}
        self._idList=[]
        self.db=dbRef
        self._idList, self._itemList=self.db.downloadEnrollItem()

    def setStstus(self, docId, status):
        self._itemList[docId]['checked']=status
        self.db.updateEnrollChecked(docId, {'checked' : status})

    def getStstus(self, docId):
        return self._itemList[docId]['checked']

    def getName(self, docId):
        return self._itemList[docId]['id']

    def getSchool(self, docId):
        return self._itemList[docId]['school']

    def getCatogoryName(self, docId):
        catlist={'sracing':"個人競速",'sitem':"個人道具",'gracing':"團體競速"}
        return catlist[self._itemList[docId]['cat']]

    def getRound(self, docId):
        # return self._itemList[docId]['round']
        return "128強"

    def getTimeInterval(self, docId):
        time=self._itemList[docId]['time'].timestamp_pb()
        time=datetime.fromtimestamp(time.seconds)
        nowTime=datetime.now()
        interval=nowTime-time
        return "{}天{}時{}分前".format(interval.days,int(interval.seconds/3600),int((interval.seconds%3600)/60))

    def getIdList(self):
        return self._idList

    def getIdListByCatRound(self, cat, round):
        result=[]
        for id in self._idList:
            if self.getRound(id)==round and self.getCatogoryName(id)==cat:
                result.append(id)
        return result

    def refresh(self):
        self._idList, self._itemList=self.db.downloadEnrollItem()
