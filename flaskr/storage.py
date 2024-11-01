import os
import json
import datetime
import uuid

class ArticleStorage:
    def __init__(self, directory='articles'):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    def _get_file_path(self, article_id):
        return os.path.join(self.directory, f"{article_id}.json")

    def _get_current_date(self):
        return datetime.datetime.now().strftime("%B %d, %Y")

    def _create_article_dict(self, title, content, article_id):
        return {
            'id': article_id,
            'title': title,
            'content': content,
            'date': self._get_current_date()
        }

    def save_article(self, title, content, article_id=None):
        if article_id is None:
            article_id = str(uuid.uuid4())

        filepath = self._get_file_path(article_id)
        article = self._create_article_dict(title, content, article_id)

        with open(filepath, 'w') as f:
            json.dump(article, f)

    def get_articles(self):
        articles = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename)) as f:
                    articles.append(json.load(f))
        return articles

    def get_article(self, article_id):
        filepath = self._get_file_path(article_id)
        if os.path.exists(filepath):
            with open(filepath) as f:
                return json.load(f)
        return None

    def delete_article(self, article_id):
        filepath = self._get_file_path(article_id)
        if os.path.exists(filepath):
            os.remove(filepath)