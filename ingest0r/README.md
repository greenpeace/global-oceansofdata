Reads weather data from Buoys

	# remove .fish for Bash
	source venv/bin/activate.fish

Then you can crawl into a datafile using

	scrapy runspider ndbc.py

The results are written to `data.jsonlines`

	{"lat": "27.401N",
	 "source": "http://www.ndbc.noaa.gov/station_page.php?station=42429",
	 "lon": "85.671W",
	 "rss": "/rss/ndbc_obs_search.php?lat=27.401N&lon=85.671W"}


