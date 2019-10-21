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
            if self.getRound(id)==round and self.getCatogoryName(id)==cat:
                result.append(id)
        return result

    def createNewMatch(self,cat,round,group,playerList):
        rcatList={"個人競速":'sracing',"個人道具":'sitem',"團體競速":'gracing'}
        data={
            'cat':rcatList[cat],
            'group':group,
            'player':playerList,
            'round':round,
            'status':'created'
        }
        self.db.newMatch(data)
        self._idList, self._itemList=self.db.downloadMatchItem()

    def deleteMatch(self, docId):
        self.db.deleteMatch(docId)
        self._idList, self._itemList=self.db.downloadMatchItem()

    def setArrangement(self, docId, dateTime):
        data={
            'matchTime':dateTime,
            'status':'arranged'
        }
        self.db.updateMatchDb(docId,data)
        self._idList, self._itemList=self.db.downloadMatchItem()

    def getRound(self, docId):
        return self._itemList[docId]['round']

    def getCatogoryName(self, docId):
        catList={'sracing':"個人競速",'sitem':"個人道具",'gracing':"團體競速"}
        return catList[self._itemList[docId]['cat']]

    def getCatogory(self, docId):
        return self._itemList[docId]['cat']

    def getGroup(self, docId):
        return self._itemList[docId]['group']

    def getStatusName(self, docId):
        statusList={'created':"已建立",'arranged':"已約戰",'finished':"已完成"}
        return statusList[self._itemList[docId]['status']]

    def getStatus(self, docId):
        return self._itemList[docId]['status']

    def getPlayerScore(self, docId, playerId):
        if(self.getStatus(docId)!="finished"):
            return "-"
        return str(self._itemList[docId]['player'][playerId])

    def getPlayerList(self, docId):
        if(self.getStatus(docId)=="finished"):
            return list(self._itemList[docId]['player'].keys())
        return self._itemList[docId]['player']

    def getAdvanceList(self, docId):
        if(self.getStatus(docId)!="finished"):
            return []
        return self._itemList[docId]['advanced']

    def getTime(self, docId):
        if(self.getStatus(docId)=="created"):
            return "--"
        time=self._itemList[docId]['matchTime'].timestamp_pb()
        time=datetime.fromtimestamp(time.seconds)
        return time.strftime("%m/%d, %H:%M")

    def isArrangable(self, docId):
        if(self.getStatus(docId)=="created"):
            return True
        return False

    def isFinishable(self, docId):
        if(self.getStatus(docId)=="arranged"):
            return True
        return False

    def isReplaySetable(self, docId):
        if(self.getStatus(docId)=="finished"):
            return True
        return False
