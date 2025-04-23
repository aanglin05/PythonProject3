import random
from datetime import datetime, timedelta

def generate_post(post_id):
    usernames = ['@joFisher', '@teupnext', '@thegreatdisappointment', '@illusionFusion']
    platforms = ['X', 'Instagram', 'Facebook', 'Twitch']
    news = [
        "Breaking: AI now able to read minds (Experts warn humanity at risk of leaking thoughts by 2027)",
        "Study shows that if you continue to drink water daily you will eventually start to hallucinate.",
        "Breaking: Yemen strikes northern Israel marking a rare targeting of this region.",
        "Breaking: Earth declares itself conscious, applies for United Nations membership.",
        "Breaking: World leaders to be replaced by AI clones after UN declares human error is way too risky.",
        "Breaking: U.S. tariff policies impacting global economy ",
        "New social media app reads your emotions and deletes posts if you’re too happy"
    ]
    credibility = ['fake', 'fake', 'true', 'fake', 'fake','true','fake']

    idr = random.randint(0, len(news) - 1)

    return {
        'id': f'post_{post_id}',
        'username': random.choice(usernames),
        'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 120)),
        'content': news[idr],
        'platform': random.choice(platforms),
        'credibility': credibility[idr],
        'shares': 0
    }

# simulated feed with 10 posts
feed = {f'post_{i}': generate_post(i) for i in range(10)}

#  the distribution of news
def spread_news(feed):
    distribution = {}
    for post_id, data in feed.items():
        base_shares = random.randint(10, 100) if data['credibility'] == 'fake' else random.randint(1, 20)
        multiplier = 2 if 'ai' in data['content'].lower() or 'earth' in data['content'].lower() else 1
        data['shares'] = base_shares * multiplier

        distribution[post_id] = {
            'content': data['content'],
            'credibility': data['credibility'],
            'shares': data['shares'],
            'platform': data['platform']
        }
    return distribution

#
spread = spread_news(feed)

for pid, info in spread.items():
    print(f"{pid}: ({info['credibility'].upper()}) {info['shares']} shares on {info['platform']} — \"{info['content']}\"")
