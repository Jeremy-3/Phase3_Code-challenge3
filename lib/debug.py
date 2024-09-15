from _init_ import CONN ,CURSOR
from music import Band,Venue,Concert



import ipdb
Band.drop_table()
Band.create_table()
Venue.drop_table()
Venue.create_table()
Concert.drop_table()
Concert.create_table()

band1 = Band.create("The Beatles", "Liverpool")
print(band1)
band2 = Band.create("The Rolling Stones", "London")
print(band2)


venue1 = Venue.create("The O2", "London")
print(venue1)
venue2 = Venue.create("Wembley Stadium", "London")
print(venue2)


concert1 = Concert.create(band1.id, venue1.id, "2023-06-01")
concert2 = Concert.create(band2.id, venue2.id, "2023-07-04")
print(concert1)
print(concert2)




ipdb.set_trace()    
