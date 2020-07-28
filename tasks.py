import logging
import os

import arrow
import requests

from db import db_session
from models import Subscriber, WikiLink
from get_emails import link_email, subscribed_email


try:
    MAILGUN_API_KEY = os.environ["MAILGUN_API_KEY"]
except Exception:
    raise Exception('MUST SET "MAILGUN_API_KEY" ENVIRONMENT VARIABLE')

try:
    DOMAIN_NAME = os.environ["DOMAIN_NAME"]
except Exception:
    raise Exception('MUST SET "DOMAIN_NAME" ENVIRONMENT VARIABLE')


def start_subscription(email: str) -> bool:
    """Signup a subscriber.

    Args:
        email (str): email of subscriber signing up.

    Returns:
        bool: Indicates if signup was successful
    """
    try:
        subscriber = Subscriber(email=email)
        db_session.add(subscriber)

        send_confirmation_email(email)
        return True
    except Exception as e:
        logging.error(f"Unable to create subscription for: {email} | Error {e}")
        return False


def subscription_confirmation(email: str) -> bool:
    """Allow subscriber to confirm subscription

    Args:
        email (str): email of subscriber

    Returns:
        bool: if the subscription was created successfully
    """
    try:
        db_session.query(Subscriber).filter(Subscriber.email == email).update(
            Subscriber.is_subscribed is True
        )
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
        db_session.query(Subscriber).filter(Subscriber.email == email).update(
            Subscriber.is_subscribed is False
        )
        db_session.commit()
        return True
    except Exception as e:
        logging.error(f"Unable to cancel subscription for: {email} | Error {e}")
        return False


def send_confirmation_email(email: str) -> int:
    """Send confirmation email.

    Args:
        title (str): Title of the email being sent.
        wikipedia_url (str): URL link to activist.
    """

    response = requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": "Knowledgeable Donations <email.knowledgeabledonations.xyz>",
            "to": email,
            "subject": "Thank you for subscribing!",
            "html": subscribed_email(email),
        },
    )
    return response.status_code


def send_link_email(title: str, html: str, subscribers: list) -> int:
    """Send daily email with Wiki link to Afrian American activist.

    Args:
        title (str): Title of the email being sent.
        wikipedia_url (str): URL link to activist.
    """

    response = requests.post(
        f"https://api.mailgun.net/v3/{DOMAIN_NAME}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": "Byte Size Black History <mailgun@bytesizeblackhistory.online>",
            "to": subscribers,
            "subject": title,
            "html": html,
        },
    )
    return response.status_code


def send_email_to_subscribers() -> None:
    """
    Compile email to send to subscribers.
    """
    subscribers: list = db_session.query(Subscriber).filter_by(is_subscribed=True)
    wiki_link = WikiLink.where(WikiLink.date_used is None).limit(1)

    email_html = link_email("Today's Wikipedia Link", wiki_link.url)

    for subscriber in subscribers:
        send_link_email(wiki_link.title, email_html, subscriber)

    wiki_link.date_used = arrow.utcnow()
    db_session.commit()
