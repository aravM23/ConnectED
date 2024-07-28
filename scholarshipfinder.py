import scrapy
import pandas as pd
from urllib.parse import urlparse
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path

class FullMastersScholarshipSpider(scrapy.Spider):
    name = 'full_masters_scholarship_spider'
    start_urls = [
        'https://www.fastweb.com',
        'https://www.scholarships.com',
        'https://bigfuture.collegeboard.org/scholarship-search',
        'https://www.niche.com/colleges/scholarships/',
        'https://www.chegg.com/scholarships',
        'https://www.petersons.com/scholarship-search.aspx',
        'https://www.unigo.com/scholarships',
        'https://www.collegegreenlight.com',
        'https://www.zinch.com',
        'https://www.goodcall.com/scholarships/',
        'https://www.scholarshipscanada.com',
        'https://www.scholarshipmonkey.com',
        'https://finaid.org',
        'https://www.raise.me/',
        'https://www.collegenet.com/elect/app/app',
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,  # Wait 2 seconds between requests
    }
    data = []

    def __init__(self):
        self.creds = None
        if os.path.exists('credentials.json'):
            self.creds = Credentials.from_authorized_user_file('credentials.json')

    def parse(self, response):
        # Extract the website name and scholarship details from the website
        website_name = urlparse(response.url).netloc.split('.')[0].capitalize()
        scholarship_details = self.scrape_scholarship_details(response, website_name)
        yield {
            'Website': website_name,
            'Website Link': response.url,
            'Scholarship Details': scholarship_details
        }
        self.data.append({
            'Website': website_name,
            'Website Link': response.url,
            'Scholarship Details': scholarship_details
        })

        # Check if the user has authorized the app and if the credentials are valid
        if self.creds and self.creds.valid:
            # Extract the deadline from the scholarship details
            deadline = self.extract_deadline(scholarship_details)
            if deadline:
                # Add the event to the user's Google Calendar
                self.add_event_to_calendar(title=scholarship_details, start=deadline, end=deadline)

    def parse(self, response):
        # Extract the website name and scholarship details from the website
        website_name = urlparse(response.url).netloc.split('.')[0].capitalize()
        scholarship_details = self.scrape_scholarship_details(response, website_name)
        yield {
            'Website': website_name,
            'Website Link': response.url,
            'Scholarship Details': scholarship_details
        }
        self.data.append({
            'Website': website_name,
            'Website Link': response.url,
            'Scholarship Details': scholarship_details
        })

    def scrape_scholarship_details(self, response, website_name):
        # This method should contain the logic to scrape the scholarship details from the website
        # It should return a string containing the relevant scholarship information
        if website_name == 'Fastweb':
            return self.scrape_scholarship1(response)
        elif website_name == 'Scholarships':
            return self.scrape_scholarship2(response)
        elif website_name == 'Collegeboard':
            return self.scrape_scholarship3(response)
        elif website_name == 'Niche':
            return self.scrape_scholarship4(response)
        elif website_name == 'Chegg':
            return self.scrape_scholarship5(response)
        elif website_name == 'Petersons':
            return self.scrape_scholarship6(response)
        elif website_name == 'Unigo':
            return self.scrape_scholarship7(response)
        elif website_name == 'Collegegreenlight':
            return self.scrape_scholarship8(response)
        elif website_name == 'Zinch':
            return self.scrape_scholarship9(response)
        elif website_name == 'Goodcall':
            return self.scrape_scholarship10(response)
        elif website_name == 'Scholarshipscanada':
            return self.scrape_scholarship11(response)
        elif website_name == 'Scholarshipmonkey':
            return self.scrape_scholarship12(response)
        elif website_name == 'Finaid':
            return self.scrape_scholarship13(response)
        elif website_name == 'Raise':
            return self.scrape_scholarship14(response)
        elif website_name == 'Collegenet':
            return self.scrape_scholarship15(response)
        else:
            return "No scholarship details found"

    def scrape_scholarship1(self, response):
        # Scrape scholarship details from Fastweb website
        scholarship_details = response.css('div.scholarship-details::text').get()
        return scholarship_details.strip()

    def scrape_scholarship2(self, response):
        # Scrape scholarship details from Scholarships website
        scholarship_details = response.css('p.scholarship-info::text').get()
        return scholarship_details.strip()

    def scrape_scholarship3(self, response):
        # Scrape scholarship details from Collegeboard website
        scholarship_details = response.css('span.scholarship-description::text').get()
        return scholarship_details.strip()

    def scrape_scholarship4(self, response):
        # Scrape scholarship details from Niche website
        scholarship_details = response.css('div.niche-scholarship-info::text').get()
        return scholarship_details.strip()

    def scrape_scholarship5(self, response):
        # Scrape scholarship details from Chegg website
        scholarship_details = response.css('p.chegg-scholarship-description::text').get()
        return scholarship_details.strip()

    def scrape_scholarship6(self, response):
        # Scrape scholarship details from Petersons website
        scholarship_details = response.css('span.petersons-scholarship-info::text').get()
        return scholarship_details.strip()

    def scrape_scholarship7(self, response):
        # Scrape scholarship details from Unigo website
        scholarship_details = response.css('div.unigo-scholarship-details::text').get()
        return scholarship_details.strip()

    def scrape_scholarship8(self, response):
        # Scrape scholarship details from Collegegreenlight website
        scholarship_details = response.css('p.collegegreenlight-scholarship-info::text').get()
        return scholarship_details.strip()

    def scrape_scholarship9(self, response):
        # Scrape scholarship details from Zinch website
        scholarship_details = response.css('span.zinch-scholarship-description::text').get()
        return scholarship_details.strip()

    def scrape_scholarship10(self, response):
        # Scrape scholarship details from Goodcall website
        scholarship_details = response.css('div.goodcall-scholarship-info::text').get()
        return scholarship_details.strip()

    def scrape_scholarship11(self, response):
        # Scrape scholarship details from Scholarshipscanada website
        scholarship_details = response.css('p.scholarshipscanada-scholarship-description::text').get()
        return scholarship_details.strip()

    def scrape_scholarship12(self, response):
        # Scrape scholarship details from Scholarshipmonkey website
        scholarship_details = response.css('span.scholarshipmonkey-scholarship-info::text').get()
        return scholarship_details.strip()

    def scrape_scholarship13(self, response):
        # Scrape scholarship details from Finaid website
        scholarship_details = response.css('div.finaid-scholarship-details::text').get()
        return scholarship_details.strip()

    def scrape_scholarship14(self, response):
        # Scrape scholarship details from Raise website
        scholarship_details = response.css('p.raise-scholarship-info::text').get()
        return scholarship_details.strip()

    def scrape_scholarship15(self, response):
        # Scrape scholarship details from Collegenet website
        scholarship_details = response.css('span.collegenet-scholarship-description::text').get()
        return scholarship_details.strip()

    def close(self, reason):
        # Authenticate the user and obtain the spreadsheet ID
        self.authenticate_user()
        super().close(reason)  # Add this line here

    def authenticate_user(self):
     # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        try:
            flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        except FileNotFoundError:
            print("Error: credentials.json file not found.")
            return

        creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

        # Get the spreadsheet ID from the user
        spreadsheet_id = input("Enter the spreadsheet ID: ")

        # Upload data to Google Spreadsheet
        self.upload_to_google_spreadsheet(spreadsheet_id, creds)

    def upload_to_google_spreadsheet(self, spreadsheet_id):
        service = build('sheets', 'v4', credentials=self.creds)
        sheet = service.spreadsheets()
        try:
            esult = sheet.values().update(
                spreadsheetId=spreadsheet_id,
                range='Sheet1!A1',
                valueInputOption='USER_ENTERED',
                body={
                '   values': [list(row.values()) for row in self.data]
                }
            ).execute()
            print('{0} cells updated.'.format(result.get('updatedCells')))
        except googleapiclient.errors.HttpError as e:
            if e.resp.status == 404:
                print(f"Error: Spreadsheet '{spreadsheet_id}' not found.")
            elif e.resp.status == 400:
                print(f"Error: Invalid range 'Sheet1!A1' for spreadsheet '{spreadsheet_id}'.")
            else:
                print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def add_event_to_calendar(self, title, start, end):
        # This method should add a new event to the user's Google Calendar
        calendar_service = build('calendar', 'v3', credentials=self.creds)
        event = {
            'summary': title,
            'start': {
                'dateTime': start.isoformat(),
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': end.isoformat(),
                'timeZone': 'America/Los_Angeles',
            },
        }
        created_event = calendar_service.events().insert(calendarId='primary', body=event).execute()
        print(f'Event created: {created_event.get("htmlLink")}')

if __name__ == "__main__":
    from scrapy.crawler import CrawlerProcess
    c = CrawlerProcess()
    c.crawl(FullMastersScholarshipSpider)
    c.start()