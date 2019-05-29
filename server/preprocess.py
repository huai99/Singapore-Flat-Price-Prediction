import pandas as pd
import numpy as np
from scipy.special import boxcox1p
from random import seed
from random import randint

north_east = "NORTH_EAST"
east = "EAST"
west = "WEST"
north = "NORTH"
central = "CENTRAL"
unknow = "UNKNOWN"

town_to_geographical_region  = {
    "ANG MO KIO" : north_east,
    "BEDOK" : east,
    "BISHAN" : central,
    "BUKIT BATOK" : west,
    "BUKIT MERAH" : central,
    "BUKIT PANJANG" : west,
    "BUKIT TIMAH" : central,
    "CENTRAL AREA" : central,
    "CHOA CHU KANG" : west,
    "CLEMENTI" : west,
    "GEYLANG" : central,
    "HOUGANG" : north_east,
    "JURONG EAST" : west,
    "JURONG WEST" : west,
    "KALLANG/WHAMPOA" : central,
    "MARINE PARADE" : central,
    "PASIR RIS" : east,
    "PUNGGOL" : north_east,
    "QUEENSTOWN" : west,
    "SEMBAWANG" : north,
    "SENGKANG" : north_east,
    "SERANGOON" : north_east,
    "TAMPINES" : east,
    "TOA PAYOH" : central,
    "WOODLANDS" : north,
    "YISHUN" : north
}

base_df = pd.read_pickle('x_all_base.pkl')

def create_feature(input_df):
    all_df = input_df.copy() 
    all_df['room_number'] = all_df['flat_type'].map({
        '2 ROOM': 2,
        '3 ROOM': 3,
        '4 ROOM': 4,
        '5 ROOM': 5,
        'EXECUTIVE': 3,
        'MULTI-GENERATION': 4,
        '1 ROOM': 1
    })
   
    all_df['toilet_number'] = all_df['flat_type'].map({
        '1 ROOM': 1,
        '2 ROOM': 1,
        '3 ROOM': 2,
        '4 ROOM': 2,
        '5 ROOM': 2,
        'EXECUTIVE': 2,
        'MULTI-GENERATION': 3
    }) 
    all_df['direction'] = all_df['town'].apply(lambda x : town_to_geographical_region[x]) 
    all_df['sale_year'] = all_df['month'].apply(lambda x: x.split("-")[0]).astype('int')
    all_df['sale_month'] = all_df['month'].apply(lambda x: x.split("-")[1]).astype('int')
    return all_df

def delete_unused_feature(input_df):
    all_df = input_df.copy()
    all_df.drop(['block'],axis=1,inplace=True)
    all_df.drop(['month'],axis=1,inplace=True) 
    return all_df


def remove_skewness(input_df):
    all_df = input_df.copy()
    all_df['storey_random'] = boxcox1p(all_df['storey_random'],0.15)
    return all_df


def conform_test_to_train_format(test_df,train_df):
    new_df = test_df.copy() 
    dum_new_df = pd.get_dummies(new_df)
    dummies_frame = pd.get_dummies(train_df)
    dum_new_df = dum_new_df.reindex(columns=dummies_frame.columns,fill_value=0)
    return dum_new_df

def preprocess(payload):
    df_test = pd.DataFrame.from_dict(payload)
    df_test = remove_skewness(delete_unused_feature(create_feature(df_test)))
    df_test = conform_test_to_train_format(df_test,base_df)
    return df_test
