import arrow
from sqlalchemy import Boolean, Column, Integer, Text
from sqlalchemy_utils import ArrowType, EmailType, URLType

from db import Base


class Subscriber(Base):
    """Subscriber information DB Model"""

    __tablename__ = "subscriber"

    id = Column(Integer, primary_key=True)
    created_ts = Column(ArrowType, default=arrow.utcnow())
    updated_ts = Column(ArrowType)

    email = Column(EmailType, unique=True, nullable=False)
    is_subscribed = Column(Boolean, default=False)

    def __repr__(self):
        return f"Subscriber {self.email}"


class WikiLink(Base):
    """Wiki links Model"""

    __tablename__ = "wiki_links"

    id = Column(Integer, primary_key=True)
    created_ts = Column(ArrowType, default=arrow.utcnow())
    updated_ts = Column(ArrowType)

    url = Column(URLType, nullable=False, unique=True)
    title = Column(Text, nullable=False)
    date_used = Column(ArrowType, nullable=True)
