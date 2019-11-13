import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class firedb:
    def __init__(self):
        cred = credentials.Certificate("./ttes-2019nukl-firebase-adminsdk-0zybv-3f3b3d8158.json")
        firebase_admin.initialize_app(cred)
        self._db = firestore.client()
        self.enroll_ref = self._db.collection('enroll-Info')
        self.match_ref = self._db.collection('match-Info')
        self.record_ref = self._db.collection('track-record')

    def updateEnrollDb(self, docId, data):
        doc_ref=self.enroll_ref.document(docId)
        doc_ref.update(data)

    def updateMatchDb(self, docId, data):
        doc_ref=self.match_ref.document(docId)
        doc_ref.update(data)

    def updateRecordDb(self, docId, data):
        doc_ref=self.record_ref.document(docId)
        doc_ref.update(data)

    def newMatch(self, data):
        self.match_ref.add(data)

    def deleteMatch(self, docId):
        doc_ref=self.match_ref.document(docId)
        doc_ref.delete()

    def downloadMatchItem(self):
        _matchIdList=[]
        _matchItemList={}
        docs = self.match_ref.stream()
        for doc in docs:
            _matchIdList.append(doc.id)
            _matchItemList[doc.id]=doc.to_dict()
        return _matchIdList, _matchItemList

    def downloadEnrollItem(self):
        _enrollIdList=[]
        _enrollItemList={}
        docs = self.enroll_ref.stream()
        for doc in docs:
            _enrollIdList.append(doc.id)
            _enrollItemList[doc.id]=doc.to_dict()
        return _enrollIdList, _enrollItemList

    def downloadRecordItem(self,docId):
        doc = self.record_ref.document(docId).get().to_dict()
        _trackList=doc['track-list']
        _recordItemList=doc['record']
        return _trackList, _recordItemList

# if __name__=="__main__":
#     db=firedb()
#     trackList, recordItemList=db.downloadRecordItem("signalRacing")
#     initRecord={}
#     for track in trackList:
#         template={"holder":"N/A","record":"N/A"}
#         initRecord[track]=template
#     data={"record":initRecord}
#     db.updateRecordDb("signalRacing",data)
#     print(initRecord)
