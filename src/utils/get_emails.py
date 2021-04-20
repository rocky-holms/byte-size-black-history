import os

try:
    DOMAIN_NAME = os.environ["DOMAIN_NAME"]
except Exception:
    raise Exception('MUST SET "DOMAIN_NAME" ENVIRONMENT VARIABLE')


def link_email(title: str, wiki_link: str) -> str:
    """
    Create text being added to emails.

    Args:
        wiki_link (str): link to activist.

    Returns:
        str: Text being added to emails.
    """
    text: str = f"""
    <html>
    <h3>{title}</h3>
    <a href="{wiki_link}">read wiki page</a>

    <hr>

    <a href="http://{DOMAIN_NAME}/donate">donate to great organization fighting for equality for everyone.</a>
    <a href="http://{DOMAIN_NAME}/unsubscribe">unsubscribe</a>
    </html>
    """
    return text


def subscribed_email(email: str):
    """HTML for when emails initially sent to subscribers.

    Args:
        email (str): Email of subscriber.

    Returns:
        [type]: Returns the HTML for the email.
    """
    text: str = f"""
    <html>
    <h3>Thank you for joining the mailing list.</h3>

    <a href="http://{DOMAIN_NAME}/confirmation/confirm/{email}">Click this link to begin receiving Black History links a day.</a>

    <hr>

    <a href="http://{DOMAIN_NAME}/donate">donate to great organization fighting for equality for everyone.</a>
    </html>
    """
    return text
