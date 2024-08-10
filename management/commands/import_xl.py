import pandas as pd
from django.core.management.base import BaseCommand
from home.models import vr_player

class Command(BaseCommand):
    help = 'Import data from an Excel file to the database'

    def add_arguments(self, parser):
        parser.add_argument('player_data', type=str, help='The path to the Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['player_data']

        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        # Iterate over the DataFrame and create model instances
        for _, row in df.iterrows():
            vr_player.objects.create(
                Name=row['Name'],
                Roll_number=row['Roll_number'],
                Branch=row['Branch'],
                Year=row['Year'],
                Email_id=row['Email_id'],
                Phone=row['Phone'],
                DOB=row['DOB'],
                Score=row['Score'],
            )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
