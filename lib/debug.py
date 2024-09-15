from _init_ import CONN ,CURSOR
from music import Band,Venue,Consert



import ipdb
Band.drop_table()
Band.create_table()
Venue.drop_table()
Venue.create_table()
Consert.drop_table()
Consert.create_table()
ipdb.set_trace()    