# 🎬 Movie Recommender System ✨

This project is a simple yet effective **movie recommendation system** built using **Natural Language Processing (NLP)** techniques.  
It suggests **5 similar movies** based on a user’s selection from a dropdown menu.  
The entire application is hosted online, making it easy for anyone to try out!

---

## 💡 How It Works (Tech Stack)

This system uses **content-based filtering**, where similarities between movies are calculated based on movie metadata like description, cast, genre, keywords, etc.

### 🧠 Technologies Used

| Category | Tools |
|---------|-------|
| Language | Python |
| Web Framework | Streamlit |
| Key Libraries | pandas, scikit-learn |
| Deployment | Render |

---

## ⚙️ NLP Pipeline Process

| Step | Description |
|-----|-------------|
| **Text Preprocessing** | Used PorterStemmer to stem text and clean data |
| **Vectorization** | CountVectorizer converts text → numerical vectors |
| **Similarity Metric** | Cosine Similarity used to calculate closeness between movies |
| **Recommendation Logic** | Returns top 5 movies with highest similarity score |

---

## 🚀 Live Demo

### 🌐 Website Link  
👉 **[Insert your Render Deployment Link Here]**

---

## 📝 How to Use

1. Open the app using the link above
2. Select a movie from the dropdown (e.g., **Avatar**, **Inception**, **The Dark Knight**)
3. Click **"Recommend"**
4. View your **top 5 similar movies** instantly!

---

## 📦 Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone <Your GitHub Repo URL>
cd <your-project-folder>
