from sqlalchemy import Column, Integer, Text, BOOLEAN,ForeignKey,TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref

Base = declarative_base()


class users(Base):
    __tablename__ = "users"

    p_id = Column(Integer,primary_key=True)
    full_name = Column(Text)
    pass_num = Column(Integer)

    def __str__(self):
        return "({},{}, {})\n".format(self.p_id, self.full_name, self.pass_num)

    def __repr__(self):
        return str(self)


class trains(Base):
    __tablename__ = "trains"

    tr_id = Column(Integer,primary_key=True)
    departure_t = Column(TIMESTAMP)
    arrival_t = Column(TIMESTAMP)


    def __str__(self):
        return "({},{},{})\n".format(self.tr_id,self.departure_t,self.arrival_t)

    def __repr__(self):
        return str(self)



class tickets(Base):
    __tablename__ = "tickets"

    t_id = Column(Integer, primary_key=True)
    num = Column(Integer)
    seat = Column(Integer)
    type = Column(Text)
    p_id = Column(Integer,ForeignKey('users.p_id'))
    tr_id = Column(Integer,ForeignKey('trains.tr_id'))

    def __str__(self):
        return "({},{},{},{},{},{})\n".format(self.t_id,self.num,self.seat,self.type,self.p_id,self.tr_id)

    def __repr__(self):
        return str(self)

