# Persona Bot

A simple Streamlit-based chatbot application that allows users to chat with different AI personas powered by Google's Gemini API.

## Features

- Multiple AI Personas
  - **SatBOT** – Sarcastic, witty, short-reply friend.
  - **SonBOT** – Creative, startup-loving, Bihar-supporting friend.
- Real-time streaming responses using Gemini.
- Chat history maintained during the session.
- Persona switching without restarting the application.
- Conversation logging to Google Sheets.
- Unique user identification for tracking interactions.

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Google Sheets
- dotenv

## Installation

```bash
git clone <repository-url>
cd persona-bot
pip install -r requirements.txt

```

## Create a Virtual Environment

```
- Create a virtual environment named 'venv'
python -m venv venv

- Activate the environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
## Environment Variables

Create a `.env` file:

```env
GOOGLE_GEMINI_KEY=your_gemini_api_key
```

## Local Google Sheets Link Configuration
Streamlit looks inside a specific configuration directory for local secrets.
- Create a folder named `.streamlit` in your project root directory.
- Inside that folder, create a file named `secrets.toml`.
- Paste your Google Sheet URL into it using the following format:

```
[connections.gsheets]
spreadsheet = "https://docs.google.com/spreadsheets/d/YOUR_SPS_ID_HERE/edit#gid=0"
```

## 📁 Project Structure

```text
├── main.py                # Main Streamlit application source code
├── .env                   # Local environment variables (API Keys)
└── requirements.txt       # Python package dependencies
```



## Run

```bash
streamlit run main.py
```

## Personas

### SatBOT
- Hinglish responses
- Sarcastic and concise
- Uses casual expressions like "bhai"

### SonBOT
- Hinglish responses
- Creative and startup-oriented
- Bihar enthusiast
- Intentionally imperfect spellings

## Logged Data

- timestamp
- user_id
- persona
- user_query
- bot_response


## Future Improvements

- Persistent memory
- More personas
- Authentication
- Analytics dashboard
- Voice support

## Disclaimer

This project is for educational and entertainment purposes. Persona behavior is controlled through prompt engineering and may vary depending on model responses.


