from coder_chatbot import FriendlyCodeChatbot

bot = FriendlyCodeChatbot()

# Test different inputs
test_inputs = [
    "Q", 
    "hello", 
    "python", 
    "what is programming", 
    "help", 
    "what is a variable", 
    "how do I create a function",
    "deepfake detection",
    "computer vision",
    "machine learning"
]

print("Testing improved chatbot responses:")
print("=" * 50)

for test_input in test_inputs:
    print(f"\nInput: '{test_input}'")
    response = bot.get_smart_response(test_input)
    # Truncate long responses for readability
    if len(response) > 200:
        response = response[:200] + "..."
    print(f"Response: {response}")
    print("-" * 30) 