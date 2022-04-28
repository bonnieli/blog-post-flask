from sqlalchemy.orm import validates
from ..shared import db


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, default=0, nullable=False)
    reads = db.Column(db.Integer, default=0, nullable=False)
    popularity = db.Column(db.Float, default=0.0, nullable=False)
    users = db.relationship("User", secondary="user_posts", viewonly=True)

    # note: comma separated string since sqlite does not support arrays
    _tags = db.Column("tags", db.String, nullable=False)

    createdAt = db.Column(db.DateTime, server_default=db.func.now())
    updatedAt = db.Column(
        db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now()
    )

    # getter and setter for tags column.
    # converts list to string when value is set and string to list when value is retrieved.
    @property
    def tags(self):
        return self._tags.split(",")

    @tags.setter
    def tags(self, tags):
        self._tags = ",".join(tags)

    @validates("popularity")
    def validate_popularity(self, key, popularity) -> str:
        if popularity > 1.0 or popularity < 0.0:
            raise ValueError("Popularity should be between 0 and 1")
        return popularity
