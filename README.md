# 🧾 Django Student Form App

A simple Django web application demonstrating how to create and process forms using Django’s built-in `forms.Form` class.  
This project includes validation, radio buttons, checkboxes, password confirmation, and textarea widgets — all rendered dynamically in an HTML template.

---

## 🚀 Features

- Collects student details like:
  - Name, Age, Email
  - Gender (Radio buttons)
  - Courses (Checkboxes)
  - Password and Re-enter Password fields
  - Address (Textarea)
- Server-side form validation using Django’s `is_valid()` and `cleaned_data`
- Beautiful gradient background styling using inline CSS
- Simple, minimal UI built with Django templates

---

## 🛠️ Tech Stack

- **Python** 3.x  
- **Django** 4.x or higher  
- **HTML5 / CSS3** (for templates)

---

## 📂 Project Structure

student_form_project/
│
├── app/
│ ├── forms.py
│ ├── views.py
│ ├── templates/
│ │ └── student_Dj_form.html
│ └── init.py
│
├── student_form_project/
│ ├── settings.py
│ ├── urls.py
│ └── init.py
│
├── manage.py
└── README.md

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/django-student-form-app.git
cd django-student-form-app
2️⃣ Create and activate virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate    # For Windows
# or
source venv/bin/activate # For Linux/Mac
3️⃣ Install dependencies
bash
Copy code
pip install django
4️⃣ Run migrations
bash
Copy code
python manage.py migrate
5️⃣ Start the development server
bash
Copy code
python manage.py runserver
6️⃣ Open in browser
arduino
Copy code
http://127.0.0.1:8000/student_Dj_form/
🧠 Example Output
When submitted successfully, the form displays all the cleaned data, for example:

bash
Copy code
{'stdname': 'John', 'stdage': 22, 'stdemail': 'john@example.com', 'gender': 'male', 'courses': ['python', 'django'], 'password': '1234', 'rpassword': '1234', 'address': 'Bangalore'}
🧑‍💻 Author
Your Name
📧 your-email@example.com
💻 GitHub Profile

🪪 License
This project is licensed under the MIT License.

