from _init_ import CONN,CURSOR

class Band:
    def __init__(self,name,hometown, id=None):
        self.id = id
        self.name = name
        self.hometown =hometown 
        
    def __repr__(self):
        return f"<The Band {self.id}: {self.name}, {self.hometown}>"    
        
    @classmethod
    def create_table(cls):
        
        sql = """
            CREATE TABLE IF NOT EXISTS bands (
            id INTEGER PRIMARY KEY,
            name TEXT,
            hometown TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):
        
        sql = """
            DROP TABLE IF EXISTS bands;
        """
        CURSOR.execute(sql)
        CONN.commit()   
        
    def save(self):
        
        sql = """
            INSERT INTO bands (name, hometown)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.hometown))
        self.id = CURSOR.lastrowid
        CONN.commit() 
    @classmethod
    def create(cls,name,hometown):
        band = cls(name, hometown)
        band.save()
        return band       

class Venue:
    def __init__(self, title, city, id=None):
        self.id = id
        self.title = title
        self.city = city

    def __repr__(self):
        return f"<The Venue {self.id}: {self.title}, {self.city}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS venues (
            id INTEGER PRIMARY KEY,
            title TEXT,
            city TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS venues;
        """
        CURSOR.execute(sql)
        CONN.commit()        
        
    def save(self):
        sql = """
            INSERT INTO venues (title, city)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.title, self.city))
        self.id = CURSOR.lastrowid
        CONN.commit()    
    
    @classmethod
    def create(cls, title, city):
        venue = cls(title, city)
        venue.save()
        return venue
    
        
class Consert:
    
    def __init__(self,band_id,venue_id,date,id=None):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date=date
    
    def __repr__(self):
        return f"<The Consert {self.id}: {self.band_id}, {self.venue_id}, {self.date}>"
    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS concerts (
            id INTEGER PRIMARY KEY,
            band_id INTEGER,
            venue_id INTEGER,
            date DATE,
            FOREIGN KEY (band_id) REFERENCES bands(id),
            FOREIGN KEY (venue_id) REFERENCES venues(id))
        """
        CURSOR.execute(sql)
        CONN.commit()    
        
    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS concerts;
        """
        CURSOR.execute(sql)
        CONN.commit()    
        
    def save(self):
        sql = """
            INSERT INTO concerts (band_id, venue_id, date)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.band_id, self.venue_id, self.date))
        CONN.commit()    
    
    @classmethod
    def create(cls, band_id, venue_id, date):
        concert = cls(band_id, venue_id, date)
        concert.save()
        return concert    