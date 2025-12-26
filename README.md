# AI ChatBot

A simple yet powerful AI-powered chatbot with memory capabilities, built using Python. This chatbot leverages the Google Gemini API for natural language processing and maintains conversation history using SQLite for persistent memory.

## Features

- **Conversational AI**: Powered by Google Gemini for intelligent and context-aware responses
- **Persistent Memory**: Chat history is stored in a SQLite database, allowing the bot to remember past conversations
- **Context-Aware Responses**: Recent conversation history is used to provide coherent and relevant replies
- **CLI Interface**: Simple command-line interface for easy interaction
- **User Management**: Basic user identification system (expandable for multi-user support)
- **Easy Setup**: Minimal dependencies and straightforward configuration

## Prerequisites

- Python 3.7 or higher
- Google Gemini API key

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd AI_ChatBot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Obtain API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key for Google Gemini

2. **Environment Configuration**:
   - Create a `.env` file in the project root directory
   - Add your API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## Usage

1. **Run the chatbot**:
   ```bash
   python app.py
   ```

2. **Interact with the bot**:
   - Type your message and press Enter
   - The bot will respond based on the conversation context
   - Type 'exit' to quit the application

Example interaction:
```
🤖 AI Chatbot with Memory (type 'exit' to quit)

You: Hello, what's your name?
Bot: Hello! I'm an AI chatbot designed to have conversations with memory. How can I help you today?

You: What's the weather like?
Bot: I'm sorry, but I don't have access to real-time weather data. However, I can help you with general information or answer questions about various topics!

You: exit
```

## Project Structure

```
AI_ChatBot/
├── app.py              # Main application logic and CLI interface
├── database.py         # SQLite database setup and connection functions
├── memory.py           # Chat history management (save/retrieve messages)
├── llm.py              # Google Gemini API integration
├── requirements.txt    # Python dependencies
├── chatbot.db          # SQLite database file (created automatically)
├── .env                # Environment variables (API key)
└── README.md           # Project documentation
```

## Dependencies

- `google-generativeai`: Google Gemini API client library
- `python-dotenv`: Environment variable management

## How It Works

1. **Database Initialization**: The app creates necessary tables for users and chat history
2. **User Interaction**: Each message is saved to the database with user ID and role
3. **Context Building**: Recent messages are retrieved to build conversation context
4. **AI Response**: The context is sent to Google Gemini API for response generation
5. **Memory Update**: The AI response is saved back to the database

## Future Enhancements

- Web-based interface using Flask/Django
- Multi-user authentication system
- Voice input/output capabilities
- Integration with other AI models
- Conversation export functionality

## Troubleshooting

- **API Key Issues**: Ensure your `.env` file is in the correct location and contains a valid API key
- **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
- **Database Errors**: The database file is created automatically; ensure write permissions in the directory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**MOHD FARHAN** - SDE (Software Development Engineer)

---

*Built with ❤️ using Python, SQLite, and Google Gemini API*
