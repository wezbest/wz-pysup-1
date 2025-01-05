# Main python file for interacting with superpanty

import os
from supabase import create_client, Client
from rich import print as rprint  # For rprinting
from rich.pretty import pprint  # For pretty printing


# Env setup
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def read_table():
    response = supabase.table("countries").select("*").execute()
    pprint(response)