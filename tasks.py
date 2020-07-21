from db import db_session
from models import Subscriber

import logging


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
    """Cancel a subscription.

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


def send_email(title: str, wikipedia_url: str):
    """Send daily email with Wiki link to Afrian American activist.

    Args:
        title (str): Title of the email being sent.
        wikipedia_url (str): URL link to activist.
    """
    pass


def send_daily_email():
    pass

