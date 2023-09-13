from django.shortcuts import render, redirect
from .models import CalendarEntry
from .forms import CalendarEntryForm

def calendar_view(request):
    if request.method == 'POST':
        form = CalendarEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')

    else:
        form = CalendarEntryForm()

    calendar_entries = CalendarEntry.objects.all()
    return render(request, 'calendar/calendar.html', {'form': form, 'calendar_entries': calendar_entries})
