import logging
import os

import arrow
import requests

from db import db_session
from models import Subscriber, WikiLink
from utils import create_email_text

try:
    MAILGUN_API_KEY = os.environ["MAILGUN_API_KEY"]
except Exception:
    raise Exception('MUST SET "MAILGUN_API_KEY" ENVIRONMENT VARIABLE')

try:
    DOMAIN_NAME = os.environ["DOMAIN_NAME"]
except Exception:
    raise Exception('MUST SET "DOMAIN_NAME" ENVIRONMENT VARIABLE')


def start_subscription(email: str) -> bool:
    """
    Signup a subscriber.

    Args:
        email (str): email of subscriber signing up.

    Returns:
        bool: Indicates if signup was successful
    """
    try:
        subscriber = Subscriber(email=email)
        db_session.add(subscriber)
        db_session.commit()
        return True
    except Exception as e:
        logging.error(f"Unable to create subscription for: {email} | Error {e}")
        return False


def stop_subscription(email: str) -> bool:
    """
    Cancel a subscription.

    Args:
        email (str): [email associated with subscriber]
    """
    try:
        subscriber = Subscriber.query.filter_by(email=email).one()
        db_session.delete(subscriber)
        db_session.commit()
        return True
    except Exception as e:
        logging.error(f"Unable to cancel subscription for: {email} | Error {e}")
        return False


def send_email_to_subscribers(title: str, text: str, subscribers: list) -> int:
    """
    Send daily email with Wiki link to Afrian American activist.

    Args:
        title (str): Title of the email being sent.
        wikipedia_url (str): URL link to activist.
    """

    response = requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": "Knowledgeable Donations <email.knowledgeabledonations.xyz>",
            "to": subscribers,
            "subject": title,
            "text": text,
        },
    )
    return response.status_code


def send_email_main() -> None:
    """
    Compile email to send to subscribers.
    """
    subscribers: list = db_session.query(Subscriber).all()
    wiki_link = db_session.select(WikiLink).where(WikiLink.date_used is None).one()

    send_email_to_subscribers("Knowledgeable Donations", create_email_text(wiki_link.url), subscribers)

    wiki_link.date_used = arrow.utcnow()
    db_session.commit()
