import os
import json
import datetime
import uuid

class ArticleStorage:
    def __init__(self, directory='articles'):
        self.directory = directory
        if not os.path.exists(directory):
            os.makedirs(directory)

    def save_article(self, title, content, id=None):
        # id = str(uuid.uuid4())
        filename = f"{id}.json"
        filepath = os.path.join(self.directory, filename)
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        if os.path.exists(filepath):
            # update existing blog
            article = {
                'id': id,
                'title': title,
                'content': content,
                'date': current_date
            }
            with open(filepath, 'w') as f:
                json.dump(article, f)
        else:
            # add new blog
            id = str(uuid.uuid4())
            filename = f"{id}.json"
            filepath = os.path.join(self.directory, filename)
            article = {
                'id': id,
                'title': title,
                'content': content,
                'date': current_date
            }
            with open(filepath, 'w') as f:
                json.dump(article, f)

    def get_articles(self):
        articles = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename)) as f:
                    articles.append(json.load(f))
        return articles

    def get_article(self, id):
        filepath = os.path.join(self.directory, f"{id}.json")
        if os.path.exists(filepath):
            with open(filepath) as f:
                return json.load(f)
        return None

    def delete_article(self, id):
        filepath = os.path.join(self.directory, f"{id}.json")
        if os.path.exists(filepath):
            os.remove(filepath)