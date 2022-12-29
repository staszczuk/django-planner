from calendar import Calendar

from django.shortcuts import render

from .models import Event

# Create your views here.


def month(request, year, month):
    events = Event.objects.filter(date__year=year, date__month=month)
    calendar = Calendar()
    days = {}
    for date in calendar.itermonthdates(year, month):
        days.update({f'{date}': {
            'date': date,
            'events': [],
        }})
    for event in events:
        days.get(f'{event.date}').get('events').append(event)
    return render(request, 'planner/month.html', {
        'year': year,
        'month': month,
        'days': days,
    })


def day(request, year, month, day):
    events = Event.objects.filter(
        date__year=year, date__month=month, date__day=day)
    return render(request, 'planner/day.html', {
        'year': year,
        'month': month,
        'day': day,
        'events': events,
    })
