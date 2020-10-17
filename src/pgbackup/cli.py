from argparse import Action, ArgumentParser

""" This file facilitaes the CLI related logic"""


"""This deals with the 2 part flag that gives the user an option 
to use a s3 bucket or local path to backup databbase. This is unlike the
positional arg (the URL)."""


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        """ Handles for the driver(s3, or local) and the destination, 
        (name of bucket or name of local path)"""
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    """ Configure and return a parse that can be used when
    the tool is ran."""

    # Description of the parser
    parser = ArgumentParser(description=""" 
    Back up PostgreSQL databases locally or to AWS s3.
    """)
    parser.add_argument('url', help="URL of database to backup")
    parser.add_argument("--driver",
                        help="how & where to store backup",
                        nargs=2,  # Driver name, and a whether an bucket or local path would be used to back up database
                        action=DriverAction,  # Moving the action taking by this to the class 'DriverAction'
                        required=True)
    return parser
