from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

# The target URL
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4'

# Perform an HTTP request to get the page content
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements that contain news titles
    titles = soup.find_all('a', {'class': 'news_tit'})

    # Extract the text of the titles and store them in a list
    title_list = [title.get_text() for title in titles]

    # Create a new Excel workbook and select the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "News Titles"

    # Add column header
    ws.append(["News Titles"])

    # Append all the titles to the worksheet
    for title in title_list:
        ws.append([title])

    # Save the workbook to a file
    wb.save('results.xlsx')
    
    print("The titles have been saved to 'results.xlsx'")
else:
    print("Failed to retrieve the webpage.")
