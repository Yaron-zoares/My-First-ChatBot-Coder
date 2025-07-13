#  bash: python coder_chatbot.py
#  Friendly and human-like chatbot for code questions - INSTANT RESPONSE VERSION
# No AI model loading - only smart response system

import tkinter as tk
from tkinter import messagebox
import json
import os
import threading
import time
import re

# Try to import pyperclip for clipboard support
try:
    import pyperclip
    _pyperclip_available = True
except ImportError:
    _pyperclip_available = False

# Daily tip (in English)
DAILY_TIP = "💡 Tip: Use f-strings in Python instead of concatenation to improve readability!"

class FriendlyCodeChatbot:
    def __init__(self):
        self.history = []
        self.history_file = "chat_history.json"
        self.load_history()

    def load_history(self):
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                self.history = json.load(f)
        except Exception:
            self.history = []

    def save_history(self):
        try:
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump(self.history, f, ensure_ascii=False)
        except Exception as e:
            print("Error saving history:", e)

    def get_smart_response(self, user_question):
        """Enhanced simple response system with comprehensive programming knowledge"""
        question_lower = user_question.lower()
        
        # Handle very short or unclear inputs
        if len(user_question.strip()) <= 2:
            return ("I see you sent a short message! I'm here to help with programming questions. 😊\n\n"
                   "Try asking me about:\n"
                   "• Python programming\n"
                   "• JavaScript and web development\n"
                   "• HTML/CSS\n"
                   "• Programming concepts like loops, functions, classes\n"
                   "• Debugging and problem solving\n"
                   "• Git and version control\n\n"
                   "What would you like to learn about?")
        
        # Greetings
        if any(word in question_lower for word in ["hello", "hi", "hey", "greetings"]) and len(question_lower.split()) <= 2:
            return "Hello! I'm your friendly code chatbot. How can I help you with programming today? 😊"
        
        # Python specific
        if "python" in question_lower:
            if "list" in question_lower or "array" in question_lower:
                return ("Python Lists are powerful! Here's a quick example:\n\n"
                       "```python\n"
                       "numbers = [1, 2, 3, 4, 5]\n"
                       "squares = [x**2 for x in numbers]  # List comprehension\n"
                       "print(squares)  # [1, 4, 9, 16, 25]\n"
                       "```\n\n"
                       "Lists are mutable, ordered, and can contain mixed types!")
            
            if "dictionary" in question_lower or "dict" in question_lower:
                return ("Python Dictionaries are key-value stores:\n\n"
                       "```python\n"
                       "person = {\n"
                       "    'name': 'Alice',\n"
                       "    'age': 30,\n"
                       "    'city': 'New York'\n"
                       "}\n"
                       "print(person['name'])  # Alice\n"
                       "person['job'] = 'Developer'  # Add new key\n"
                       "```")
            
            if "function" in question_lower or "def" in question_lower:
                return ("Python Functions are defined with 'def':\n\n"
                       "```python\n"
                       "def greet(name, greeting='Hello'):\n"
                       "    return f'{greeting}, {name}!'\n"
                       "\n"
                       "result = greet('World')\n"
                       "print(result)  # Hello, World!\n"
                       "```")
            
            if "class" in question_lower or "oop" in question_lower:
                return ("Python Classes and OOP:\n\n"
                       "```python\n"
                       "class Person:\n"
                       "    def __init__(self, name, age):\n"
                       "        self.name = name\n"
                       "        self.age = age\n"
                       "    \n"
                       "    def greet(self):\n"
                       "        return f'Hello, I am {self.name}'\n"
                       "\n"
                       "person = Person('Alice', 30)\n"
                       "print(person.greet())  # Hello, I am Alice\n"
                       "```")
            
            return ("Python is amazing! Key concepts:\n\n"
                   "• **Variables**: `name = 'Python'`\n"
                   "• **Functions**: `def my_func():`\n"
                   "• **Lists**: `items = [1, 2, 3]`\n"
                   "• **Dictionaries**: `data = {'key': 'value'}`\n"
                   "• **F-strings**: `f'Hello {name}'`\n"
                   "• **Classes**: `class MyClass:`\n\n"
                   "What specific Python topic do you want to learn?")
        
        # String operations (capital letters, case conversion)
        if any(word in question_lower for word in ["capital", "uppercase", "lowercase", "case", "letter"]):
            return ("Python String Case Operations:\n\n"
                   "```python\n"
                   "text = 'hello world'\n"
                   "\n"
                   "# Convert to uppercase\n"
                   "upper_text = text.upper()\n"
                   "print(upper_text)  # HELLO WORLD\n"
                   "\n"
                   "# Convert to lowercase\n"
                   "lower_text = text.lower()\n"
                   "print(lower_text)  # hello world\n"
                   "\n"
                   "# Capitalize first letter\n"
                   "cap_text = text.capitalize()\n"
                   "print(cap_text)  # Hello world\n"
                   "\n"
                   "# Title case (capitalize each word)\n"
                   "title_text = text.title()\n"
                   "print(title_text)  # Hello World\n"
                   "```")
        
        # Mathematical operations (sum, addition)
        if any(word in question_lower for word in ["sum", "add", "addition", "math", "calculate", "number"]):
            return ("Python Mathematical Operations:\n\n"
                   "```python\n"
                   "# Basic addition\n"
                   "a = 5\n"
                   "b = 3\n"
                   "sum_result = a + b\n"
                   "print(sum_result)  # 8\n"
                   "\n"
                   "# Sum of a list\n"
                   "numbers = [1, 2, 3, 4, 5]\n"
                   "total = sum(numbers)\n"
                   "print(total)  # 15\n"
                   "\n"
                   "# Using sum() with range\n"
                   "range_sum = sum(range(1, 6))  # 1+2+3+4+5\n"
                   "print(range_sum)  # 15\n"
                   "\n"
                   "# Sum with list comprehension\n"
                   "squares_sum = sum([x**2 for x in range(1, 6)])\n"
                   "print(squares_sum)  # 55 (1+4+9+16+25)\n"
                   "```")
        
        # JavaScript specific
        if "javascript" in question_lower or "js" in question_lower:
            if "function" in question_lower:
                return ("JavaScript Functions:\n\n"
                       "```javascript\n"
                       "// Regular function\n"
                       "function greet(name) {\n"
                       "    return `Hello, ${name}!`;\n"
                       "}\n"
                       "\n"
                       "// Arrow function\n"
                       "const greetArrow = (name) => `Hello, ${name}!`;\n"
                       "```")
            
            if "array" in question_lower:
                return ("JavaScript Arrays:\n\n"
                       "```javascript\n"
                       "const numbers = [1, 2, 3, 4, 5];\n"
                       "const doubled = numbers.map(x => x * 2);\n"
                       "const filtered = numbers.filter(x => x > 2);\n"
                       "console.log(doubled);  // [2, 4, 6, 8, 10]\n"
                       "```")
            
            if "async" in question_lower or "promise" in question_lower:
                return ("JavaScript Async/Await:\n\n"
                       "```javascript\n"
                       "async function fetchData() {\n"
                       "    try {\n"
                       "        const response = await fetch('https://api.example.com/data');\n"
                       "        const data = await response.json();\n"
                       "        return data;\n"
                       "    } catch (error) {\n"
                       "        console.error('Error:', error);\n"
                       "    }\n"
                       "}\n"
                       "```")
            
            return ("JavaScript for web development:\n\n"
                   "• **Variables**: `let`, `const`, `var`\n"
                   "• **Functions**: Regular and arrow functions\n"
                   "• **Arrays**: `map()`, `filter()`, `reduce()`\n"
                   "• **Objects**: Key-value pairs\n"
                   "• **Template literals**: `` `Hello ${name}` ``\n"
                   "• **Async/Await**: Promise handling\n\n"
                   "What JavaScript topic interests you?")
        
        # HTML/CSS
        if "html" in question_lower:
            return ("HTML Structure:\n\n"
                   "```html\n"
                   "<!DOCTYPE html>\n"
                   "<html>\n"
                   "<head>\n"
                   "    <title>My Page</title>\n"
                   "</head>\n"
                   "<body>\n"
                   "    <header>\n"
                   "        <h1>Welcome</h1>\n"
                   "    </header>\n"
                   "    <main>\n"
                   "        <p>Content here</p>\n"
                   "    </main>\n"
                   "</body>\n"
                   "</html>\n"
                   "```\n\n"
                   "Use semantic tags for better accessibility!")
        
        if "css" in question_lower:
            return ("CSS Styling:\n\n"
                   "```css\n"
                   ".container {\n"
                   "    display: flex;\n"
                   "    justify-content: center;\n"
                   "    align-items: center;\n"
                   "    background-color: #f0f0f0;\n"
                   "    padding: 20px;\n"
                   "}\n"
                   "\n"
                   "/* Responsive design */\n"
                   "@media (max-width: 768px) {\n"
                   "    .container {\n"
                   "        flex-direction: column;\n"
                   "    }\n"
                   "}\n"
                   "```")
        
        # General programming concepts
        if "loop" in question_lower:
            return ("Loops in different languages:\n\n"
                   "**Python:**\n"
                   "```python\n"
                   "for i in range(5):\n"
                   "    print(i)\n"
                   "```\n\n"
                   "**JavaScript:**\n"
                   "```javascript\n"
                   "for (let i = 0; i < 5; i++) {\n"
                   "    console.log(i);\n"
                   "}\n"
                   "```")
        
        if "error" in question_lower or "debug" in question_lower:
            return ("Debugging Tips:\n\n"
                   "1. **Read the error message** - it tells you what's wrong\n"
                   "2. **Check line numbers** - errors point to specific lines\n"
                   "3. **Use print statements** - see what your code is doing\n"
                   "4. **Break it down** - test small parts separately\n"
                   "5. **Google the error** - someone else probably had the same issue\n\n"
                   "What specific error are you seeing?")
        
        if "git" in question_lower:
            return ("Git Basics:\n\n"
                   "```bash\n"
                   "git init                    # Start new repository\n"
                   "git add .                   # Stage all changes\n"
                   "git commit -m 'message'     # Save changes\n"
                   "git push origin main        # Upload to remote\n"
                   "git pull                    # Download changes\n"
                   "```\n\n"
                   "Always commit frequently with clear messages!")
        
        if "api" in question_lower or "rest" in question_lower:
            return ("REST API Basics:\n\n"
                   "```javascript\n"
                   "// GET request\n"
                   "fetch('https://api.example.com/users')\n"
                   "    .then(response => response.json())\n"
                   "    .then(data => console.log(data));\n"
                   "\n"
                   "// POST request\n"
                   "fetch('https://api.example.com/users', {\n"
                   "    method: 'POST',\n"
                   "    headers: {'Content-Type': 'application/json'},\n"
                   "    body: JSON.stringify({name: 'John', age: 30})\n"
                   "});\n"
                   "```")
        
        # AI/ML and Computer Vision topics
        if any(word in question_lower for word in ["deepfake", "deep fake", "fake video", "video analysis", "computer vision", "ai", "machine learning", "ml"]):
            if "deepfake" in question_lower or "fake video" in question_lower:
                return ("Deepfake Detection and Analysis! 🤖\n\n"
                       "**Python Example using OpenCV and MediaPipe:**\n"
                       "```python\n"
                       "import cv2\n"
                       "import mediapipe as mp\n"
                       "import numpy as np\n"
                       "\n"
                       "def analyze_video_for_deepfake(video_path):\n"
                       "    # Initialize MediaPipe Face Detection\n"
                       "    mp_face_detection = mp.solutions.face_detection\n"
                       "    face_detection = mp_face_detection.FaceDetection()\n"
                       "    \n"
                       "    cap = cv2.VideoCapture(video_path)\n"
                       "    \n"
                       "    while cap.isOpened():\n"
                       "        ret, frame = cap.read()\n"
                       "        if not ret:\n"
                       "            break\n"
                       "        \n"
                       "        # Convert to RGB for MediaPipe\n"
                       "        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)\n"
                       "        results = face_detection.process(rgb_frame)\n"
                       "        \n"
                       "        if results.detections:\n"
                       "            for detection in results.detections:\n"
                       "                # Analyze face landmarks for inconsistencies\n"
                       "                bbox = detection.location_data.relative_bounding_box\n"
                       "                # Add your deepfake detection logic here\n"
                       "        \n"
                       "    cap.release()\n"
                       "    return 'Analysis complete'\n"
                       "```\n\n"
                       "**Key Deepfake Detection Methods:**\n"
                       "• **Face Landmark Analysis**: Check for unnatural facial movements\n"
                       "• **Blinking Patterns**: Deepfakes often have irregular blinking\n"
                       "• **Lighting Inconsistencies**: Look for shadows that don't match\n"
                       "• **Audio-Visual Sync**: Check if lip movements match audio\n"
                       "• **Metadata Analysis**: Examine video file properties\n\n"
                       "**Libraries to use:**\n"
                       "• OpenCV (cv2) - Video processing\n"
                       "• MediaPipe - Face detection and landmarks\n"
                       "• TensorFlow/PyTorch - Deep learning models\n"
                       "• scikit-learn - Traditional ML algorithms")
            
            if "computer vision" in question_lower:
                return ("Computer Vision with Python! 👁️\n\n"
                       "**Basic Image Processing Example:**\n"
                       "```python\n"
                       "import cv2\n"
                       "import numpy as np\n"
                       "\n"
                       "def process_image(image_path):\n"
                       "    # Read image\n"
                       "    img = cv2.imread(image_path)\n"
                       "    \n"
                       "    # Convert to grayscale\n"
                       "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n"
                       "    \n"
                       "    # Edge detection\n"
                       "    edges = cv2.Canny(gray, 50, 150)\n"
                       "    \n"
                       "    # Face detection\n"
                       "    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')\n"
                       "    faces = face_cascade.detectMultiScale(gray, 1.1, 4)\n"
                       "    \n"
                       "    return faces\n"
                       "```\n\n"
                       "**Popular Computer Vision Libraries:**\n"
                       "• **OpenCV**: Image and video processing\n"
                       "• **MediaPipe**: Face, hand, and pose detection\n"
                       "• **Pillow (PIL)**: Image manipulation\n"
                       "• **scikit-image**: Scientific image processing")
            
            return ("AI and Machine Learning Basics! 🤖\n\n"
                   "**Simple ML Example with scikit-learn:**\n"
                   "```python\n"
                   "from sklearn.model_selection import train_test_split\n"
                   "from sklearn.ensemble import RandomForestClassifier\n"
                   "import pandas as pd\n"
                   "\n"
                   "# Load data\n"
                   "data = pd.read_csv('your_data.csv')\n"
                   "X = data.drop('target', axis=1)\n"
                   "y = data['target']\n"
                   "\n"
                   "# Split data\n"
                   "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n"
                   "\n"
                   "# Train model\n"
                   "model = RandomForestClassifier()\n"
                   "model.fit(X_train, y_train)\n"
                   "\n"
                   "# Make predictions\n"
                   "predictions = model.predict(X_test)\n"
                   "```\n\n"
                   "**Popular AI/ML Libraries:**\n"
                   "• **TensorFlow**: Deep learning framework\n"
                   "• **PyTorch**: Research-focused deep learning\n"
                   "• **scikit-learn**: Traditional machine learning\n"
                   "• **Keras**: High-level neural network API")
        
        # General programming questions
        if any(word in question_lower for word in ["what is", "explain", "how to", "how do", "what are", "tell me"]):
            if "programming" in question_lower or "code" in question_lower:
                return ("Programming is the art of giving instructions to computers! 🖥️\n\n"
                       "**Key Concepts:**\n"
                       "• **Variables**: Store data (like `name = 'John'`)\n"
                       "• **Functions**: Reusable blocks of code\n"
                       "• **Loops**: Repeat actions (for, while)\n"
                       "• **Conditions**: Make decisions (if/else)\n"
                       "• **Data Structures**: Organize data (lists, dictionaries)\n\n"
                       "**Popular Languages:**\n"
                       "• **Python**: Great for beginners, data science, web apps\n"
                       "• **JavaScript**: Web development, frontend and backend\n"
                       "• **Java**: Enterprise applications, Android apps\n"
                       "• **C++**: System programming, games, performance\n\n"
                       "What specific aspect of programming interests you?")
            
            if "variable" in question_lower:
                return ("Variables are containers that store data in programming! 📦\n\n"
                       "**Python Example:**\n"
                       "```python\n"
                       "name = 'Alice'          # String variable\n"
                       "age = 25               # Integer variable\n"
                       "height = 1.75          # Float variable\n"
                       "is_student = True      # Boolean variable\n"
                       "```\n\n"
                       "**JavaScript Example:**\n"
                       "```javascript\n"
                       "let name = 'Alice';    // String variable\n"
                       "const age = 25;        // Constant (can't change)\n"
                       "var height = 1.75;     // Old way (avoid)\n"
                       "```\n\n"
                       "Variables can store different types of data and can be changed during program execution!")
            
            if "function" in question_lower:
                return ("Functions are reusable blocks of code that perform specific tasks! 🔧\n\n"
                       "**Python Example:**\n"
                       "```python\n"
                       "def greet(name):\n"
                       "    return f'Hello, {name}!'\n"
                       "\n"
                       "result = greet('World')\n"
                       "print(result)  # Hello, World!\n"
                       "```\n\n"
                       "**JavaScript Example:**\n"
                       "```javascript\n"
                       "function greet(name) {\n"
                       "    return `Hello, ${name}!`;\n"
                       "}\n"
                       "\n"
                       "const result = greet('World');\n"
                       "console.log(result);  // Hello, World!\n"
                       "```\n\n"
                       "Functions help organize code and avoid repetition!")
        
        # Default response with programming topics
        return ("I'm here to help with programming! Here are some topics I can assist with:\n\n"
               "🔹 **Languages**: Python, JavaScript, HTML/CSS, Java, C++\n"
               "🔹 **Concepts**: Functions, loops, data structures, OOP\n"
               "🔹 **Tools**: Git, debugging, testing, IDEs\n"
               "🔹 **Web Dev**: Frontend, backend, APIs, databases\n"
               "🔹 **Best Practices**: Clean code, documentation, performance\n\n"
               "💡 **Try asking me specific questions like:**\n"
               "• \"How do I create a function in Python?\"\n"
               "• \"What are JavaScript arrays?\"\n"
               "• \"How do I debug my code?\"\n"
               "• \"Explain loops in programming\"\n"
               "• \"What is Git?\"\n\n"
               "Just ask me anything programming-related! 🚀")

    def ask(self, user_question):
        # Use smart response system for instant answers
        answer = self.get_smart_response(user_question)
        self.history.append((user_question, answer))
        self.save_history()
        return answer

# Classic/Bubble view mode flag
show_classic_mode = False

def run_gui():
    global show_classic_mode
    print("Starting GUI...")
    bot = FriendlyCodeChatbot()
    bg_color = "#2E2E2E"
    text_color = "#FFFFFF"

    root = tk.Tk()
    root.title("Friendly Code Chatbot (Free LLMs)")
    root.configure(bg=bg_color)

    # Ensure window appears and is focused
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.geometry("800x600")
    root.resizable(True, True)

    print("GUI window created")

    # Daily tip label
    tip_label = tk.Label(root, text=DAILY_TIP, bg=bg_color, fg="#FFD700", font=("Segoe UI", 9, "italic"))
    tip_label.pack(pady=(5, 0))
    
    # Status label
    status_label = tk.Label(root, text="Instant Mode Ready! ⚡", bg=bg_color, fg="#00FF00", font=("Segoe UI", 9))
    status_label.pack(pady=(2, 0))

    # Classic chat area (Text widget)
    chat_area = tk.Text(
        root, wrap=tk.WORD, width=80, height=25, font=("Consolas", 11),
        bg="#1E1E1E", fg="#FFFFFF", state='disabled'
    )
    chat_area.pack(padx=10, pady=10)

    # Bubble chat area (Frame)
    bubbles_frame = tk.Frame(root, bg=bg_color)
    # Not shown by default

    def show_classic():
        chat_area.pack(padx=10, pady=10)
        bubbles_frame.pack_forget()
        refresh_classic_chat()

    def show_bubbles():
        chat_area.pack_forget()
        bubbles_frame.pack(padx=10, pady=10, fill="both", expand=True)
        refresh_bubbles_chat()

    def refresh_classic_chat():
        chat_area.config(state='normal')
        chat_area.delete(1.0, tk.END)
        for user, bot_msg in bot.history:
            chat_area.insert(tk.END, f"User: {user}\n")
            chat_area.insert(tk.END, f"Bot: {bot_msg}\n")
        chat_area.config(state='disabled')
        chat_area.see(tk.END)

    def refresh_bubbles_chat():
        for widget in bubbles_frame.winfo_children():
            widget.destroy()
        for user, bot_msg in bot.history:
            user_bubble = tk.Label(
                bubbles_frame, text=user, bg="#4A90E2", fg="#fff", anchor="w",
                font=("Segoe UI", 10, "bold"), padx=10, pady=5, wraplength=600, justify="left"
            )
            user_bubble.pack(anchor="w", pady=2, padx=5, fill="x")
            bot_bubble = tk.Label(
                bubbles_frame, text=bot_msg, bg="#444", fg="#fff", anchor="w",
                font=("Consolas", 10), padx=10, pady=5, wraplength=600, justify="left"
            )
            bot_bubble.pack(anchor="w", pady=(0, 8), padx=30, fill="x")
        bubbles_frame.update_idletasks()
        # Dummy yview for compatibility
        bubbles_frame.yview = lambda *a, **k: None

    def add_to_classic_chat(sender, message):
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f"{sender}: {message}\n")
        chat_area.config(state='disabled')
        chat_area.see(tk.END)

    def add_to_bubbles(sender, message):
        if sender == "User":
            user_bubble = tk.Label(
                bubbles_frame, text=message, bg="#4A90E2", fg="#fff", anchor="w",
                font=("Segoe UI", 10, "bold"), padx=10, pady=5, wraplength=600, justify="left"
            )
            user_bubble.pack(anchor="w", pady=2, padx=5, fill="x")
        else:
            bot_bubble = tk.Label(
                bubbles_frame, text=message, bg="#444", fg="#fff", anchor="w",
                font=("Consolas", 10), padx=10, pady=5, wraplength=600, justify="left"
            )
            bot_bubble.pack(anchor="w", pady=(0, 8), padx=30, fill="x")
        bubbles_frame.update_idletasks()

    def send_question():
        user_question = user_input.get()
        if not user_question.strip():
            return
        user_input.delete(0, tk.END)
        
        # Show user message and typing indicator
        if show_classic_mode:
            add_to_bubbles("User", user_question)
            add_to_bubbles("Bot", "🤖 Thinking...")
            root.update()
        else:
            add_to_classic_chat("User", user_question)
            add_to_classic_chat("Bot", "🤖 Thinking...")
            root.update()
        
        # Process the question in a separate thread to avoid blocking GUI
        def process_question():
            try:
                answer = bot.ask(user_question)
                
                # Update GUI in main thread
                root.after(0, lambda: update_chat_with_answer(answer))
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                root.after(0, lambda: update_chat_with_answer(error_msg))
        
        thread = threading.Thread(target=process_question, daemon=True)
        thread.start()
    
    def update_chat_with_answer(answer):
        if show_classic_mode:
            # Remove the "Thinking..." bubble (last widget)
            children = bubbles_frame.winfo_children()
            if children and children[-1].cget("text") == "🤖 Thinking...":
                children[-1].destroy()
            add_to_bubbles("Bot", answer)
            refresh_bubbles_chat()
        else:
            # Remove the "Thinking..." line (last line)
            chat_area.config(state='normal')
            lines = chat_area.get("1.0", tk.END).splitlines()
            if lines and lines[-1].strip() == "Bot: 🤖 Thinking...":
                chat_area.delete(f"{len(lines)}.0", tk.END)
            chat_area.config(state='disabled')
            add_to_classic_chat("Bot", answer)
        save_code_if_present(answer)

    def clear_chat():
        bot.history.clear()
        bot.save_history()
        if show_classic_mode:
            for widget in bubbles_frame.winfo_children():
                widget.destroy()
            add_to_bubbles("Bot", "✅ Chat cleared")
        else:
            chat_area.config(state='normal')
            chat_area.delete(1.0, tk.END)
            chat_area.config(state='disabled')
            add_to_classic_chat("Bot", "✅ Chat cleared")

    def copy_last_bot_answer():
        if not _pyperclip_available:
            messagebox.showerror("Error", "pyperclip module is not installed.")
            return
        if show_classic_mode:
            # Find last bot bubble
            children = bubbles_frame.winfo_children()
            for widget in reversed(children):
                if isinstance(widget, tk.Label) and widget.cget("bg") == "#444":
                    text = widget.cget("text")
                    pyperclip.copy(text)
                    messagebox.showinfo("Copied", "Last bot answer copied to clipboard!")
                    return
        else:
            # Find last "Bot: ..." line
            lines = chat_area.get(1.0, tk.END).strip().split('\n')
            for line in reversed(lines):
                if line.startswith("Bot:"):
                    text = line[len("Bot:"):].strip()
                    pyperclip.copy(text)
                    messagebox.showinfo("Copied", "Last bot answer copied to clipboard!")
                    return

    def save_code_if_present(answer):
        # Save code if answer looks like it contains code (simple heuristic)
        code_keywords = ["def ", "print(", "{", "}"]
        if any(keyword in answer.lower() for keyword in code_keywords):
            try:
                with open("code_sample.py", "w", encoding="utf-8") as f:
                    f.write(answer)
                print("⚙️ Example code saved to code_sample.py")
            except Exception as e:
                print("Error saving code:", e)

    def toggle_theme():
        nonlocal bg_color, text_color
        if root["bg"] == "#2E2E2E":
            bg_color = "#F2F2F2"
            text_color = "#000000"
            theme_button.config(text="🌙 Night Mode")
            chat_area.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
            user_input.config(bg="#FFFFFF", fg="#000000", insertbackground="#000000")
            bubbles_frame.config(bg=bg_color)
            for widget in bubbles_frame.winfo_children():
                if widget.cget("bg") == "#4A90E2":
                    widget.config(bg="#A3C8F2", fg="#000")
                elif widget.cget("bg") == "#444":
                    widget.config(bg="#E0E0E0", fg="#000")
        else:
            bg_color = "#2E2E2E"
            text_color = "#FFFFFF"
            theme_button.config(text="☀️ Day Mode")
            chat_area.config(bg="#1E1E1E", fg="#FFFFFF", insertbackground="#FFFFFF")
            user_input.config(bg="#333333", fg="#FFFFFF", insertbackground="#FFFFFF")
            bubbles_frame.config(bg=bg_color)
            for widget in bubbles_frame.winfo_children():
                if widget.cget("bg") == "#A3C8F2":
                    widget.config(bg="#4A90E2", fg="#fff")
                elif widget.cget("bg") == "#E0E0E0":
                    widget.config(bg="#444", fg="#fff")
        root.configure(bg=bg_color)
        tip_label.configure(bg=bg_color)
        status_label.configure(bg=bg_color)

    def toggle_chat_style():
        global show_classic_mode
        show_classic_mode = not show_classic_mode
        theme = "🧱 Bubble Mode" if show_classic_mode else "📋 Text Mode"
        chat_style_button.config(text=theme)
        if show_classic_mode:
            show_bubbles()
        else:
            show_classic()

    # Input area and buttons
    input_frame = tk.Frame(root, bg=bg_color)
    input_frame.pack(fill="x", padx=10, pady=(0, 10))

    user_input = tk.Entry(
        input_frame, font=("Consolas", 11),
        bg="#333333", fg="#FFFFFF", insertbackground="white"
    )
    user_input.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
    user_input.bind("<Return>", lambda e: send_question())

    send_button = tk.Button(input_frame, text="Send", command=send_question)
    send_button.pack(side=tk.LEFT, padx=5)

    clear_button = tk.Button(input_frame, text="Clear", command=clear_chat)
    clear_button.pack(side=tk.LEFT, padx=5)

    copy_button = tk.Button(input_frame, text="Copy Bot", command=copy_last_bot_answer)
    copy_button.pack(side=tk.LEFT, padx=5)

    theme_button = tk.Button(input_frame, text="☀️ Day Mode", command=toggle_theme)
    theme_button.pack(side=tk.LEFT, padx=5)

    chat_style_button = tk.Button(input_frame, text="📋 Text Mode", command=toggle_chat_style)
    chat_style_button.pack(side=tk.LEFT, padx=5)

    # AI functionality removed for instant responses

    # Welcome message
    if show_classic_mode:
        show_bubbles()
        add_to_bubbles("Bot", "Welcome! I'm a friendly code chatbot. Ask me any programming question 😃")
    else:
        show_classic()
        add_to_classic_chat("Bot", "Welcome! I'm a friendly code chatbot. Ask me any programming question 😃")

    print("Starting mainloop...")
    root.mainloop()
    print("GUI closed")

def main():
    run_gui()

if __name__ == "__main__":
    main()
