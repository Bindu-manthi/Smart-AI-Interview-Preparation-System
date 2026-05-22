from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import random
from textblob import TextBlob


# Question Lists

python_questions = [

    "What is Python?",
    "What is OOPs?",
    "What is inheritance?",
    "What is polymorphism?",
    "What is encapsulation?",
    "Difference between list and tuple?",
    "What is a dictionary?",
    "Explain recursion?",
    "What is a function?",
    "What are decorators?",
    "What is lambda function?",
    "Difference between set and list?",
    "What is exception handling?",
    "Explain try and except?",
    "What is Django?",
    "What is Flask?",
    "What are modules in Python?",
    "What is NumPy?",
    "What is Pandas?",
    "What is machine learning?"
]
data_questions = [

    "What is SQL?",
    "What is Power BI?",
    "What is Excel?",
    "What is data cleaning?",
    "Difference between WHERE and HAVING?",
    "What is GROUP BY?",
    "What is a primary key?",
    "What is a foreign key?",
    "What is normalization?",
    "Explain joins in SQL?",
    "What is data visualization?",
    "What is ETL?",
    "What is a dashboard?",
    "What is KPI?",
    "Difference between COUNT and COUNT DISTINCT?",
    "What is data analysis?",
    "What is Python used for in data analysis?",
    "What is Pandas?",
    "What is NumPy?",
    "What is machine learning?"
]
java_questions = [
    "What is JVM?",
    "Explain OOPs concepts in Java?",
    "Difference between JDK and JRE?"
]

web_questions = [
    "What is HTML?",
    "Difference between HTML and CSS?",
    "What is JavaScript?"
]

fullstack_questions = [
    "What is frontend and backend?",
    "Explain REST API?",
    "What is Django?"
]

ai_questions = [
    "What is Machine Learning?",
    "Difference between AI and ML?",
    "What is NLP?"
]


# Home Page

def home(request):

    question = None
    answer = ""
    score = None
    feedback = None

    good_feedback = [

        "Excellent Answer",
        "Good Job",
        "Well Explained",
        "Strong Technical Answer"
    ]

    bad_feedback = [

        "Poor Answer",
        "Need Improvement",
        "Answer Too Short",
        "Try Explaining More Clearly"
    ]

    if request.method == "POST":

        role = request.POST.get('role')

        # Start Interview

        if 'start' in request.POST:

            if role == "python":

                question = random.choice(python_questions)

            elif role == "data":

                question = random.choice(data_questions)

            elif role == "java":

                question = random.choice(java_questions)

            elif role == "web":

                question = random.choice(web_questions)

            elif role == "fullstack":

                question = random.choice(fullstack_questions)

            elif role == "ai":

                question = random.choice(ai_questions)

        # Submit Answer

        if 'submit_answer' in request.POST:

            question = request.POST.get('current_question')

            answer = request.POST.get('answer')
            


            # Random Score & Feedback

            if len(answer) > 20:

                score = random.randint(7, 10)

                feedback = random.choice(good_feedback)

            else:

                score = random.randint(3, 5)

                feedback = random.choice(bad_feedback)

    context = {

        'question': question,
        'answer': answer,
        'score': score,
        'feedback': feedback,
    }

    return render(request,
                  'home.html',
                  context)


# Register Page

def register(request):

    form = UserCreationForm()

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')

    return render(request,
                  'register.html',
                  {'form': form})