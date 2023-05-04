from django.shortcuts import render

from django.shortcuts import render

def home(request):
    context = {
        'welcome_text': 'Welcome to the home page of my project!',
        'intro_text': 'My name is Efimov Michael and I created my first Django project. I created this project to show my skills and experience in web development.',
        'body_text': 'Here you can find information about my project, my experience and skills, and contact me if you have any questions or suggestions. I hope you enjoy my project!',
    }
    return render(request, 'home.html', context)

def resume(request):
    context = {
        'phone_numbers': ['+38097-645-75-63', '+38097-645-75-63', '+38097-645-75-63', '+38097-645-75-63', '+38097-645-75-63'],
        'summary': 'Have experience with Python. In 2021, he received a diploma of complete secondary education in the specialty "Software Development". Passed courses to improve the level of English at the SpeakUp school.',
        'education': [
            'From 2017 to 2021 Kharkiv College of Computer Technologies with a degree in Software Engineer.',
            'Since 2021: Semyon Kuznets University for the specialty "Cybersecurity" of the Faculty of Information Technology.'
        ],
        'work_experience': 'None',
        'footer_text': '&copy; My Copyright'
    }
    return render(request, 'resume.html', context)
