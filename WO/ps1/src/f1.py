# Main python file for interacting with superpanty

import os
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


def read_table():
    response = supabase.table("dancers").select("*").execute()
    pprint(response)
