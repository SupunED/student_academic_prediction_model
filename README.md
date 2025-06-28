# 🎓 Student Exam Score Predictor - ML + Flask Web App

This project is a **Machine Learning web application** that predicts students' **exam scores** based on various lifestyle, academic, and personal factors. The model is trained using a dataset containing student profiles and deployed via a **Flask** backend with a simple web interface.

---

## 🧠 Project Description

With increasing interest in understanding student performance, this project aims to predict a student’s **exam score** given 13 key features such as study habits, health, and socio-economic background. This can be useful for educators, counselors, or students themselves to identify areas of improvement.

---

## 🗃️ Dataset Overview

The dataset contains the following columns:

| Column | Description |
|--------|-------------|
| `student_id` | Unique identifier for each student |
| `age` | Age of the student |
| `gender` | Gender of the student |
| `study_hours_per_day` | Number of hours studied daily |
| `social_media_hours` | Daily time spent on social media |
| `netflix_hours` | Daily time spent watching Netflix |
| `part_time_job` | Whether the student has a part-time job (0 = No, 1 = Yes) |
| `attendance_percentage` | Attendance rate in percentage |
| `sleep_hours` | Average sleep duration per day |
| `diet_quality` | Quality of diet on a scale |
| `exercise_frequency` | Weekly exercise frequency |
| `parental_education_level` | Level of education of parents |
| `internet_quality` | Internet quality at home |
| `mental_health_rating` | Self-reported mental health score |
| `extracurricular_participation` | Participation in extracurriculars (0 = No, 1 = Yes) |
| `exam_score` | **Target** variable: Score obtained in exam |

---

## 🔍 Features Used for Prediction

The model uses the following 13 features to predict `exam_score`:

```python
features = [
    'age',
    'study_hours_per_day',
    'social_media_hours',
    'netflix_hours',
    'part_time_job',
    'attendance_percentage',
    'sleep_hours',
    'diet_quality',
    'exercise_frequency',
    'parental_education_level',
    'internet_quality',
    'mental_health_rating',
    'extracurricular_participation'
]
