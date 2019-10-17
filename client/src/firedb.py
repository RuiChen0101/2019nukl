import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
from google.api_core.datetime_helpers import DatetimeWithNanoseconds

class firedb:
    def __init__(self):
        cred = credentials.Certificate("./ttes-2019nukl-firebase-adminsdk-0zybv-3f3b3d8158.json")
        firebase_admin.initialize_app(cred)
        self._db = firestore.client()
        self.info_ref = self._db.collection('enroll-Info')
        self._itemList={}
        self._idList=[]
        self.dowloadAllItem()

    def handelCheck(self,docid):
        self._itemList[docid]['checked']="true"
        doc_ref=self.info_ref.document(docid)
        doc_ref.update({'checked': 'true'})

    def handelCancel(self,docid):
        self._itemList[docid]['checked']="false"
        doc_ref=self.info_ref.document(docid)
        doc_ref.update({'checked': 'false'})

    def handelDelete(self,docid):
        self._itemList[docid]['checked']="delete"
        doc_ref=self.info_ref.document(docid)
        doc_ref.update({'checked': 'delete'})

    def handelRefresh(self):
        self.dowloadAllItem()

    def getIdList(self):
        return self._itemList

    def getStstus(self,docid):
        return self._itemList[docid]['checked']

    def getName(self,docid):
        return self._itemList[docid]['id']

    def getSchool(self,docid):
        return self._itemList[docid]['school']

    def getCatogory(self,docid):
        catlist={'sracing':"個人競速",'sitem':"個人道具",'gracing':"團體競速"}
        return catlist[self._itemList[docid]['cat']]

    def dowloadAllItem(self):
        docs = self.info_ref.stream()
        for doc in docs:
            self._idList.append(doc.id)
            self._itemList[doc.id]=doc.to_dict()

    def getTimeInterval(self,docid):
        time=self._itemList[docid]['time'].timestamp_pb()
        time=datetime.fromtimestamp(time.seconds)
        nowTime=datetime.now()
        interval=nowTime-time
        return "{}天{}時{}分前".format(interval.days,int(interval.seconds/3600),int((interval.seconds%3600)/60))
