import requests
from bs4 import BeautifulSoup


def scrape_news(url):
  """Fetches and scrapes news headlines from the given URL.

  Args:
      url: The URL of the webpage containing the news articles.

  Returns:
      A list of news headlines or snippets.
  """

  # Make a request to the webpage
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
  except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the webpage: {e}")
    return []

  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  # Extract the news article data
  data = []
  for item in soup.find("div", class_="timeline-scroller").find_all("li"):
    text = item.get_text(strip=True)
    if text:
      data.append(text)

  # Remove duplicates and return the data
  return list(set(data))


# Example usage: URL for Die Son sports section
url = "https://www.son.co.za/dieson/sport"
news_data = scrape_news(url)

# Print the scrapped data
print("\n======================")
print("Maandag, 25 Maart")
print("======================")
print("\n".join(news_data))
print("======================")
