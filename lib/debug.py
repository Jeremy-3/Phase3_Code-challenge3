from _init_ import CONN ,CURSOR
from music import Band,Venue,Consert



import ipdb
Band.drop_table()
Band.create_table()
Venue.drop_table()
Venue.create_table()
Consert.drop_table()
Consert.create_table()

band1 = Band.create("The Beatles", "Liverpool")
print(band1)
band2 = Band.create("The Rolling Stones", "London")
print(band2)


venue1 = Venue.create("The O2", "London")
print(venue1)
venue2 = Venue.create("Wembley Stadium", "London")
print(venue2)


consert1 = Consert.create(band1.id, venue1.id, "2023-06-01")
consert2 = Consert.create(band2.id, venue2.id, "2023-07-04")
print(consert1)
print(consert2)




ipdb.set_trace()    
