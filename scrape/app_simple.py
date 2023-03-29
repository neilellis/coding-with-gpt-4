import snscrape.modules.twitter as sntwitter
import datetime

# Function to get the latest headlines from BBC News
def get_latest_headlines(user, num_headlines):
    headlines = []
    for i, tweet in enumerate(sntwitter.TwitterUserScraper(user).get_items()):
        if i >= num_headlines:
            break
        headlines.append(tweet.content)
    return headlines

# Fetch the headlines
num_headlines = 10
bbc_headlines = get_latest_headlines('BBCNews', num_headlines)

# Save the headlines to a file
with open('headlines.md', 'w') as f:
    for i, headline in enumerate(bbc_headlines):
        f.write(f"{i + 1}. {headline}\n")

print("Headlines saved to 'headlines.md'")
