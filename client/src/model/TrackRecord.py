from src.model.firedb import firedb

class TrackRecord():
    def __init__(self, dbRef):
        self._categoryList={"團體競速":"groupRacing","個人道具":"signalItem","個人競速":"signalRacing"}
        self.db=dbRef

    def getAllTrackRecord(self, cat):
        return self.db.downloadRecordItem(self._categoryList[cat])

    def updateTrackRecord(self, cat, data):
        data={'record':data}
        self.db.updateRecordDb(self._categoryList[cat],data)
