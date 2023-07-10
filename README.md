# YouTube Scraper
This repository contains a Flask web application that scrapes YouTube videos and displays their information including titles, views, and upload dates. The application allows users to enter a YouTube channel name and retrieves the information for the top 5 videos from that channel.

## Prerequisites
- Python 3.7 or above
- Pip package manager

## Installation
1. Clone this repository to your local machine.
`git clone git@github.com:Abhijit1102/youtube-scapper.git`
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required dependencies by running the following command:
4. `pip install -r requirements.txt`

## Usage
1. Run the Flask application by executing the following command in the terminal:
2. `python appplication.py`
3. The application will start running on your local server at http://127.0.0.1:8000/.
4. Open a web browser and navigate to the above URL to access the application.
5. Enter a YouTube channel name in the input field and click the "Submit" button.
6. The application will scrape the top 5 videos from the specified YouTube channel and display their information, including the video titles, views, and upload dates, on the results page.
7. If any errors occur during the scraping process, an error message will be displayed.

##  Project Structure
- `app.py`: Contains the main Flask application code, including route definitions and data scraping logic.
- `templates/`: Directory containing HTML templates for the web pages.
  - `index.html`: Template for the home page where users can enter the YouTube channel name.
  - `results.html`: Template for the results page where the scraped video information is displayed.
- static/: Directory containing static files for the web application.
  - `styles.css`: CSS file for styling the web pages.

## Contributing
Contributions to this project are welcome! If you have any suggestions, improvements, or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
This project was inspired by the need to easily retrieve and display information about YouTube videos from specific channels.
The Flask web framework and its ecosystem made it possible to quickly build and deploy the YouTube scraper application.
