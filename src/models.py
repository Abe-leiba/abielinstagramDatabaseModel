from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    #relationship
    posts: Mapped[List["Post"]] = relationship(back_populates = "user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Post(db.Model):
     id: Mapped[int] = mapped_column(primary_key=True)

     #relationship
     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

     def serialize(self):
        return {
            "id": self.id,
        
            
        }



class Follower(db.Model):
     id:Mapped[int] = mapped_column(primary_key=True)
     
     #relationship
     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
     follower_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
     def serialize(self):
        return {
            "id": self.id,
        
            
        }
     
     
class Comment(db.Model):
     id: Mapped[int] = mapped_column(primary_key=True)
     comment_text: Mapped[str] = mapped_column(String(120))
     #relationship
     author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
     post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
     def serialize(self):
        return {
            "id": self.id,
        
            
        }
     
     
class Media(db.Model):
     id: Mapped[int] = mapped_column(primary_key=True)

     #relationship
     post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
     url: Mapped[str] = mapped_column(String(250))
     
     def serialize(self):
        return {
            "id": self.id,
        
            
        }
     