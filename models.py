from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY

db = SQLAlchemy()

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, nullable=False)
    member_ids = db.Column(ARRAY(db.Integer), nullable=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)
    stack = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('active', 'completed', 'pending', 'archived', name='status'), nullable=False)
    private = db.Column(db.Boolean, default=False)
    accepted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Project {self.name}>'
