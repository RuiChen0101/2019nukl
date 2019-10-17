const functions = require('firebase-functions');
const admin = require('firebase-admin');
const cors = require('cors')({origin: true});
admin.initializeApp();
const db = admin.firestore();

exports.hitCounter = functions.https.onRequest((req, res) => {
    const counterRef = db.doc('web-data/main');
    res.set('Access-Control-Allow-Origin', 'https://ttes-2019nukl.web.app/');
    if (req.method === 'PUT') {
    	return res.status(403).send('Forbidden!');
  	}
  	cors(req, res, () => {
   		counterRef.update({
      		counter: admin.firestore.FieldValue.increment(1)
  		})
  		.then(function() {
  		    res.status(200).send('success');
  		});
   	})
});

exports.updateVacancy = functions.https.onRequest((req, res) => {
    const enrollRef = db.collection("enroll-Info");
    const counterRef = db.doc('web-data/main');
    if (req.method === 'PUT') {
    	return res.status(403).send('Forbidden!');
  	}
    var category=[0,0,0];
    switch(req.body.category){
      case "sitem":
        category[0]=-1;
        break;
      case "sracing":
        category[1]=-1;
        break;
      case "gracing":
        category[2]=-1;
        break;
    }
    enrollRef.add({
        time: admin.firestore.FieldValue.serverTimestamp(),
        cat: req.body.category,
        id: req.body.id,
        school: req.body.school,
        checked: "false"
    })
 		counterRef.update({
    		groupRacingLeft: admin.firestore.FieldValue.increment(category[2]),
        signalRacingLeft: admin.firestore.FieldValue.increment(category[1]),
        signalItemLeft: admin.firestore.FieldValue.increment(category[0])
		})
    .then(function() {
      res.status(200).send('success');
    });
});
