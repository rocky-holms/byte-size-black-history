import unittest

from models import Subscriber, WikiLink
from utils import create_email_text

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base

from sqlalchemy.orm import Query


def test_email_text():
    wiki_link: str = "wikilink.com"
    email_text: str = create_email_text(wiki_link)

    expected_text: str = """
    Today we are presenting another activist\n\n
    You can find them here at this link: wikilink.com\n\n
    We appreciate your subscription as always, and below we have some donation links.\n\n
    NAACP Donation Page: https://www.naacp.org/Donate/\n
    ACLU Donation Page: https://action.aclu.org/give/now\n
    Know your rights Camp Donation: https://www.knowyourrightscamp.com\n
    """

    assert email_text == expected_text


class TestDb(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        self.base = Base
        self.base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.db_session = self.Session()
        self.db_session.add(Subscriber(email="michael@example.com"))
        self.db_session.commit()

    def tearDown(self):
        self.base.metadata.drop_all(self.engine)

    def test_subscriber(self):
        subscriber_one = Query(Subscriber).filter(Subscriber.email == "michael@example.com")

        assert subscriber_one is not None

        subscriber_one = Query(Subscriber).filter(Subscriber.email == "none@example.com")

        assert subscriber_one is None
