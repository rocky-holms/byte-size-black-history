from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import ArrowType, EmailType, URLType

from db import Base


class Subscriber(Base):
    """Subscriber information DB Model"""

    __tablename__ = "subscriber"

    id = Column(Integer, primary_key=True)
    email = Column(EmailType, unique=True, nullable=False)
    subscription_id = Column(String, unique=True, nullable=True)

    def __repr__(self):
        return f"Subscriber {self.name}"


class WikiLink(Base):
    """Wiki links Model"""

    __tablename__ = "wiki_links"

    url = Column(URLType, nullable=False)
    date_used = Column(ArrowType, nullable=False)
