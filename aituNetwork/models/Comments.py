from aituNetwork.models import db
from datetime import datetime


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False, index=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DATETIME, nullable=False, default=datetime.now)

    @staticmethod
    def get(comment_id: int):
        return Comments.query.get(comment_id)

    @staticmethod
    def create_comment(user_id: int, text: str):
        comment = Comments(user_id=user_id, text=text)
        db.session.add(comment)
        db.session.commit()

        return comment
