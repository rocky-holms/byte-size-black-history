import argparse
import logging
import os
import sys
from typing import Union

from sqlalchemy import insert, exc

from db import db_session
from models import WikiLink

my_parser = argparse.ArgumentParser(
    description="Take in filename of txt with Wiki links."
)


my_parser.add_argument(
    "File", metavar="file", type=str, help="The path to Wiki link file."
)

args = my_parser.parse_args()

filename = args.File

if not os.path.isfile(filename):
    print("Please enter a valid file to parse")
    sys.exit()


def parsed_link_data(line: str) -> Union[list, None]:
    """Parse link data to be commited via sqlalchemy.

    Args:
        line (str): link to page.

    Returns:
        Union[list, None]: return data if any data to return.
    """
    if line:
        try:
            parsed_line: list = line.split("/")
            title: str = parsed_line[-1].strip().replace("_", " ")
            url: str = line.strip()
            values: dict = {"title": title, "url": url}
            return values
        except Exception as e:
            logging.error(f"Unable to parse line {line} | Error: {e}")


def link_to_db(link_data: dict) -> None:
    """Commit link and title to the DB.

    Args:
        link_data (dict): data for the Wikilink model.
    """
    try:
        insert_statement = insert(WikiLink).values(link_data)
        db_session.execute(insert_statement)
        db_session.commit()
    except exc.IntegrityError:
        db_session.rollback()
        logging.error(f"Link data already in DB: {link_data}")
    except Exception as e:
        logging.error(f"Unable to add data to DB. Data: {link_data} | Error: {e}")


def parse_links(filename) -> None:
    """Parse links and commits to DB.

    Args:
        filename ([type]): Name of the file with links.
    """
    with open(filename) as f:
        content = f.readlines()

        for line in content:
            data: Union[tuple, None] = parsed_link_data(line)
            if data:
                link_to_db(data)


if __name__ == "__main__":
    parse_links(filename)
