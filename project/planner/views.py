from calendar import Calendar
from datetime import date

from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import Event
from . import utils

# Create your views here.


def month(request, year, month):
    events = Event.objects.filter(date__year=year, date__month=month)
    cal = Calendar()
    days = {}
    for date in cal.itermonthdates(year, month):
        days.update({f'{date}': {
            'date': date,
            'events': [],
        }})
    for event in events:
        days.get(f'{event.date}').get('events').append(event)
    prev = utils.prev_month(year, month)
    next = utils.next_month(year, month)
    return render(request, 'planner/month.html', {
        'year': year,
        'month': month,
        'days': days,
        'prev': prev,
        'next': next,
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
