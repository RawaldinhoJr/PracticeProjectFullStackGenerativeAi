from sqlalchemy import Column, Integer, String, DateTime,Boolean,ForeignKey,JSON
from sqlalchemy.sql import func 
from sqlalchemy.orm import relationship
from db.database import Base

#SQL Alchemy creates a link between python and SQL, Using this we can make a SQL database in python using python classes

class Story(Base): #Story Table for the main story (The story from the initial prompt )  
    __tablename__ = "stories" 
    id = Column(Integer, index=True, primary_key=True)   
    title=Column(String, index=True)
    session_id=Column (String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    nodes=relationship("StoryNodes", back_populates="story")

    class StoryNode(Base): #Story Nodes are 
        __tablename__ = "story_nodes"

        id = Column(Integer, primary_key=True, index=True)
        story_id= Column(Integer, ForeignKey("stories.id"))
        content= Column(String)
        is_root= Column(Boolean, default=False)
        is_root= Column(Boolean, default=False)
        is_winning_ending= Column(Boolean, default=False)
