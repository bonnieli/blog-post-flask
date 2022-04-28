from ..shared import db


class UserPost(db.Model):
    __tablename__ = "user_posts"
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    postId = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
