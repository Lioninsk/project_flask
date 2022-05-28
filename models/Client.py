from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.sql import func

from config import db


class Client(db.Model):
    __tablename__ = 'clients'
    user_id = db.Column(INTEGER(unsigned=True),
                        db.ForeignKey('users.id',
                                      ondelete='CASCADE',
                                      onupdate='CASCADE'),
                        nullable=False,
                        index=True,
                        primary_key=True,
                        unique=True)

    name = db.Column(db.String(150), nullable=False)

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True),
                           server_default=db.func.now(),
                           onupdate=db.func.now())

    def __init__(self, data=None):
        if data:
            keys = list(data.keys())
            values = list(data.values())
            for i in range(0, len(keys)):
                setattr(self, keys[i], values[i])

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
