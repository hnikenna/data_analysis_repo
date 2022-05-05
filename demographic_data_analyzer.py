import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = df['race']
    elements = {}
    for i in race:
        if i not in elements:
            elements.update({i: len(race[race.eq(i)])})

    race_count = pd.Series(elements)

    # What is the average age of men?
    men_data = df[df['sex'] == 'Male']
    men_age = men_data['age']
    average_age_men = men_age.mean()
    average_age_men = f'{average_age_men:.1f}'
    average_age_men = float(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_data = df[df['education'] == 'Bachelors']
    bachelors_quantity = len(bachelors_data)
    total_quantity = len(df)
    percentage_bachelors = (bachelors_quantity / total_quantity) * 100
    percentage_bachelors = f'{percentage_bachelors:.1f}'
    percentage_bachelors = float(percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    degrees = ['Bachelors', 'Masters', 'Doctorate']
    educated_data = df[df['education'].isin(degrees)]
    non_educated_data = df[~df['education'].isin(degrees)]
    educated_quantity = len(educated_data)
    higher_education = (educated_quantity / total_quantity) * 100
    lower_education = 100 - higher_education

    # percentage with salary >50K
    educated_rich_data = educated_data[educated_data['salary'].eq('>50K')]
    educated_rich_quantity = len(educated_rich_data)
    non_educated_rich_data = non_educated_data[non_educated_data['salary'].eq('>50K')]
    non_educated_rich_quantity = len(non_educated_rich_data)
    higher_education_rich = (educated_rich_quantity / len(educated_data)) * 100
    higher_education_rich = f'{higher_education_rich:.1f}'
    higher_education_rich = float(higher_education_rich)
    lower_education_rich = (non_educated_rich_quantity / len(non_educated_data)) * 100
    lower_education_rich = f'{lower_education_rich:.1f}'
    lower_education_rich = float(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    work_hours_data = df['hours-per-week']
    min_work_hours = work_hours_data.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hours_data = df[df['hours-per-week'].eq(min_work_hours)]
    num_min_workers = len(min_hours_data)
    rich_min_hours_data = min_hours_data[min_hours_data['salary'].eq('>50K')]
    rich_min_hours_quantity = len(rich_min_hours_data)
    rich_percentage = (rich_min_hours_quantity / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    rich_data = df[df['salary'].eq('>50K')]
    rich_country_data = rich_data['native-country']
    elements2 = {}
    for i in rich_country_data:
        if i not in elements2:
            percentage_rich = (len(rich_country_data[rich_country_data.eq(i)]) / len(df[df['native-country'].eq(i)]) * 100)
            elements2.update({percentage_rich: i})
    max_length = max(elements2.keys())
    highest_earning_country = elements2.get(max_length)
    highest_earning_country_percentage = max_length
    highest_earning_country_percentage = f'{highest_earning_country_percentage:.1f}'
    highest_earning_country_percentage = float(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich_country_data = rich_data[rich_data['native-country'].eq('India')]
    india_rich_country_occupation_data = india_rich_country_data['occupation']
    elements3 = {}
    for i in india_rich_country_occupation_data:
        if i not in elements3:
            elements3.update({len(india_rich_country_occupation_data[india_rich_country_occupation_data.eq(i)]): i})
    india_max_length = max(elements3.keys())
    top_IN_occupation = elements3.get(india_max_length)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data(True)
