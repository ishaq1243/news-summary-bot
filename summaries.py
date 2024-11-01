from transformers import pipeline

def load_summarization_pipeline():
    """
    Load a summarization pipeline from HuggingFace.
    """
    return pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_words=500):
    """
    Chunk the text into smaller parts with a specified maximum number of words.
    :param text: The original text to be chunked
    :param max_words: Maximum number of words per chunk
    :return: List of text chunks
    """
    words = text.split()  # Split text into words
    chunks = [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return chunks

def summarize_texts(text: str, chunk_size: int = 500):
    """
    Summarize large text by breaking it into chunks if necessary.
    :param text: The input text to summarize
    :param chunk_size: Maximum chunk size (in words) to pass to the summarization model
    """
    summarizer = load_summarization_pipeline()
    
    # Chunk the text using the custom chunking function
    chunks = chunk_text(text, max_words=chunk_size)
    
    # Summarize each chunk
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    
    # Combine all summaries into a single string
    combined_summary = ' '.join(summaries)
    return combined_summary
