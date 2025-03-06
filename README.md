# Placement Prediction Web App 🎓📊  

This is a **Flask-based web application** that predicts whether a student will be placed or not based on their **CGPA** and **IQ** using a **Logistic Regression model** trained in Python.

---

## 📂 Project Structure
```
your_project/
│── app.py              # Flask backend
│── model.pkl           # Trained machine learning model
│── requirements.txt    # List of dependencies
│── templates/
│   ├── index.html      # Frontend UI
```

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies  
First, install **Python** (if not installed). Then, open a terminal in the project folder and run:
```bash
pip install -r requirements.txt
```
This installs Flask and other required packages.

---

### 2️⃣ Start the Flask Server  
Run the following command in the terminal:
```bash
python app.py
```
If successful, Flask will output:
```
 * Running on http://127.0.0.1:5000/
```

---

### 3️⃣ Open the Web App in Browser  
Go to **http://127.0.0.1:5000/** in your browser.

---

## 🖥️ Usage  
1. Enter a **CGPA** (e.g., `7.5`)  
2. Enter an **IQ Score** (e.g., `130`)  
3. Click the **Predict** button.  
4. The app will display whether the student is **Placed ✅** or **Not Placed ❌**  

---

## 🔧 Troubleshooting
- If `sklearn` is missing, install it manually:
  ```bash
  pip install scikit-learn
  ```
- If `index.html` is not found, ensure it's inside the `templates/` folder.

---

## 📜 License  
This project is **open-source** and free to use.  

---

## ✨ Contributing  
Feel free to **fork** this repository and contribute! 🚀

