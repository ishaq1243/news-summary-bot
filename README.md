# News-Summarization-App

A Streamlit-based web application that fetches and summarizes news articles. The app allows users to enter URLs of news websites or specific news articles, retrieve the content, and generate concise summaries. This tool is particularly useful for quickly understanding lengthy news articles without reading the entire text.

Features
Fetch News Articles: Supports both direct news article URLs and general news website URLs for article scraping.
Automatic Summarization: Uses state-of-the-art NLP models to generate summaries of news articles, even for lengthy content.
Handles Large Articles: Splits lengthy articles into manageable chunks before summarizing, ensuring smooth processing without errors.
User-Friendly Interface: Built with Streamlit for an easy-to-use web interface.
Demo

How It Works
Input URL: The user enters a URL of a news website or a specific article in the sidebar.
Article Scraping: If a website URL is entered, the app lists available articles, allowing the user to select one for summarization.
Text Chunking: For lengthy articles, the app splits the content into chunks to handle token limits in the summarization model.
Summarization: Each chunk is summarized separately, and the individual summaries are combined into a final summary.
Display Results: Both the original article text and the summarized content are displayed in the app.

Technologies Used
Streamlit: For building the web application interface.
Hugging Face Transformers: For summarization, using the facebook/bart-large-cnn model.
newspaper3k: For scraping news articles from various websites.


Prerequisites
Python 3.7 or above
An internet connection to download and load models from Hugging Face's Model Hub
