import csv
import requests

from dagster import asset


@asset
def cereals():
    response = requests.get('https://docs.dagster.io/assets/cereal.csv')
    lines = response.text.split('\n')
    return [row for row in csv.DictReader(lines)]


@asset
def nabisco_cereals(cereals):
    return [row for row in cereals if row['mfr'] == 'N']


@asset
def cereal_protein_fractions(cereals):
    result = {}

    for cereal in cereals:
        total_grams = float(cereal['weight']) * 28.35
        result[cereal['name']] = float(cereal['protein']) / total_grams

    return result


@asset
def highest_protein_nabisco_cereal(nabisco_cereals, cereal_protein_fractions):
    sorted_by_protein = sorted(
        nabisco_cereals,
        key=lambda cereal: cereal_protein_fractions[cereal['name']],
    )
    return sorted_by_protein[-1]['name']
