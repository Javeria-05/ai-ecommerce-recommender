# 🛍️ AI Ecommerce Recommendation System

An AI-powered ecommerce recommendation system that suggests relevant products based on user input using machine learning techniques. The application provides an interactive web interface and supports deployment, API testing, unit testing, and containerization.

---

## 📌 Overview

This project was developed to build and deploy a lightweight AI-based web application by extending an existing recommendation system and integrating Software Construction and Development concepts.

The system allows users to search for products and receive recommendation results through an interactive interface.

---

## ✨ Features

✔ Product recommendation system  
✔ Search by product title/category  
✔ Interactive web interface  
✔ Flask backend integration  
✔ HTML/CSS frontend  
✔ Streamlit interface support  
✔ REST API integration  
✔ API testing using Postman  
✔ Unit testing using unittest  
✔ Threading implementation  
✔ Docker container support  
✔ Hugging Face deployment  

---

## 🛠️ Tech Stack

### Languages
- Python

### Frameworks
- Flask
- Streamlit

### Libraries
- Pandas
- Scikit-Learn
- Joblib
- Threading
- Unittest

### Tools & Platforms
- GitHub
- Hugging Face
- Docker
- Trello
- Postman

---

## 📂 Project Structure

```bash
AI-Ecommerce-Recommendation-System/
│
├── hf_deployment/
│   ├── app.py
│   ├── data.pkl
│   ├── preprocessor.joblib
│   ├── kmeans_model.joblib
│   ├── requirements.txt
│   └── Dockerfile
│
├── flask_interface/
│   ├── app.py
│   ├── templates/
│   │     └── index.html
│   │
│   └── static/
│         └── style.css
│
├── testing.py
├── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository-name.git
```

Move into the project directory:

```bash
cd AI-Ecommerce-Recommendation-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run Flask application:

```bash
python app.py
```

Run Streamlit application:

```bash
streamlit run app.py
```

---

## 🧪 Unit Testing

Run test cases:

```bash
python testing.py
```

Implemented test cases:

- Valid product testing
- Invalid product testing
- Empty input testing

---

## 🔌 API Testing

API endpoint:

```bash
GET /api/recommend?product=shoes
```

Tested using Postman.

---

## 🐳 Docker Support

Build image:

```bash
docker build -t ecommerce-recommender .
```

Run container:

```bash
docker run -p 8501:8501 ecommerce-recommender
```

---

## 🚀 Deployment

- GitHub Repository ✅
- Hugging Face Spaces ✅
- Docker Support ✅

---

## 🔮 Future Enhancements

- Personalized recommendations
- Product images support
- Authentication system
- Real-time database integration
- Improved recommendation accuracy

---

## 🙏 Credits

Original Repository:

Repository: E-commerce Recommendation System  
Author: Shawon Barman  

GitHub Repository:  
https://github.com/ShawonBarman/E-commerce_recommendation_system

Additional modifications:

- Flask + HTML/CSS interface
- Streamlit integration
- Docker support
- API testing
- Unit testing
- Threading implementation
- UI enhancements

Modified and enhanced by:

**Javeria Irum and Abdul Basit Khan**

---

## 📄 License

This project is developed for educational and academic purposes.
