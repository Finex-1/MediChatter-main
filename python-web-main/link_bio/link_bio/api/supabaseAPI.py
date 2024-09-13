import os
from dotenv import load_dotenv
from supabase import create_client, Client

class supabaseAPI:
    load_dotenv()

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    def data_cancer(self) -> list:
        response = self.supabase.table("data_cancer").select("*").execute()
        return response.data

    def data_covid(self) -> list:
        response = self.supabase.table("data_covid").select("*").execute()
        return response.data

    def data_diabetes(self) -> list:
        response = self.supabase.table("data_diabetes").select("*").execute()
        return response.data

    def data_life(self) -> list:
        response = self.supabase.table("data_life").select("*").execute()
        return response.data