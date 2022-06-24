import json
from sqlalchemy import Column, Integer, String, create_engine, update
import sqlalchemy
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///firstdb.db" , echo=True)

Session = sessionmaker(bind=engine)
Base = sqlalchemy.orm.declarative_base()


class Database(Base):
    __tablename__ = "first_db"

    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    typeOf =Column(String(256))

    def __repr__(self):
        return f"Database(id={self.id!r}, name={self.name!r}, typeOf={self.typeOf!r})" 
        
def main():
    session = Session()


    Base.metadata.create_all(engine) #This creates the tables.

    #testing just adding to the DB:

    session.add(
        Database(
            id=1,
            name="jinx",
            typeOf="cat"
        )
    )
    session.commit()
    print("just added a row to the DB")
    print("You can view the DB by installing SQLITE Explorer in VSCODE and opening the db w that.")



if __name__ == "__main__":
    main()