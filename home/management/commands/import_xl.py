import pandas as pd
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from home.models import Players
import re
class Command(BaseCommand):
    help = 'Import data from an Excel file to the database'

    def add_arguments(self, parser):
        parser.add_argument('player_data', type=str, help='The path to the Excel file')

    def generate_robohash_avatar(self, name):
        url = f'https://robohash.org/{name}.png'
        response = requests.get(url)
        if response.status_code == 200:
            return ContentFile(response.content)
        return None

    def handle(self, *args, **kwargs):
        file_path = kwargs['player_data']

        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        # Iterate over the DataFrame and create model instances
        for _, row in df.iterrows():
            avatar_file = self.generate_robohash_avatar(row['Name'])
            if avatar_file:
                print(avatar_file)
                player=Players(
                    Name=row['Name'],
                    Roll_number=row['Roll_number'],
                    Branch=row['Branch'],
                    Year=row['Year'],
                    Email_id=row['Email_id'],
                    Phone=row['Phone'],
                    DOB=row['DOB'],
                    Score=row['Score'],
                )
                clean_filename = re.sub(r'[^\w\s\.-]', '', row["Name"])[:100] + ".png"  # Limit filename length for safety
                player.Avatar.save(clean_filename, avatar_file)
                # player.Avatar.save(f'{row["Name"]}.png', avatar_file)
                player.save()
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
