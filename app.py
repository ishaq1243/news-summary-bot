import streamlit as st
from newspaper import Article, build
from summaries import summarize_texts

# Streamlit UI setup
st.title("News Summarization App")

st.sidebar.header("Enter a News Website or Article URL")

# Input URL for a news site or article
url = st.sidebar.text_input("URL", "Enter a news website or article URL")

def process_article(url):
    """
    Process an article from a given URL, including downloading and parsing.
    Ensure the article has valid text content before processing further.
    """
    try:
        article = Article(url)
        article.download()
        article.parse()

        if not article.text or len(article.text.strip()) == 0:
            raise ValueError("No valid content found in the article.")

        return article.text

    except Exception as e:
        st.error(f"Failed to process the article at {url}. Error: {e}")
        return None

# If a URL is provided
if url:
    try:
        # If it's an article URL, process it directly
        if url.endswith(".html"):
            article_text = process_article(url)

            if article_text:
                st.subheader("Original Article")
                st.write(article_text)

                # Summarize the article, handling larger articles by splitting them into chunks
                st.subheader("Summarized Article")
                summary = summarize_texts(article_text)  # Summarize with chunking for larger articles
                st.write(summary)

        # If it's a website, scrape article URLs
        else:
            st.subheader("Scraping articles from website...")
            paper = build(url, memoize_articles=False)
            article_urls = [article.url for article in paper.articles]

            if article_urls:
                st.write(f"Found {len(article_urls)} articles.")
                selected_article = st.selectbox("Select an article to summarize", article_urls)
                
                article_text = process_article(selected_article)

                if article_text:
                    st.subheader("Original Article")
                    st.write(article_text)

                    # Summarize the selected article
                    st.subheader("Summarized Article")
                    summary = summarize_texts(article_text)  # Summarize with chunking for larger articles
                    st.write(summary)
            else:
                st.warning("No articles found on this website.")
    
    except Exception as e:
        st.error(f"Error processing URL: {e}")
else:
    st.info("Please enter a valid URL.")
