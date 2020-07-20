from sqlalchemy import Column, Integer, String

from db import Base
from sqlalchemy_utils import EmailType, URLType, UUIDType


class Subscriber(Base):
    """Subscriber information DB Model"""

    __tablename__ = "subscriber"

    id = Column(Integer, primary_key=True)
    email = Column(EmailType, unique=True, nullable=False)

    def __repr__(self):
        return f"Subscriber {self.name}"


class ChangeEmail(Base):
    """Email validation Model for subscriber email change"""

    __tablename__ = "change_email"

    email = Column(EmailType, nullable=False)
    uid = Column(UUIDType, nullable=False)


class WikiLinks(Base):
    """Wiki links Model"""

    __tablename__ = "wiki_links"

    url = Column(URLType, nullable=False)
