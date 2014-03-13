import numpy as np
#====================

"""filename		= '/home/kasey/Desktop/USGS_Deadly_Quakes.txt'
f 					= open(filename,'r')
lines			= f.readlines()
year				= []
loc				= []
deaths    		= []
"""

EQ_info      = {"2012":768, "2011":21953,"2010":320120,"2009":1790,
							"2008":88011,"2007":712,"2006":6605,"2005":88003,
							"2004":228802,"2003":33819,"2002":1685,"2001":21357,
							"2000":231,"1999":22662,"1998":9430,"1990":52056,
							"1991":3210,"1992":3920,"1993":10096,"1994":1634,
							"1995":7980,"1996":589,"1997":3069,	"1980":8620,
							"1981":5223,"1982":3328,"1983":2372,"1984":174,
							"1985":9846,"1986":1068,"1987":1080,"1988":26552,
							"1989":617,"1978":15000,"1977":1500,"1976":279769,
							"1975":4300,"1974":25300}

# Count fatalities
this_dec 					= 0
last_dec  				= 0
last_last_dec		 	= 0
last_last_last_dec 	= 0
total							= 0

YEARS 				= np.sort(EQ_info.keys())

for year in YEARS:
	dead = EQ_info[year]
	year  = int(year)

	total += dead

	if year>2002 and year<2013:
		this_dec 					+= dead
	elif year>1992 and year<2003:
		last_dec 					+= dead
	elif year>1982 and year<1993:
		last_last_dec 			+= dead
	elif year>1972 and year<1983:
		last_last_last_dec 	+= dead


