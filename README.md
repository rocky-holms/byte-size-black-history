# Byte Size Black History

## Purpose

1. This is a website to subscribe to daily emails with a link to different African American History
   1. Will receive an email daily.
   2. Email will contain a link to donations page to different African American organizations.
   3. Email will contain a different wiki link sent daily.
   
## Current Site

1. This is the current URL to the site: https://bytesizeblackhistory.online
   1. Works with current implemenation

## Setup

## Python Version

1. Requires Python 3.7.5 or greater

### Environment Variables

These are the list of envvironement variables that need to be set in the postactivate file of your virtualenv

1. `DB_URL` ->  URL associated with Postgres
   1. Format as: `postgres://username:password@localhost/db_name`
2. `MAILGUN_API_KEY` -> Mailgun API key
3. `DOMAIN_NAME` -> Full URL associate with Mailgun
   1. Example: `https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages`

## Additional Settings

1. run `pip install -r requirements.txt` after virtualenv is activated
2. you can optionally install dev requirements with `pip install -r dev-requirements.txt`

### DB

1. The following with need to be run to sync the db
   1. `python models.py`
   2. only needs to be run one time

### Crontab

1. Will need to be set with the following
   1. `0 0 * * * /usr/bin/python send_daily_email.py`
   2. This may differ based off your environment
   3. I recommend `crontab -e`

### Import Links

1. You can create a txt with all the links (I have included one).
   1. Once the DB is setup:
      1. You can run `python link_parser.py wiki_link.txt`
      2. This will create all the entries within the DB.

## Start the server

1. the server can be started by running:
   1. `uvicorn api:app`

## Tests

1. Tests currently need to be expanded on due to time constraints
   1. currently only test tasks
   2. need to add testing for:
      1. Models
      2. Some of the email tests with Mailgun API
      3. The API calls with FastAPI

## Project Information

### Used Utilities for Project

1. FastAPI
2. SQLAlchemy
3. Postgres for DB
4. Jinja2 for displaying pages

### Additional Project Information

1. A user signs up from the landing page.
2. An email is sent to the user for confirmation.
3. After the user is confirmed
   1. Confirmation email is sent to subscribe
4. Emails are sent at midnight everyday to all subscribers.
   1. Email contains donations page
   2. Wiki link to Black History.
   3. Unsubscribe option.
5. I am including a list of Black History links to be imported to the database via SQLAlchemy.
