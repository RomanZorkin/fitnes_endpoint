from sqlalchemy import Column, Integer, String

from service.db import Base, engine


class Endpoint(Base):
    __tablename__ = 'endpoint'
    id = Column(Integer, primary_key=True, autoincrement=True)
    clubid = Column(String)
    login = Column(String)
    password = Column(String)
    url = Column(String)    

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

    def __repr__(self):
        return f'<Endpoint url="{self.url}" clubid="{self.clubid}">'


def create_schema():
    Base.metadata.create_all(bind=engine)