from django.shortcuts import render, redirect
from . import forms, run_function


def create_tour(request):
    if request.method == 'POST':
        form = forms.TourForm(request.POST)
        if form.is_valid():
            night_from = form.cleaned_data['night_from']
            night_till = form.cleaned_data['night_till']
            difference = (night_till - night_from).days
            adult = form.cleaned_data['adult']
            child = form.cleaned_data['child']
            result = run_function.run(day_of_month=21,
                                      month=7,
                                      nights=6,
                                      adult=adult,
                                      child=child,
                                      )
        print(result)
        print('Results should be printed')
        return redirect('home')

    else:
        form = forms.TourForm()
    return render(request, 'core/index.html', {'form': form})
