# ConnectED: Empowering Student Success

ConnectED is a comprehensive application designed to support students in their educational journey by providing tools for financial planning, scholarship discovery, and mentor matching. Leveraging cutting-edge technologies such as *natural language processing (NLP)* and *linear programming*, ConnectED offers students personalized and efficient solutions to overcome the challenges of higher education. Submitted to EmpowerHacks 2.0.

## Features 🚀
- **Financial Aid Calculator:** Calculates various financial components, including Expected Family Contribution (EFC), student and parent contributions, and the total financial aid package.
- **Tinder Style Scholarship Finder:** Utilizes Scrapy to scrape scholarship information from websites and manages data storage and calendar integration for scholarship deadlines.
- **Mentor Matching:** Matches students with mentors based on shared interests and expertise, utilizing NLP for keyword extraction and linear programming for optimal matching.

## The Design 🎨 
![Mockup](Mockup.png)

The full UI mockup is available **[here!](https://www.figma.com/proto/ghLS2guhHTHzSs6cTC5kCi/Untitled?node-id=1-511&t=hOaYrkqAJSAJqKbR-1)**

## Installation 🛠️
To set up the ConnectED application, follow these steps:
### Here's how to clone the repository:
```
git clone https://github.com/aravM23/ConnectED.git
cd ConnectED
```
### Here's how to install it:
```
pip install -r requirements.txt
```
## Usage 💡
Each module in ConnectED can be run independently depending on the needs of the user. Here’s how to use each feature:

### Financial Aid Calculator
Navigate to the directory containing FinancialAid.py and execute the script:
```
python FinancialAid.py
```
Follow the prompts to input your financial information and receive a detailed breakdown of your financial aid eligibility.

### Tinder Style Scholarship Finder
Run the scholarshipfinder.py script to start scraping scholarship data:
```
python scholarshipfinder.py
```
This script will scrape data, upload it to Google Sheets, and add relevant deadlines to your Google Calendar.

### Mentor Matching
Execute mentormatch.py to initiate the mentor matching process:
```
python mentormatch.py
```
Input your interests and the script will match you with a suitable mentor based on the data in mentorsLOLweneedafindthisman.csv.

## Contributing
Contributions are what make the open-source community such a powerful place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## Fork the Project
- Create your Feature Branch (git checkout -b feature/Feature)
- Commit your Changes (git commit -m 'Add some Feature')
- Push to the Branch (git push origin feature/Feature)
- Open a Pull Request

## License
Distributed under MIT License

## Other Details
The Notion containing our report and feauture breakdown is available **[here!](https://chain-impala-ab1.notion.site/ConnectED-Information-Report-e38477cdc0d64dea989d060dc2fb4c3b?pvs=4)**
