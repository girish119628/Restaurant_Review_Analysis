# Restaurant_Review_Analysis

This project analyzes restaurant ratings and customer reviews to uncover key factors influencing **customer satisfaction** and **restaurant success**.  
It includes end-to-end data cleaning, sentiment analysis, statistical testing, and visualization, powered by Python, MySQL, and Power BI.

---

## Problem Statement

**Objective:**  
To analyze customer reviews and ratings to:
- Determine what drives customer satisfaction.
- Explore temporal patterns and user engagement metrics.
- Perform sentiment analysis using NLP.
- Identify statistically significant patterns using ANOVA.
- Build dynamic Power BI dashboards using real-time data from MySQL.

---

## 🧰 Tech Stack & Tools

- **Python** – Data cleaning, NLP, statistical analysis
- **MySQL** – Data storage using Python-MySQL connector
- **Power BI** – Dashboard connected directly to MySQL (no manual file import)
- **Excel** – Initial data exploration and profiling
- **Libraries Used:** Pandas, Numpy, NLTK/TextBlob/VADER, Matplotlib/Seaborn, Scikit-learn, Scipy/Statsmodels

---

## 📈 Project Workflow

### 1. **Data Understanding & Exploration**
- Inspected raw dataset: restaurant names, user reviews, followers, ratings, date-time, etc.
- Performed exploratory data analysis (EDA) in **Excel**.

### 2. **Data Cleaning in Python**
- Removed null values and handled incorrect data types.
- Standardized date formats and text fields.
- Saved cleaned data directly to a **MySQL Server** using Python's connector module.

### 3. **Sentiment Analysis (NLP)**
- Applied **TextBlob/VADER** to classify reviews into **Positive**, **Neutral**, and **Negative** sentiments.
- Created sentiment scores to analyze customer emotions.

### 4. **Statistical Analysis**
- Performed **ANOVA** to test whether customer ratings significantly differ based on various features (like review length, sentiment, or time periods).

### 5. **Power BI Dashboard**
- Connected **Power BI directly to MySQL server** (no need for importing CSV/Excel).
- Built dynamic visuals for:
  - Ratings vs Time
  - Sentiment distribution
  - User engagement (followers, number of reviews)
  - Comparative trends and key insights

---

## 🎥 Project Explanation Video
*(Coming Soon)* – A video walkthrough is being created to explain each project step and insights derived from the dashboard.

---

## 💡 Key Insights

- Sentiment polarity had a strong correlation with ratings.
- Review volume and follower count positively impact restaurant visibility.
- Significant variation found in rating patterns across time slots and user segments.

---

## 📂 Folder Structure

```bash
📁 restaurant-review-analysis/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📊 Dashboard.pbix (optional)
├── 📁 data_cleaning/
│   └── data_cleaning_script.py
├── 📁 sentiment_analysis/
│   └── nlp_sentiment_model.py
├── 📁 mysql_connector/
│   └── upload_cleaned_data.py
└── 📁 visuals/
    └── screenshots/
