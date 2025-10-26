📰 Automatic Verified News Feed System
 Overview

This project is a Django-based web application integrated with AI workflow automation (n8n) to fetch, verify, and categorize news articles in real time.
It also includes a subscription system — whenever a new user subscribes, their details are automatically added to Google Sheets, and a separate workflow sends them email notifications for new verified news updates.

 Aim

To build an intelligent automated system that fetches and verifies real-time news using AI, filters fake information, categorizes articles, and notifies subscribed users instantly about verified updates.

🧠 Key Features

 Fetches latest articles from trusted RSS feeds

 Verifies authenticity using AI Agent Node( OpenAI) and fact checking

 Categorizes verified news into sections (Tech, Business, Health, etc.)

 Pushes verified results to Django backend via REST API

 Adds new subscriber details to Google Sheets via workflow

 Sends automated email notifications to subscribers

 Temporarily deployed using Ngrok

🧩 Tech Stack
Backend:

Django 5.x

Python 3.13

REST API

Frontend:

HTML, CSS, JavaScript

Automation & AI:

n8n Workflow Automation

Google Gemini / OpenAI / OpenRouter models

Google Sheets Node for subscription management

Email Node (Gmail ) for sending notifications

Deployment:

Ngrok (temporary URL for public access)

GitHub for version control

⚙️ System Workflow
🧾 News Verification Flow

RSS Feeds are fetched from trusted sources.

Each article is sent to AI Agent for verification.

The AI returns a JSON with:

is_true (True/False)

credibility_score (>40)

verification_notes (text)

Articles with credibility ≥ 50 are pushed to the Django backend.

Django web app displays verified, categorized articles to users.

📩 Subscriber Notification Flow

When a new user subscribes, their details (name, email) are added to Google Sheets via n8n.

A secondary workflow checks Google Sheets for new entries.

The workflow sends personalized email notifications to each subscriber whenever new verified articles are published.

💻 Installation Steps
# Clone the repository
git clone https://github.com/lasya2624/Authentic_news_verification.git
cd verified-news-feed

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start Django server
python manage.py runserver


Run the Zapier workflows for both:

 AI Verification Flow

 Email Subscription Flow

🔗 API Endpoint Example

POST /api/add-article/
Stores verified news from the workflow into the backend.

{
  "title": " ",
  "category": " ",
  "source_url": " ",
  "credibility_score": " ",
  "is_verified": true,
  "verified_by_sources": " "
}


POST /api/subscribe/
Adds user email to Google Sheets via workflow trigger.

{
  "name": "John Doe",
  "email": "john@example.com"
}

🧾 Example Output

Verified articles displayed with category tags.

Email updates automatically sent to subscribers.
