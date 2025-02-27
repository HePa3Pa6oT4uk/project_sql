from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db import engine
Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('project_id', Integer, ForeignKey('projects.id')))

class User(Base):
    '''
    User
    '''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    projects = relationship('Project', 
    secondary=association_table, 
    back_populates='users')
    def __repr__(self):
        return str((self.id, self.username, self.email))
class Profile(Base):
    '''
    Profile
    '''
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    bio = Column(String)
    phone = Column(String)
    user_id = Column(Integer,
    ForeignKey('users.id'), unique=True)
    user = relationship('User', backref='profile',
    uselist=False)

class Project(Base):
    '''
    Project
    '''
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    users = relationship('User', 
    secondary=association_table, 
    back_populates='projects')

class Task(Base):
    '''
    or Tusk?...
    '''
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    status = Column(String)
    project_id = Column(Integer,
    ForeignKey('projects.id'), unique=True)

Base.metadata.create_all(engine)
