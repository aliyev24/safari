from django.shortcuts import render, redirect
from . import forms, run_function


def create_tour(request):
    if request.method == 'POST':
        form = forms.TourForm(request.POST)
        if form.is_valid():
            flight_date = form.cleaned_data['from_date']  # Flight date.
            night_from = form.cleaned_data['night_from']
            night_till = form.cleaned_data['night_till']
            nights = (night_till-night_from).days
            adult = form.cleaned_data['adult']
            child = form.cleaned_data['child']
            results = run_function.run(
                                       flight_date=flight_date,
                                       nights=nights,
                                       adult=adult,
                                       child=child,
                                       )
        request.session['results'] = results
        return redirect('show_tours')

    else:
        form = forms.TourForm()
    return render(request, 'core/index.html', {'form': form})


# Showing tour results.
def show_tours(request):
    results = request.session['results']
    return render(request, 'core/secondary.html', {'results': results})
