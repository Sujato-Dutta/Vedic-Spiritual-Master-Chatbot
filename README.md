# Vedic Spiritual Master Chatbot

A RAG-based chatbot that provides spiritual guidance using the wisdom of the Vedas, Upanishads, Bhagavad Gita and Yoga Vashishta.

## Setup

1.  **Install Dependencies**:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

2.  **Set up API Key**:
    -   Add your Google Gemini API key: `GOOGLE_API_KEY=your_key_here`.

3.  **Ingest Data**:
    -   This will read the texts from `data/` and create the vector database.
    ```bash
    python ingest_data.py
    ```

4.  **Run the App**:
    ```bash
    streamlit run app.py
    ```

## Data Sources
-   Bhagavad Gita
-   Advaita Vedanta
-   Kaivalya Upanishad
