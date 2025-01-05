# Main python file for interacting with superpanty

import os
from .utils import label1
from supabase import create_client, Client
from dotenv import load_dotenv
from rich import print as rprint  # For rprinting
from rich.pretty import pprint  # For pretty printing

# Custon en
load_dotenv(dotenv_path="pee")

# Env setup
url: str = os.environ.get("SUB")
key: str = os.environ.get("SUP")
supabase: Client = create_client(url, key)


rez = supabase.table("dancers").select("*").execute()


def read_table():
    label1("Printing with pprint")
    pprint(rez)


# Reading specific data
def read_data():
    label1("Reading Specific data data")
    rprint(rez)


# Inserting Data
