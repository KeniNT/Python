import os
import json
from collections import defaultdict

def read_json_files(directory):
    """
    Recursively read all JSON files in the specified directory and its subdirectories.
    """
    covid_data = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    covid_data.append(data)
    return covid_data

def calculate_statistics(covid_data):
    """
    Calculate total confirmed cases, deaths, recovered cases, and active cases for each country.
    """
    country_stats = defaultdict(lambda: {"total_confirmed": 0, "total_deaths": 0, "total_recovered": 0})
    
    for entry in covid_data:
        country = entry['country']
        country_stats[country]['total_confirmed'] += entry['confirmed_cases']['total']
        country_stats[country]['total_deaths'] += entry['deaths']['total']
        country_stats[country]['total_recovered'] += entry['recovered']['total']
        
    for country, stats in country_stats.items():
        stats['total_active'] = stats['total_confirmed'] - (stats['total_deaths'] + stats['total_recovered'])
    
    return country_stats

def find_top_countries(country_stats, top_n=5):
    """
    Find the top N countries with the highest and lowest number of confirmed cases.
    """
    sorted_countries = sorted(country_stats.items(), key=lambda x: x[1]['total_confirmed'], reverse=True)
    top_countries_highest = sorted_countries[:top_n]
    top_countries_lowest = sorted_countries[-top_n:]
    
    return top_countries_highest, top_countries_lowest

def generate_summary(country_stats, top_countries_highest, top_countries_lowest):

    summary = {
        "COVID-19 Statistics by Country": [],
        "Top 5 Countries with Highest Confirmed Cases": [],
        "Top 5 Countries with Lowest Confirmed Cases": []
    }

    for country, stats in country_stats.items():
        summary["COVID-19 Statistics by Country"].append(
            f"{country}: Confirmed: {stats['total_confirmed']}, Deaths: {stats['total_deaths']}, "
            f"Recovered: {stats['total_recovered']}, Active: {stats['total_active']}"
        )

    for country, stats in top_countries_highest:
        summary["Top 5 Countries with Highest Confirmed Cases"].append(f"{country}: {stats['total_confirmed']}")

    for country, stats in top_countries_lowest:
        summary["Top 5 Countries with Lowest Confirmed Cases"].append(f"{country}: {stats['total_confirmed']}")

    return summary

def save_summary_to_json(summary_data, output_file):
    """
    Save the summary report to a JSON file.
    """
    with open(output_file, 'w') as json_file:
        json.dump(summary_data, json_file, indent=4)

def main(directory, output_directory):

    covid_data = read_json_files(directory)

    country_stats = calculate_statistics(covid_data)

    top_countries_highest, top_countries_lowest = find_top_countries(country_stats)

    summary_data = generate_summary(country_stats, top_countries_highest, top_countries_lowest)

    output_file = os.path.join(output_directory, "covid19_summary.json")
    save_summary_to_json(summary_data, output_file)
    
    print(f"\nSummary report saved to {output_file}")

if __name__ == "__main__":
    
    main('C:/sem5/Adv_Python_Lab', 'C:/sem5/Adv_Python_Lab')


