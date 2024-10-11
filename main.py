import pandas as pd
import numpy as np
# Load the Nobel Prize data from a CSV file
nobel = pd.read_csv('nobel.csv')
# 1. Identify the most commonly awarded gender and birth country
# Get the most common gender in the 'sex' column
top_gender = nobel['sex'].value_counts().index[0]
print("Most commonly awarded gender : ",top_gender)
# Get the most common birth country in the 'birth_country' column
top_country = nobel['birth_country'].value_counts().index[0]
print("Most commonly awarded birth country : ",top_country)
# 2. Find the decade with the highest ratio of US-born Nobel Prize winners to total winners
# Create a new column to indicate whether the winner was born in the USA
nobel['usa_born_winners'] = nobel['birth_country'] == 'United States of America'
# Create a new column for the decade by dividing the year by 10 and flooring it
nobel['decade'] = np.floor(nobel['year'] / 10)
# Multiply by 10 and convert to an integer to represent the decade correctly (e.g., 1970, 1980)
nobel['decade'] = (nobel['decade'] * 10).astype(int)
# Group by decade and calculate the proportion of USA-born winners for each decade
prop = nobel.groupby('decade', as_index=False)['usa_born_winners'].mean()
# Find the decade with the highest proportion of USA-born winners
max_decade_usa = prop[prop['usa_born_winners'] == prop['usa_born_winners'].max()]['decade']
max_decade_usa = int(max_decade_usa.iloc[0])
print("Decade with the highest ratio of US-born Nobel Prize winners to total winners : ", max_decade_usa)
# 3. Find the decade and category with the highest proportion of female laureates
# Create a new column to indicate if the winner was female
nobel['female_winner'] = nobel['sex'] == 'Female'
# Group by both decade and category and calculate the proportion of female winners
female_prop = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
# Find the combination of decade and category with the highest proportion of female winners
max_female_win = female_prop[female_prop['female_winner'] == female_prop['female_winner'].max()]
# Create a dictionary where the key is the decade and the value is the category
max_female_dict = {(max_female_win['decade'].values[0]): (max_female_win['category'].values[0])}
print("Find the decade and category with the highest proportion of female laureates : ",max_female_dict)
# 4. Identify the first woman to receive a Nobel Prize and her category
# Filter the dataset to include only female winners
females = nobel[nobel['female_winner'] == True]
# Find the earliest year in which a female won a Nobel Prize
first_woman = females[females['year'] == females['year'].min()]
# Extract the name of the first female Nobel Prize winner
first_woman_name = first_woman['full_name'].values[0]
print("First woman to receive a Nobel Prize : ",first_woman_name)
# Extract the category of the first female Nobel Prize winner
first_woman_category = first_woman['category'].values[0]
print("first woman to receive a Nobel Prize category : ",first_woman_category)
# 5. Identify individuals or organizations that have won more than one Nobel Prize
# Count the number of occurrences of each full name in the dataset
winner_count = nobel['full_name'].value_counts()
# Filter to include only those who have won more than once
winner_count = winner_count[winner_count >= 2].index
# Convert the list of repeat winners to a Python list
repeat_list = list(winner_count)
print("Individuals or organizations that have won more than one Nobel Prize : ",repeat_list)
