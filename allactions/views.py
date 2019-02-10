from django.shortcuts import render
from .models import Stages, Questions, Sections, Grades


def send(request, section_id=1):
    stages = Stages.objects.filter(section_id=section_id)
    # print(Stages.objects.filter(section_id=Stages.objects.get(section_id).section_id))
    # print(Stages.objects.filter(section_id=Stages.objects.get(section_id)))
    questions = Questions.objects.all()
    sections = Sections.objects.all()
    grades = Grades.objects.all()
    context = {"sections": sections, "stages": stages, "questions": questions, "grades": grades}
    # print(request.method)
    # if request.method == "POST":
    #     print('KARTOSHECHKA')
    return render(request, 'main.html', context)
