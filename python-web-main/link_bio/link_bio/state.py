import reflex as rx
from link_bio.api.supabaseAPI import supabaseAPI

class DataState(rx.State):
    data_cancer: list = []
    data_life: list = []
    data_diabetes: list = []
    data_covid: list = []

    def load_all_data(self):
        supabase_client = supabaseAPI()
        self.data_cancer = supabase_client.data_cancer()
        self.data_life = supabase_client.data_life()
        self.data_diabetes = supabase_client.data_diabetes()
        self.data_covid = supabase_client.data_covid()