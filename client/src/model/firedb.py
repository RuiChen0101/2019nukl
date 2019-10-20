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

    def updateEnrollChecked(self, docId, status):
        doc_ref=self.enroll_ref.document(docId)
        doc_ref.update({'checked': status})

    def handelRefresh(self):
        self._downloadEnrollItem()
        self._downloadMatchItem()

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
