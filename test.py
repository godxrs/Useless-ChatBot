import praw
import json

from praw.reddit import Subreddit

# Reddit API credentials
client_id = 'yh9J1U5cAU3ePOALt9wk0Q'
client_secret = 'q3_fwd3WWrTMYLc4CPDpCRGc9A8gFg'
user_agent = 'Useless Chatbot/0.01 by God'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# query paramenrt
num_posts = 1

subreddit = reddit.subreddit('LearnJapanese')
posts  = subreddit.hot(limit=num_posts)

# Collect post data
data = []
for post in posts:
    post_info = {'comments': []}

    # Collect comments and replies, gracefully handling potential errors
    try:
        comments = post.comments.list()
        for comment in comments:
            comment_info = {'body': comment.body, 'replies': []}

            try:
                for reply in comment.replies:
                    reply_body = reply.body
                    comment_info['replies'].append(reply_body)
            except AttributeError:
                pass  # Skip non-comment objects

            post_info['comments'].append(comment_info)
    except AttributeError:
        pass  # Skip posts without comments

    data.append(post_info)

# Save the data to a JSON file
with open('useless_discussions.json', 'w') as file:
    json.dump(data, file, indent=4)