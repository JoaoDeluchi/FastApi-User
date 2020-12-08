from sqlalchemy import Column, String, Boolean
from uuid import uuid4
from config.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    first_name = Column(String(20))
    last_name = Column(String(20))
    is_active= Column(Boolean, default=True)
    is_admin= Column(Boolean, default=False)
    password = Column(String(16))

    def serializer(self):
        return {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "is_active": self.is_active,
                "is_admin": self.is_admin,
                "password": self.password
            }
