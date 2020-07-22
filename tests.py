import unittest.mock as mock

import tasks


def test_scription_confirmation():
    check = tasks.subscription_confirmation(None)

    assert check is False


def test_stop_subscription():
    check = tasks.stop_subscription(None)

    assert check is False


@mock.patch("tasks.send_confirmation_email", return_value=200)
def test_send_confirmation_email(response):
    code = tasks.send_confirmation_email("me@example.com")

    assert code == 200


@mock.patch("tasks.send_link_email", return_value=200)
def test_send_link_email(response):
    code = tasks.send_link_email("me@example.com")

    assert code == 200


@mock.patch("tasks.send_email_to_subscribers", return_value=None)
def test_send_email_to_subscribers(response):
    value = tasks.send_email_to_subscribers()

    assert value is None

