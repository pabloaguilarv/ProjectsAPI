from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    company = Column(String)

    members = relationship('TeamMember', back_populates='project')


class TeamMember(Base):
    __tablename__ = 'teammembers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))

    project = relationship('Project', back_populates='members')