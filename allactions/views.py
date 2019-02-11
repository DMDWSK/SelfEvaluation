from django.shortcuts import render, redirect
from .models import Stages, Questions, Sections, Grades
from answers.models import UserAnswers



def enter(request):
    return render(request, "enter.html")


def send(request, section_id):
    i = 0
    stages = Stages.objects.filter(section_id=section_id)
    questions = Questions.objects.all()
    sections = Sections.objects.all()
    grades = Grades.objects.all()
    context = {"sections": sections, "stages": stages, "questions": questions, "grades": grades}
    if request.method == 'POST':
        print(request.POST)
        usr_grd = request.POST.getlist('select_box')
        for g in usr_grd:
            i += 1
            choice = request.POST.get('choice-{}'.format(i), 'No')
            answers = UserAnswers()
            if choice == 'yes':
                answers.answer = True
            else:
                answers.answer = False
            answers.grade = Grades.objects.get(grade=g)
            answers.question_id = i
            answers.user_id = request.user.id
            answers.save()
        if section_id == len(sections):
            return render(request,'finish.html')
        return redirect('/{}'.format(section_id+1))
    return render(request, 'main.html', context)

