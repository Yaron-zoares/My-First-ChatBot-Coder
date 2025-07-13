import tkinter as tk
from tkinter import messagebox
import json, os

class SimpleCodeChatbot:
    def __init__(self):
        self.history = []
        self.history_file = "chat_history.json"
        self.load_history()

    def load_history(self):
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                self.history = json.load(f)
        except:
            self.history = []

    def save_history(self):
        try:
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump(self.history, f, ensure_ascii=False)
        except Exception as e:
            print("Error saving history:", e)

    def ask(self, user_question):
        # Simple fallback response for now
        response = (
            f"Hello! You asked: '{user_question}'\n\n"
            "I'm a simple chatbot. Here are some programming tips:\n"
            "1. Use meaningful variable names\n"
            "2. Comment your code\n"
            "3. Test thoroughly\n"
            "4. Use version control\n"
            "5. Keep functions small and focused"
        )
        self.history.append((user_question, response))
        self.save_history()
        return response

def run_simple_gui():
    print("Starting Simple GUI...")
    bot = SimpleCodeChatbot()
    
    root = tk.Tk()
    root.title("Simple Code Chatbot")
    root.geometry("600x400")
    root.configure(bg="#2E2E2E")
    
    # Welcome message
    welcome_label = tk.Label(root, text="Welcome to Simple Code Chatbot!", 
                           bg="#2E2E2E", fg="#FFFFFF", font=("Arial", 14, "bold"))
    welcome_label.pack(pady=10)
    
    # Chat area
    chat_area = tk.Text(root, wrap=tk.WORD, width=70, height=20, 
                       font=("Consolas", 10), bg="#1E1E1E", fg="#FFFFFF")
    chat_area.pack(padx=10, pady=10)
    
    # Input area
    input_frame = tk.Frame(root, bg="#2E2E2E")
    input_frame.pack(fill="x", padx=10, pady=(0,10))
    
    user_input = tk.Entry(input_frame, font=("Consolas", 11), 
                         bg="#333333", fg="#FFFFFF")
    user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0,5))
    
    def send_message():
        question = user_input.get()
        if question.strip():
            user_input.delete(0, tk.END)
            
            # Add user message
            chat_area.insert(tk.END, f"You: {question}\n")
            
            # Get bot response
            response = bot.ask(question)
            chat_area.insert(tk.END, f"Bot: {response}\n\n")
            
            chat_area.see(tk.END)
    
    send_button = tk.Button(input_frame, text="Send", command=send_message)
    send_button.pack(side=tk.LEFT)
    
    user_input.bind("<Return>", lambda e: send_message())
    
    # Add initial message
    chat_area.insert(tk.END, "Bot: Hello! I'm a simple code chatbot. Ask me anything about programming!\n\n")
    
    print("GUI created, starting mainloop...")
    root.mainloop()
    print("GUI closed")

if __name__ == "__main__":
    run_simple_gui() 