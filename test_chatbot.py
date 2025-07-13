#!/usr/bin/env python3
"""
Simple test script for the FriendlyCodeChatbot
"""

from coder_chatbot import FriendlyCodeChatbot

def test_chatbot():
    print("Testing FriendlyCodeChatbot...")
    
    # Create chatbot instance
    bot = FriendlyCodeChatbot()
    
    # Test questions
    test_questions = [
        "What is Python?",
        "How do I create a function in Python?",
        "What is a variable?"
    ]
    
    for question in test_questions:
        print(f"\nUser: {question}")
        try:
            answer = bot.ask(question)
            print(f"Bot: {answer}")
        except Exception as e:
            print(f"Error: {e}")
    
    print(f"\nChat history saved with {len(bot.history)} conversations")

if __name__ == "__main__":
    test_chatbot() 