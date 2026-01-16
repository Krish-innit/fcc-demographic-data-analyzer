import pandas as pd
col_names= [
    'age','workclass','fnlwgt','education','education-num','marital-status',
    'occupation','relationship','race','sex','capital-gain','capital-loss',
    'hours-per-week','native-country','salary'
]
adult = pd.read_csv('adult.data.csv', header=None, names=col_names)
adult.head()
def calculate_demographic_data(print_data = True):
    race_count = adult['race'].value_counts()
    adult['sex'] = adult['sex'].str.strip()
    men = adult[adult['sex'] == "Male"]
    average_age_men = round(men['age'].mean(), 1)
    adult['education']= adult['education'].str.strip()
    Bachelors= adult[adult['education'] == "Bachelors"]
    percentage_bachelors = round((len(Bachelors) / len(adult)) * 100, 1)
    AdvEdu = adult[(adult['education'] == "Bachelors") |
               (adult['education'] == "Doctorate")|
               (adult['education'] == "Masters")].copy()
    AdvEdu['salary'] = AdvEdu['salary'].str.strip()
    income = AdvEdu[AdvEdu['salary'] == ">50K"]
    high_education_rich = round((len(income) / len(AdvEdu))*100,1)
    OtherEdu = adult.drop(AdvEdu.index)
    OtherEdu['salary'] = OtherEdu['salary'].str.strip()
    Others_income = OtherEdu[OtherEdu['salary'] == ">50K"]
    Other_education_rich = round((len(Others_income) / len(OtherEdu))*100,1)
    min_working_hours = adult['hours-per-week'].min()
    Minhour = adult[adult['hours-per-week'] == min_working_hours].copy()
    Minhour['salary'] = Minhour['salary'].str.strip()
    MinhourIncome = Minhour[Minhour['salary'] == ">50K"]
    min_workhours_rich = (len(MinhourIncome) / len(Minhour))*100
    adult['salary'] = adult['salary'].str.strip()
    Each_country_rich = adult.value_counts('native-country')
    High_rich = adult[adult['salary'] == ">50K"].value_counts('native-country')
    Highest_Percentage = (High_rich / Each_country_rich)*100
    High_earn_country = Highest_Percentage.idxmax()
    High_earn_country_Percentage = round(Highest_Percentage.max(), 1)
    adult['native-country'] = adult['native-country'].str.strip()
    Indians = adult[adult['native-country'] == "India"]
    High_earning_indian = Indians[Indians['salary'] == ">50K"]
    Most_popular_occupation_IND = High_earning_indian.value_counts('occupation').idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': high_education_rich,
        'lower_education_rich': Other_education_rich,
        'min_work_hours': min_working_hours,
        'rich_percentage': min_workhours_rich,
        'highest_earning_country': High_earn_country,
        'highest_earning_country_Percentage': High_earn_country_Percentage,
        'top_IN_occupation': Most_popular_occupation_IND
    }
