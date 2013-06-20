import urllib2
from bs4 import BeautifulSoup
from collections import defaultdict
import optparse, logging, sys, re
import json
import time

def parse_seasons (project_names):
	d  = defaultdict(lambda : defaultdict(list)) #list of produce keyed by month and state
	late_early_pattern = r"(.+)\s\((early|late)\)"
	state_pattern = r"Full Year:\s(.*)"
	base_url = "http://www.nrdc.org/health/foodmiles/fullyear.asp?state="
	# for i in range(1,53):
	for i in range(1,2):
		time.sleep(1)
		url = base_url+str(i)
		print url
		page = urllib2.urlopen(url).read()
		soup = BeautifulSoup(page)
		state = soup.findAll('caption')[0].contents[0].encode("ascii","ignore")
		state = re.match(state_pattern, state).group(1)
		rows = soup.body.findAll('tr')[1:-1] #remove header and footnote
		for row in rows[1:2]:
			month = row.find('th').contents[0]
			#reformat month
			print month
			matchObj = re.match(late_early_pattern, month)
			if matchObj:
				month = matchObj.group(1)
				timing = matchObj.group(2)
				if timing in ['early', 'late']:
					month = month+"-"+timing			
			foods = [f.encode("ascii","ignore").strip("*").strip() for f in row.find('td').contents[0].split(",")]
			print str(foods)
			d[month][state] = foods
	with open('seasons.json', 'w') as outfile:
  		json.dump(d, outfile)

def _main():
    
    usage = "usage: parse each state and month"
    parser = optparse.OptionParser(usage)
    
    options, args = parser.parse_args()
    
    parse_seasons(args)
        
if __name__ == "__main__":
    _main()    