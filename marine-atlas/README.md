
Interesting website showing area's where you are not allowed to fish
etc.

Example URL.

	http://ec.europa.eu/maritimeaffairs/atlas/maritime_atlas/#lang=EN;p=w;pos=14.589:56.113:6;bkgd=6:0.45;gra=0;mode=1;theme=14:0.7:1:0,120:1:1:0,73:1:1:0;

Digging in you can get some data out of here

	{
		"results": [
			{
				"attributes": {
					"Area_km2": "1239.480525",
					"MS": "NL",
					"OBJECTID": "19673",
					"POINT_X": "343355.691",
					"POINT_Y": "7174558.8692",
					"RELEASE_DA": "01/10/2013",
					"SITECODE": "NL2008002",
					"SITENAME": "Klaverbank",
					"SITETYPE": "B",
					"Shape": "Polygon",
					"Shape_Area": "3564215311.46448",
					"Shape_Length": "242495.544638"
				},
				"displayFieldName": "SITECODE",
				"layerId": 2,
				"layerName": "Scale under 1:10,000,000",
				"value": "NL2008002"
			},
			{
				"attributes": {
					"Area_km2": "1239.480525",
					"MS": "NL",
					"OBJECTID": "19673",
					"POINT_X": "343355.691",
					"POINT_Y": "7174558.8692",
					"RELEASE_DA": "01/10/2013",
					"SITECODE": "NL2008002",
					"SITENAME": "Klaverbank",
					"SITETYPE": "B",
					"Shape": "Polygon",
					"Shape_Area": "3564215311.46448",
					"Shape_Length": "242495.544638"
				},
				"displayFieldName": "SITECODE",
				"layerId": 2,
				"layerName": "Scale under 1:10,000,000",
				"value": "NL2008002"
			}
		]
	}

From this URL

	curl
	'http://discomap.eea.europa.eu/ArcGIS/rest/services/Bio/Natura2000_Dyna_WM/MapServer/identify?returnGeometry=false&tolerance=6&layers=visible%3A1%2C2%2C3%2C4%2C5%2C6%2C7%2C8&sr=102100&f=json&geometryType=esriGeometryPoint&imageDisplay=1282%2C490%2C96&geometry=%7B%22x%22%3A347235%2E9307078235%2C%22y%22%3A7204182%2E945255516%7D&mapExtent=%2D1511712%2E597187169%2C6382332%2E017133519%2C4759792%2E699553305%2C8779397%2E224156009'
	-H 'Host: discomap.eea.europa.eu' -H 'User-Agent: Mozilla/5.0
	(Macintosh; Intel Mac OS X 10.9; rv:33.0) Gecko/20100101 Firefox/33.0'
	-H 'Accept:
	text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H
	'Accept-Language: nl,en-US;q=0.7,en;q=0.3' -H 'Accept-Encoding: gzip,
	deflate' -H 'Referer:
	http://ec.europa.eu/maritimeaffairs/atlas/maritime_atlas/index.swf' -H
	'Connection: keep-alive'

It's justs need to be gunzipped

