# Friendly Code Chatbot

A friendly and human-like chatbot for code questions, using free LLMs and knowledge sources.

## Features

- 🤖 AI-powered responses using Hugging Face models
- 💬 Two chat modes: Classic text mode and Bubble chat mode
- 🌙 Dark/Light theme toggle
- 📋 Copy bot responses to clipboard
- 💾 Automatic chat history saving
- 💡 Daily programming tips
- 🔧 Automatic code sample saving

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the chatbot:
```bash
python coder_chatbot.py
```

## Usage

### GUI Mode
- Type your programming questions in the input field
- Press Enter or click "Send" to get a response
- Use the buttons to:
  - **Clear**: Clear chat history
  - **Copy Bot**: Copy the last bot response to clipboard
  - **Day/Night Mode**: Toggle between light and dark themes
  - **Text/Bubble Mode**: Switch between classic text and bubble chat styles

### Test Mode
Run the test script to verify functionality:
```bash
python test_chatbot.py
```

## Files

- `coder_chatbot.py` - Main chatbot application
- `test_chatbot.py` - Test script for functionality verification
- `requirements.txt` - Python dependencies
- `chat_history.json` - Saved conversation history (created automatically)
- `code_sample.py` - Automatically saved code examples (created when code is detected)

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- transformers
- torch
- pyperclip (optional, for clipboard functionality)

## Notes

- The AI model will download on first use (may take several minutes)
- Internet connection required for AI model access
- Chat history is automatically saved between sessions
- Code samples are automatically saved when detected in responses 