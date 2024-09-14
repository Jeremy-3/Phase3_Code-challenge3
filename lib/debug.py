from _init_ import CONN ,CURSOR
from music import Band
from music import Venue


import ipdb
Band.drop_table()
Band.create_table()
Venue.drop_table()
Venue.create_table()

ipdb.set_trace()