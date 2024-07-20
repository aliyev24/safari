from django.shortcuts import render, redirect
from . import forms, run_function


def create_tour(request):
    if request.method == 'POST':
        form = forms.TourForm(request.POST)
        if form.is_valid():
            night_from = form.cleaned_data['night_from']
            night_till = form.cleaned_data['night_till']
            adult = form.cleaned_data['adult']
            child = form.cleaned_data['child']
            results = run_function.run(day_of_month=21,
                                       month=7,
                                       nights=6,
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
