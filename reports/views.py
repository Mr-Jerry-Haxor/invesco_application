from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import ReportLog, ReportType, VisualizationType
import pandas as pd
import yfinance as yf
from django.contrib.auth.models import User


import matplotlib.pyplot as plt
from io import BytesIO
import base64

@login_required(login_url='login/')
def dashboard(request):
    if request.method == 'POST':
        report_type = ReportType.objects.get(id=request.POST['report_type'])
        date_range_start = request.POST['date_range_start']
        date_range_end = request.POST['date_range_end']
        visualization_type = VisualizationType.objects.get(id=request.POST['visualization_type'])

        # Download historical data
        data = yf.download('IVZ', start=date_range_start, end=date_range_end)

        # Check if the DataFrame is empty
        data_exists = not data.empty

        # Calculate the EMA, MACD, and Signal Line
        if data_exists:
            # Calculate the 12-day EMA
            data['12_EMA'] = data['Close'].ewm(span=12, adjust=False).mean()

            # Calculate the 26-day EMA
            data['26_EMA'] = data['Close'].ewm(span=26, adjust=False).mean()

            # Calculate the MACD
            data['MACD'] = data['12_EMA'] - data['26_EMA']

            # Calculate the Signal Line
            data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

        # Convert the DataFrame to JSON
        data_json = data.reset_index().to_json(orient='records')

        # Save a log in the database
        ReportLog.objects.create(
            user=request.user,
            report_type=report_type,
            date_range_start=date_range_start,
            date_range_end=date_range_end,
            visualization_type=visualization_type,
        )

        report_types = ReportType.objects.all()
        visualization_types = VisualizationType.objects.all()

        # Render the dashboard page with the report data
        return render(request, 'dashboard.html', {'data': data, 'data_exists': data_exists , 'report_types': report_types, 'visualization_types': visualization_types ,'data_json': data_json , 'visualization_type': visualization_type.name})

    else:
        report_types = ReportType.objects.all()
        visualization_types = VisualizationType.objects.all()
        return render(request, 'dashboard.html', {'report_types': report_types, 'visualization_types': visualization_types})