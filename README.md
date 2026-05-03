# 🚀 AI Job Recommendation App

This project is a **Streamlit-based AI Job Recommendation system** that leverages LLMs and external APIs to provide intelligent job suggestions.

---

## 📌 Prerequisites

Before running the application locally, ensure you have the following installed:

* Python **3.13**
* A code editor (recommended: VS Code)
* `pip` (Python package manager)

---

## ⚙️ Setup Instructions

### 1. Clone or Download the Project

Copy all project files to your local machine.

---

### 2. Open the Project

Open the project folder in your preferred IDE (e.g., VS Code).

---

### 3. Create a Virtual Environment

```bash
python3.13 -m venv venv
```

Activate the virtual environment:

* **Windows**

```bash
venv\Scripts\activate
```

* **Mac/Linux**

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

All required package versions are already specified in `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

### 5. Configure API Keys

This project requires API keys for:

* **LLM Provider (Groq)**
* **Apify Platform**

#### 🔑 Get your API Keys:

* Groq: https://console.groq.com/keys
* Apify: https://docs.apify.com/api/v2

Add your keys in the appropriate configuration file or environment variables (as used in the project).

---

### 6. Run the Application

Navigate to the project root folder and run:

```bash
streamlit run app.py
```

---

## ✅ Application Access

Once the app starts, it will automatically open in your browser.

If not, visit:

```
http://localhost:8501
```

---

## 🧪 Usage

* Enter relevant inputs as required by the app
* Get AI-powered job recommendations instantly

---

## ⚠️ Notes

* Ensure your API keys are valid and active
* Free-tier limits may apply (especially for Apify and Groq)
* This is a POC project and may require enhancements for production deployment

---

## 📦 Quick Command Summary

```bash
python3.13 -m venv venv
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Future Improvements

* Add authentication
* Improve UI/UX
* Add caching for API responses
* Enhance recommendation accuracy

---

## 🤝 Contributing

Feel free to fork and improve this project.

---

## 📄 License

This project is for learning/demo purposes.