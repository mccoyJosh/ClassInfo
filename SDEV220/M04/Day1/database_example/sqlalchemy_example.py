import sqlalchemy as sq
from sqlalchemy.orm import declarative_base # THE BOOK USES A DEPRECIATED VERSION OF THIS


conn = sq.create_engine('sqlite:///company.db')  # since sqlalchemy can use other databases, we must let it know we want to use sqlite


Base = declarative_base()
class Company(Base):
    __tablename__ = 'company'
    id = sq.Column('id', sq.Integer, primary_key=True)
    name = sq.Column('name', sq.String)
    address = sq.Column('address', sq.String)
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def __repr__(self):
        return "<Company({}, {}, {})>".format(self.id, self.name, self.address)


Base.metadata.create_all(conn)


# Now you can just make objects like normal in python to insert
cmp_1 = Company(1, 'Big Ads Company', '123 Advertisement Way, LA, CA')
cmp_2 = Company(2, 'Big Products LLC', '096 Make Money Avenue, LA, CA')


# TO INSERT, do these
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

#session.add(cmp_1)   # This works, or you can just add all
session.add_all([cmp_1, cmp_2])
session.commit()


# Gets results from querying database
q = session.query(Company)
result = q.all()
print(result)
