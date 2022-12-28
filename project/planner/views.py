from django.shortcuts import render

# Create your views here.


def month(request, year, month):
    return render(request, 'planner/month.html', {
        'year': year,
        'month': month,
    })
