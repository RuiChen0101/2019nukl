from datetime import datetime
from google.api_core.datetime_helpers import DatetimeWithNanoseconds
from src.model.firedb import firedb

class MatchInfo():
    def __init__(self,dbRef):
        self._itemList={}
        self._idList=[]
        self.db=dbRef
        self._idList, self._itemList=self.db.downloadMatchItem()

    def getMatchList(self, cat, round):
        result=[]
        for id in self._idList:
            if self.getRound(id)==round and self.getCatogory(id)==cat:
                result.append(id)
        return result

    def createNewMatch(self,playerList):
        self._idList, self._itemList=self.db.downloadMatchItem()

    def getRound(self, docId):
        return self._itemList[docId]['round']

    def getCatogory(self, docId):
        catList={'sracing':"個人競速",'sitem':"個人道具",'gracing':"團體競速"}
        return catList[self._itemList[docId]['cat']]

    def getGroup(self, docId):
        return self._itemList[docId]['group']

    def getStatus(self, docId):
        statusList={'created':"已建立",'arranged':"已約戰",'finished':"已完成"}
        return statusList[self._itemList[docId]['status']]
