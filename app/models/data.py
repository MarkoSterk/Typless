from app import db
from datetime import datetime
import json


class Data(db.Model):
    
    __tablename__ = 'data'

    id=db.Column(db.Integer, primary_key=True)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    email=db.Column(db.String(200), nullable=False)
    data=db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Data(id: {self.id}, created_at: {self.created_at}, email: {self.email})'    

    def to_json(self):
        data = {
            'id': self.id,
            'created_at': self.created_at,
            'email': self.email,
            'data': json.loads(self.data)
        }
        return data


        
