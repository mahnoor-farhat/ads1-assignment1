# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:48:44 2023

@author: Mahnoor Farhat
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_5995100.csv", skiprows=4)

def line_plot(df):
    """
    This function reads the data from the csv file and plots a line graph.


    Parameters
    ----------
    df : DataFrame used for visualization.

    """
    country_data = df[df['Country Name'] == 'Africa Eastern and Southern']
    years = country_data.columns[4:]
    values = country_data.iloc[:, 4:]

    country_data2 = df[df['Country Name'] == 'Africa Western and Central']
    years2 = country_data2.columns[4:]
    values2 = country_data2.iloc[:, 4:]

    country_data3 = df[df['Country Name'] == 'Central African Republic']
    years3 = country_data3.columns[4:]
    values3 = country_data3.iloc[:, 4:]

    country_data4 = df[df['Country Name'] == 'East Asia & Pacific']
    years4 = country_data4.columns[4:]
    values4 = country_data4.iloc[:, 4:]

    country_data5 = df[df['Country Name'] == 'Europe & Central Asia']
    years5 = country_data5.columns[4:]
    values5 = country_data5.iloc[:, 4:]

    plt.figure(figsize=(12, 6))
    plt.plot(years, values.values.ravel(),
             label='Access to electricity (%) for Africa Eastern and Southern')
    plt.plot(years2, values2.values.ravel(),
             label='Access to electricity (%) for Africa Western and Central')
    plt.plot(years3, values3.values.ravel(), label='Central African Republic')
    plt.plot(years4, values4.values.ravel(), label='East Asia & Pacific')
    plt.plot(years5, values5.values.ravel(), label='Europe & Central Asia')

    plt.xlabel('Year')
    plt.ylabel('Access to electricity (%)')
    plt.title(
        'Access to Electricity Over Time in Different Parts of Continents (Line Plot)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.show()
    return


def scat_plot(df):
    """
    This function reads the data from the csv file and plots a scatter graph.


    Parameters
    ----------
    df : DataFrame used for visualization.

    """
    country_data = df[df['Country Name'] == 'Pakistan']
    years = country_data.columns[4:]
    values = country_data.iloc[:, 4:]

    country_data2 = df[df['Country Name'] == 'India']
    years2 = country_data2.columns[4:]
    values2 = country_data2.iloc[:, 4:]

    plt.figure(figsize=(12, 6))
    plt.scatter(years, values.values.ravel(),
                label='Access to electricity (%)', s=50, c='green', marker='o')
    plt.scatter(years2, values2.values.ravel(),
                label='Access to electricity (%)', s=50, c='orange', marker='o')

    plt.xlabel('Year')
    plt.ylabel('Access to electricity (%)')
    plt.title(
        'Access to Electricity Over Time for The Indian Subcontinent (Scatter Plot)')
    plt.legend(["Pakistan", "India"])
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.show()
    return


def bar_plot(df):
    """
    This function reads the data from the csv file and plots a bar graph.


    Parameters
    ----------
    df : DataFrame used for visualization.

    """
    year_data = df[df['2020'].notna()]
    sorted_data = year_data.sort_values(by='2020', ascending=False)
    top_n = 10
    top_countries = sorted_data.head(top_n)

    plt.figure(figsize=(12, 6))

    plt.bar(top_countries['Country Name'],
            top_countries['2020'], color='green')

    plt.xlabel('Country')
    plt.ylabel('Access to electricity (%) in 2020')
    plt.title(
        'Top 10 Countries with Highest Access to Electricity in 2020 (Bar Graph)')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
    return


line_plot(df)
scat_plot(df)
bar_plot(df)
