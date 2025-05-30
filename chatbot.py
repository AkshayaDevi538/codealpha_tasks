import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (run this once)
nltk.download('punkt')

# Define a list of pattern-response pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created using NLTK.", "You can call me ChatBot."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem.", "Don't worry about it."]
    ],
    [
        r"i'm (.*) doing good",
        ["Great to hear that!", "Awesome!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help. What do you need?", "I'll do my best to assist you!"]
    ],
    [
        r"(.*) your name ?",
        ["You can call me ChatBot."]
    ],
    [
        r"quit",
        ["Bye-bye!", "Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["Tell me more...", "I see.", "Interesting. Go on...", "Could you elaborate on that?"]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
def start_chat():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chatbot.converse()

# Run the chatbot
if __name__ == "__main__":
    start_chat()
