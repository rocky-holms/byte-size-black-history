import arrow
<<<<<<< HEAD
from sqlalchemy import Boolean, Column, Integer, Text
=======
from sqlalchemy import Boolean, Column, Integer, DateTime, Text
>>>>>>> 00b1ae0155e4eb97f80fd787486c24f3a18fc6b6
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

    url = Column(URLType, nullable=False)
    title = Column(Text, nullable=False)
    date_used = Column(ArrowType, nullable=False)
