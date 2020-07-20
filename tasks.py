import logging

import stripe

from db import db_session
from models import Company


def company_information_to_db(information: dict) -> bool:
    try:
        company = Company(**information)
        db_session.add(company)
        db_session.commit()
        return True
    except Exception:
        logging.error(f"Unable to save company information to db: {information}")
        return False


def email_signup(email: str, subscription_id: str = None):
    pass


def cancel_service(email: str):
    pass


def send_email(title: str, wikipedia_url: str):
    pass


def change_email(current_email: str, new_email: str):
    pass


def update_credit_card(new_subscription_id: str):
    pass


def send_daily_email():
    pass


def finalize_email_change(email_change_code: str):
    pass
