def create_email_text(wiki_link: str) -> str:
    """
    Create text being added to emails.

    Args:
        wiki_link (str): link to activist.

    Returns:
        str: Text being added to emails.
    """
    text: str = f"""
    Today we are presenting another activist\n\n
    You can find them here at this link: {wiki_link}\n\n
    We appreciate your subscription as always, and below we have some donation links.\n\n
    NAACP Donation Page: https://www.naacp.org/Donate/\n
    ACLU Donation Page: https://action.aclu.org/give/now\n
    Know your rights Camp Donation: https://www.knowyourrightscamp.com\n
    """
    return text
