# import pandas as pd
# import requests
# from django.core.management.base import BaseCommand
# from django.core.files.base import ContentFile
# from home.models import vr_zombie_Players,vr_ultimechs_Players,vr_pirate_Players,vr_pistol_Players,vr_racer_Players,vr_roller_Players
# import re
# class Command(BaseCommand):
#     help = 'Import data from an Excel file to the database'

#     def add_arguments(self, parser):
#         parser.add_argument('player_data', type=str, help='The path to the Excel file')

#     def generate_robohash_avatar(self, name):
#         url = f'https://robohash.org/{name}.png'
#         response = requests.get(url)
#         if response.status_code == 200:
#             return ContentFile(response.content)
#         return None

#     def handle(self, *args, **kwargs):
#         file_path = kwargs['player_data']

#         # Load the Excel file into a DataFrame
#         df = pd.read_excel(file_path)
#         # Iterate over the DataFrame and create model instances
#         for _, row in df.iterrows():
#             avatar_file = self.generate_robohash_avatar(row['Name'])
#             if avatar_file:
#                 print(avatar_file)
#                 player=vr_zombie_Players(
#                     Name=row['Name'],
#                     Roll_number=row['Roll_number'],
#                     Branch=row['Branch'],
#                     Year=row['Year'],
#                     Email_id=row['Email_id'],
#                     Phone=row['Phone'],
#                     DOB=row['DOB'],
#                     Score=row['Score'],
#                 )
#                 clean_filename = re.sub(r'[^\w\s\.-]', '', row["Name"])[:100] + ".png"  # Limit filename length for safety
#                 player.Avatar.save(clean_filename, avatar_file)
#                 # player.Avatar.save(f'{row["Name"]}.png', avatar_file)
#                 player.save()
#         self.stdout.write(self.style.SUCCESS('Data imported successfully'))

import os
import csv
import requests
from datetime import datetime
from supabase import create_client, Client
import re


# Set up Supabase client
url: str = "https://wrelzdetluebmnrnuuuj.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndyZWx6ZGV0bHVlYm1ucm51dXVqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU4NTg2MjUsImV4cCI6MjA0MTQzNDYyNX0.IMlBgdT3lvVg4tUQw_RxitSpaP4Yxxudcg31GTnOSLs"
supabase: Client = create_client(url, key)

def generate_robohash_avatar(roll_number: str) -> bytes:
    """Generate RoboHash avatar based on roll number"""
    url = f'https://robohash.org/{roll_number}.png'
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    return None

def upload_avatar_to_supabase(avatar_content: bytes, filename: str) -> str:
    """Upload avatar to Supabase Storage and return the public URL"""
    bucket_name = 'avatars'
    try:
        # Clean filename for storage compatibility
        clean_filename = re.sub(r'[^\w\s\.-]', '', filename)[:100] + ".png"
        # Upload to Supabase Storage
        response = supabase.storage().from_(bucket_name).upload(f'avatars/{clean_filename}', avatar_content)
        if response.status_code == 200:
            public_url = supabase.storage().from_(bucket_name).get_public_url(f'avatars/{clean_filename}')
            return public_url
        else:
            print(f"Failed to upload avatar: {response.json()}")
            return ''
    except Exception as e:
        print(f"Error uploading avatar: {e}")
        return ''

# Read data from CSV and insert into Supabase
with open('player_data.xlsx', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        roll_number = row.get('Roll_number', '')
        avatar_content = generate_robohash_avatar(roll_number)
        avatar_url = upload_avatar_to_supabase(avatar_content, row.get('Name', 'unknown'))

        # Prepare data for insertion
        player_data = {
            'Name': row.get('Name'),
            'Roll_number': roll_number,
            'Branch': row.get('Branch'),
            'Year': row.get('Year'),
            'Email_id': row.get('Email_id'),
            'Phone': row.get('Phone'),
            'DOB': row.get('DOB'),
            'Score': row.get('Score'),
            'Avatar': avatar_url,
            'Date': datetime.now().date(),
            'Time': datetime.now().time(),
        }

        # Insert data into Supabase table
        try:
            result = supabase.table('your_table_name').insert(player_data).execute()
            print(f"Successfully added: {result}")
        except Exception as e:
            print(f"Error inserting data: {e}")
