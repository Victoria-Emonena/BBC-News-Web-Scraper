import feedparser
import pandas as pd
import datetime

# URL of the BBC News RSS feed
rss_url = "https://feeds.bbci.co.uk/news/rss.xml"

# Parse the RSS feed
print("Parsing the RSS feed...")  # Debug message
ogbono = feedparser.parse(rss_url)

# Name of feed variable is 'ogbono' to represent the soup that is the feed data

# Check if feed is valid
print("Checking feed validity...")
if not ogbono.entries:  # If no entries found
    print("No entries found in the RSS feed. Please check the URL or the feed structure.")
    print(ogbono)  # Print the full feed structure for inspection
    exit()

# Print general feed details for context
print(f"Feed Title: {ogbono.feed.title}")
print(f"Feed Description: {ogbono.feed.description}")
print(f"Number of Entries: {len(ogbono.entries)}")

# Extract article details
print("Extracting articles...")
articles = []
for entry in ogbono.entries:
    # Debugging: Print each entry to check what is available
    print("\nProcessing new entry...")
    print(f"Title: {entry.title}")
    print(f"Description: {entry.description}")
    print(f"Link: {entry.link}")
    print(f"Published Date: {entry.published}")

    # Check for media_thumbnail existence
    thumbnail = entry.media_thumbnail[0]['url'] if 'media_thumbnail' in entry else None
    print(f"Thumbnail: {thumbnail}")

    # Append to articles list
    articles.append({
        "Title": entry.title,
        "Description": entry.description,
        "Link": entry.link,
        "Published Date": entry.published,
        "Thumbnail": thumbnail
    })

# Check if articles list is populated
if not articles:
    print("No articles were extracted. Exiting...")
    exit()

# Save to Excel
print("Saving to Excel...")
df = pd.DataFrame(articles)
filename = f"bbc_news_{datetime.datetime.now().strftime('%Y-%m-%d')}.xlsx"
try:
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")
except Exception as e:
    print(f"Error saving to Excel: {e}")
