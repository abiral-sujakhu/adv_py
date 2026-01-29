import praw
from datetime import datetime

# Step 4: Replace these with your actual credentials from Reddit
CLIENT_ID = "YOUR_CLIENT_ID_HERE"
CLIENT_SECRET = "YOUR_CLIENT_SECRET_HERE"
USER_AGENT = "python:news_fetcher:v1.0 (by /u/YOUR_REDDIT_USERNAME)"

# Create Reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

print("=" * 70)
print("🔥 POPULAR NEWS FROM REDDIT")
print("=" * 70)

# Get popular posts from news subreddits
subreddits = ['news', 'worldnews', 'technology']

for subreddit_name in subreddits:
    print(f"\n📰 r/{subreddit_name}")
    print("-" * 70)
    
    subreddit = reddit.subreddit(subreddit_name)
    
    # Get top 5 hot posts
    for i, post in enumerate(subreddit.hot(limit=5), 1):
        print(f"\n{i}. {post.title}")
        print(f"   👤 Author: u/{post.author}")
        print(f"   ⬆️  Upvotes: {post.score}")
        print(f"   💬 Comments: {post.num_comments}")
        print(f"   🔗 URL: {post.url}")
        
        # Convert timestamp to readable format
        post_time = datetime.fromtimestamp(post.created_utc)
        print(f"   🕒 Posted: {post_time.strftime('%Y-%m-%d %H:%M:%S')}")

print("\n" + "=" * 70)
print("✅ Done!")
