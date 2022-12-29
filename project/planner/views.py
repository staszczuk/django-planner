from calendar import Calendar
from datetime import date

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

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


def add_event(request, year, month, day):
    event = Event(date=date(year, month, day), name=request.POST['eventName'])
    event.save()
    return HttpResponseRedirect(reverse('planner:day', args=(year, month, day)))


def delete_event(request, year, month, day):
    event = get_object_or_404(Event, date=date(
        year, month, day), name=request.POST['eventName'])
    event.delete()
    return HttpResponseRedirect(reverse('planner:day', args=(year, month, day)))
