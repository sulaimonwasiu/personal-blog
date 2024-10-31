# Personal Blog

A simple personal blog application built with Flask, allowing users to create, read, update, and delete articles. The application has two sections: a guest section for viewing articles and an admin section for managing them.

## Features

- **Guest Section**:
  - Home Page: Displays a list of published articles.
  - Article Page: Shows the content of a selected article along with its publication date.

- **Admin Section**:
  - Dashboard: Lists all articles with options to add, edit, or delete articles.
  - Add Article Page: Form to create a new article.
  - Edit Article Page: Form to modify an existing article.

- **Authentication**: Basic authentication for accessing the admin section.

## Technology Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Storage**: JSON files for article storage
- **Environment**: Python 3.x

## Project Structure

```
personal_blog/
├── flaskr/
│   ├── __init__.py
│   ├── auth.py
│   ├── blog.py
│   ├── storage.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── article.html
│   │   ├── dashboard.html
│   │   ├── add_article.html
│   │   └── edit_article.html
│   └── static/
│       └── style.css
├── articles/                # Directory to store article files
├── .env                     # Environment variables (for sensitive data)
├── requirements.txt         # Project dependencies
└── run.py                   # Entry point to run the Flask application
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sulaimonwasiu/personal_blog.git
   cd personal_blog
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create the articles directory**:
   ```bash
   mkdir articles
   ```

5. **Set environment variables** (optional):
   Create a `.env` file in the project root and add your sensitive data (like `SECRET_KEY`).

## Usage

1. **Run the application**:
   ```bash
   python run.py
   ```

2. **Access the blog**:
   - Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Admin Section**:
   - To access the admin section, log in using:
     - **Username**: `admin`
     - **Password**: `password` (This is a simple hardcoded example; consider using a more secure method for production).

4. **Manage Articles**:
   - From the dashboard, you can add, edit, or delete articles.

## Directory and File Structure

- **flaskr/**: Contains the main application code.
  - **auth.py**: Handles authentication.
  - **blog.py**: Manages blog functionality (CRUD operations on articles).
  - **storage.py**: Contains the `ArticleStorage` class for managing article files.
  - **templates/**: HTML files for rendering views.
  - **static/**: CSS files for styling.

- **articles/**: Directory where article JSON files are stored.

## Future Improvements

- Implement a more secure authentication mechanism.
- Add features like comments, tags, and categories.
- Use a database (e.g., PostgreSQL) for persistent storage.
- Implement a search functionality for articles.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/) - The web framework used for building the blog.
- [Markdown](https://daringfireball.net/projects/markdown/) - For formatting the README file.
```

