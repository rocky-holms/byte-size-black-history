# Byte Size Black History

## Purpose

1. This is a website to subscribe to daily emails with a link to different African American History
   1. Will receive an email daily.
   2. Email will contain a link to donations page to different African American organizations.
   3. Email will contain a different wiki link sent daily.

## Current Site

1. This is the current URL to the site: https://bytesizeblackhistory.online
   1. Works with current implementation

## Setup

### Python Version

1. Requires Python 3.8 or greater

### Docker Environment Variables

1. `ENV MAILGUN_API_KEY` will need to be set with the Mailgun API Key
2. `ENV DOMAIN_NAME` will need to be set for email purposes
### Additional Settings
1. `docker build -t image_name .`
2. locally run the application within Docker with:
   * `docker run --name container_name -d -p 8000:80 image_id`
   * you can check the image id with `docker images`
### Crontab

1. Will need to be started within container
   * `/etc/init.d/cron start`
### Import Links

1. You can create a txt with all the links (I have included one).
   1. Once the DB is setup:
      1. You can run `python /app/src/utils/link_parser.py wiki_link.txt`
      2. This will create all the entries within the DB.

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
5. Docker
6. Poetry

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
