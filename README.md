# 🎬 Movie Recommender System ✨

This project is a simple yet effective **movie recommendation system** built using **Natural Language Processing (NLP)** techniques.  
It suggests **5 similar movies** based on a user’s selection from a dropdown menu.  
The entire application is hosted online, making it easy for anyone to try out!

---

## 💡 How It Works (Tech Stack)

This system uses **content-based filtering**, where similarities between movies are calculated based on movie metadata like description, cast, genre, keywords, etc.

### 🧠 Technologies Used

* Language & Environment: Python

* Web Framework: Streamlit (for the simple, interactive web interface)

* Key Libraries: pandas, scikit-learn (for vectorization), requests (for API calls)

* External Service: The Movie Database (TMDB) API (for fetching high-quality movie posters)

* Deployment: Render (for hosting the web application)

---

## ✨ Feature Enhancements

Beyond the core NLP recommendation engine, I integrated a key feature to enhance the user experience:

Visual Appeal with Posters: Used the TMDB API to fetch the official poster image for each of the 5 recommended movies. This involved making API requests and dynamically displaying the images alongside the titles, making the results much more engaging!

---

## ⚙️ NLP Pipeline Process

1. **Text Preprocessing:** Used Stemming (specifically, the Porter Stemmer) to reduce words to their root form, standardizing the text data.

2. **Vectorization:** Employed CountVectorizer to transform the cleaned text data (the combined features for each movie) into a numerical feature vector.

3.  **Similarity Calculation:** Calculated the Cosine Similarity between the feature vector of the selected movie and all other movies to determine the 'closeness' or 'similarity' between them.

4. **Recommendation:** The system then retrieves and displays the top 5 movies with the highest similarity scores.

---

## 🚀 Live Demo

### 🌐 Website Link  
👉 **https://movie-recommender-system-1-auw1.onrender.com**

---

## 📝 How to Use

1. Open the app using the link above
2. Select a movie from the dropdown (e.g., **Avatar**, **Inception**, **The Dark Knight**)
3. Click **"Recommend"** button
4. View your **top 5 similar movies** instantly!

---

## 📦 Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone <Your GitHub Repo URL>
cd <your-project-folder>
```

### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
# .\venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app
```bash
streamlit run app.py
# (Assuming your main Streamlit file is named 'app.py')
```

(Your local web browser should automatically open the app!)

---

### 🙋‍♂️ Thoughts on the Project
I built this project to get hands-on experience with the complete cycle of a Data Science/NLP application: from data processing and algorithm selection to web development (using Streamlit, which was really fun and fast!) and finally, deployment on a cloud service like Render. It's a great example of how simple NLP techniques can power real-world applications!

---

## 🎥 Demo

### 🖼️ App Screenshot

<img width="926" height="602" alt="app_screenshot" src="https://github.com/user-attachments/assets/29806ffa-4c9f-4e69-b4af-96a4fcd201cc" />
##hii

