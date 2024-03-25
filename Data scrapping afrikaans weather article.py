import requests
from bs4 import BeautifulSoup

# Scraping data from the first webpage
r = requests.get("https://www.son.co.za/dieson/sport")
soup = BeautifulSoup(r.content, 'html.parser')

# Add the <div> element for all the articles in the webpage
div_articles = []
for article in soup.find_all("article"):
    new_div = soup.new_tag("div")
    new_div.string = article.get_text()
    article.replace_with(new_div)
    div_articles.append(new_div)

# Extract the required data points
data_1 = [item.get_text(strip=True) for item in soup.find("div", class_="timeline-scroller").find_all("li") if item.get_text(strip=True) != '']

# Save the webpage content with the <div> elements
with open("webpage_1.html", "w", encoding="utf-8") as file:
    file.write(str(soup))

# Scraping data from the second webpage
r = requests.get("https://www.netwerk24.com/rapport/soek?query=weather")
soup = BeautifulSoup(r.content, 'html.parser')

# Add the <div> element for all the articles in the webpage
div_articles = []
for article in soup.find_all("article"):
    new_div = soup.new_tag("div")
    new_div.string = article.get_text()
    article.replace_with(new_div)
    div_articles.append(new_div)

# Prepare the list to store the texts
articles_texts = []

# Extract the texts from the article elements
for article in div_articles:
    article_text = article.get_text(strip=True)
    if article_text not in articles_texts:
        articles_texts.append(article_text)
    else:
        print("Duplicate: " + article_text)

# Save the extracted texts to a file
with open("extracted_data.txt", "w", encoding="utf-8") as file:
    file.write("\n\n".join(articles_texts))
