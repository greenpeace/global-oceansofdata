# AIShub

This is the data coming from AIS hub, single call.

	curl -Lo /tmp/data.json.gzip "http://data.aishub.net/ws.php?username=USERNAME&format=1&output=json&compress=2"

Here is some details on the API http://www.aishub.net/xml-description-20.html

I have a password, just ask me.

	{
	"A": 5,
	"B": 51,
	"C": 8,
	"CALLSIGN": "PD2541",
	"COG": 79.1,
	"D": 2,
	"DEST": "GRAVENDEEL",
	"DRAUGHT": 0,
	"ETA": "05-02 15:12",
	"HEADING": 511,
	"IMO": 0,
	"LATITUDE": 51.97957,
	"LONGITUDE": 5.89863,
	"MMSI": 244670840,
	"NAME": "EUREKA V",
	"NAVSTAT": 0,
	"SOG": 0,
	"TIME": "2014-11-28 22:23:55 GMT",
	"TYPE": 0
	},

