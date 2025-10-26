Automatic News Feed System for Verified News
🚀 Overview

This project is a Django-based web application that displays verified and categorized news articles. It integrates AI-powered workflow automation (using Zapier) to fetch live news from multiple RSS feeds, verify their authenticity using AI agents, and publish only trustworthy news to users.

🎯 Aim

To develop a smart automated platform that collects real-time news, fact-checks its credibility using AI, and presents only authentic, categorized, and verified news articles for public consumption.

🧠 Key Features

Fetches latest news from multiple trusted RSS feeds

Uses AI Agent (OpenAI) for fact verification and web-based credibility checks

Filters out fake or low-credibility articles automatically

Categorizes news into Technology, Business, Sports, Health, Science, etc.

Displays verified articles via Django Web App

Uses Ngrok temporary deployment for live testing

🧩 Tech Stack
Backend:

Django 5.x

Python 3.13

REST API Integration

Frontend:

HTML, CSS, JavaScript

Automation & AI:

Zapier Workflow Automation

Google OpenAI model for fact verification

Deployment:

Ngrok (temporary tunnel)

GitHub for version control

⚙️ System Workflow

RSS Feeds are fetched from trusted news sources.

n8n Workflow processes each article and sends it to the AI Agent.

AI Verification: The agent checks authenticity, credibility score, and factual correctness.

Filtering: Only articles with credibility ≥ 50 are accepted.

Categorization: News is organized by topics (Tech, Health, Business, etc.).

Storage: Verified articles are pushed to Django backend via REST API.

Display: The web app shows only verified, categorized news to users.

💻 Installation Steps
# Clone the repository
git clone https://github.com/yourusername/verified-news-feed.git
cd verified-news-feed

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver


Then, run the Zapier workflow to start fetching and verifying news.

🔗 API Endpoint Example

POST /api/add-article/
Stores verified news from workflow into the Django database.

{
  "title": " ",
  "category": " ",
  "source_url": ,
  "credibility_score":  ,
  "is_verified": true,
  "verified_by_sources": " "
}

🧾 Example Output

✔️ Verified and categorized articles displayed on the homepage with credibility tags and category filters.
