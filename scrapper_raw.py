import requests
from bs4 import BeautifulSoup

# URL of the webpage with the tables
url = "https://www.loto.ro/loto-new/newLotoSiteNexioFinalVersion/web/app2.php/jocuri/649_si_noroc/rezultate_extragere.html"

# Send an HTTP GET request
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all table elements on the page
tables = soup.find_all("table")

# Initialize a list to store data from both tables
all_data = []

# Initialize a variable to count the number of rows

counter = 0

# Iterate through each table
for table in tables:
    table_data = []
    if counter < 2:
    # Iterate through rows in the table
        for row in table.find_all("tr"):
            row_data = []
            for cell in row.find_all(["th", "td"]):
                row_data.append(cell.get_text(strip=True))
            table_data.append(row_data)
    # Increment number of tables the loop iterated through
        counter += 1

        all_data.append(table_data)

# Print the scraped data from both tables
# for table_data in all_data:
#     print("Table:")
#     for row in table_data:
#         print(row)
#     print("\n")
print(all_data[0][1][0]) # all_data[table][row][value]
