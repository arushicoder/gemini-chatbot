# 🤖 Gemini Chatbot

A conversational AI chatbot built with **Google Gemini API** and **Streamlit**. This application provides an intuitive interface where users can interact with Google's Gemini model to ask questions, generate content, and receive AI-powered responses in real time.

## 🚀 Features

- 💬 Interactive chat interface
- 🤖 Powered by Google Gemini API
- ⚡ Fast and responsive Streamlit UI
- 🔒 Secure API key management using `.env`
- 📝 Conversation history during the session
- 🎨 Clean and user-friendly design

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv

## 📂 Project Structure

```
gemini-chatbot/
│── app.py
│── requirements.txt
│── .env               # Not included in GitHub
│── .gitignore
│── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Create a virtual environment (optional but recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project root and add:

```env
GEMINI_API_KEY=your_api_key_here
```

> **Note:** Never commit your `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

## 📸 Screenshot

_Add a screenshot of your chatbot here._

Example:

```
![Chatbot Screenshot](screenshot.png)
```

## 🔒 Security

This project uses environment variables to protect sensitive API keys.

Make sure `.env` is included in your `.gitignore` file.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, create a new branch, and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

## 👩‍💻 Author

**Arushi Mukherjee**

GitHub: https://github.com/arushicoder
