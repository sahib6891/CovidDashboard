from django.shortcuts import render
from django.shortcuts import HttpResponse
import pandas as pd 

# Create your views here.
def index(request):

    confirmedGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    totalCount = confirmedGlobal[confirmedGlobal.columns[-1]].sum()
    barPlotData = confirmedGlobal[['Country/Region', confirmedGlobal.columns[-1]]].groupby('Country/Region').sum()
    barPlotData = barPlotData.reset_index()
    barPlotData.columns = ['Country/Region', 'values']
    barPlotData = barPlotData.sort_values(by='values', ascending=False)
    barPlotVals = barPlotData['values'].values.tolist()
    countryNames = barPlotData['Country/Region'].values.tolist()
    context = {'totalCount': totalCount, 'countryNames': countryNames, 'barPlotVals': barPlotVals}
    return render(request, 'index.html', context=context)