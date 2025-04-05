import pandas as pd

# 
df = pd.read_csv("tackoverflow_qa.csv")
df['creationdate'] = pd.to_datetime(df['creationdate'])

# 
filters = {
    "before_2014": df[df['creationdate'] < '2014-01-01'],
    "score_gt_50": df[df['score'] > 50],
    "score_50_100": df[(df['score'] >= 50) & (df['score'] <= 100)],
    "answered_by_scott": df[df['ans_name'] == 'Scott Boston'],
    "answered_by_5_users": df[df['ans_name'].isin(['Scott Boston', 'Unutbu', 'Mike Pennington', 'Demitri', 'doug'])],
    "unutbu_mar_oct_2014_score_lt_5": df[
        (df['creationdate'] >= '2014-03-01') &
        (df['creationdate'] <= '2014-10-31') &
        (df['ans_name'] == 'Unutbu') &
        (df['score'] < 5)
    ],
    "score_5_10_or_views_gt_10000": df[
        ((df['score'] >= 5) & (df['score'] <= 10)) |
        (df['viewcount'] > 10000)
    ],
    "not_answered_by_scott": df[df['ans_name'] != 'Scott Boston']
}

# 
combined_results = []

for name, result in filters.items():
    temp = result.copy()
    temp['filter_name'] = name
    combined_results.append(temp)

all_results = pd.concat(combined_results, ignore_index=True)

#### titanic 


#
titanic_df = pd.read_csv("titanic.csv")

#
titanic_df['Cabin'] = titanic_df['Cabin'].astype(str)
titanic_df['Ticket'] = titanic_df['Ticket'].astype(str)

# 
homework_filters = {
    "female_class1_age_20_30": titanic_df[
        (titanic_df['Sex'] == 'female') & 
        (titanic_df['Pclass'] == 1) & 
        (titanic_df['Age'] >= 20) & 
        (titanic_df['Age'] <= 30)
    ],
    "fare_over_100": titanic_df[titanic_df['Fare'] > 100],
    "survived_and_alone": titanic_df[
        (titanic_df['Survived'] == 1) & 
        (titanic_df['SibSp'] == 0) & 
        (titanic_df['Parch'] == 0)
    ],
    "embarked_C_fare_over_50": titanic_df[
        (titanic_df['Embarked'] == 'C') & 
        (titanic_df['Fare'] > 50)
    ],
    "siblings_spouses_and_parents_children": titanic_df[
        (titanic_df['SibSp'] > 0) & 
        (titanic_df['Parch'] > 0)
    ],
    "age_15_or_younger_not_survived": titanic_df[
        (titanic_df['Age'] <= 15) & 
        (titanic_df['Survived'] == 0)
    ],
    "cabin_and_fare_over_200": titanic_df[
        (titanic_df['Cabin'] != 'nan') & 
        (titanic_df['Fare'] > 200)
    ],
    "odd_passenger_id": titanic_df[titanic_df['PassengerId'] % 2 == 1],
    "unique_ticket_numbers": titanic_df[
        titanic_df['Ticket'].map(titanic_df['Ticket'].value_counts()) == 1
    ],
    "miss_in_name_class1": titanic_df[
        (titanic_df['Name'].str.contains('Miss')) & 
        (titanic_df['Pclass'] == 1) & 
        (titanic_df['Sex'] == 'female')
    ]
}



