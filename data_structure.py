# Say we are trying to predict the hourly bike counts y at station s at time t. 
# The hourly bike count at station s1 at time t1 would be denoted y_s1_t1.
# Say there are two independent variables, x1 and x2.
# x1 and x2 at station s1 at time t1 would be denoted x1_s1_t1 and x2_s1_t1.

# We have data for x1, x2, and y at station s1 and at times t1, t2, t3, t4, t5, t6, and t7. 
# We are trying to predict the bike counts at station s1 at time t8, denoted y1_s1_t8
# Let us also use time_steps = 4 for the model.

# In order to structure the data to input into an LSTM model, 
# Data structure is [ samples, time_steps, n_features]
#                   [ 4 samples, 4 time steps, 2 features ]
X_train = 
[
    [
        [ x1_s1_t1, x2_s1_t1 ], [x1_s1_t2, x2_s1_t2], [x1_s1_t3, x2_s1_t3], [x1_s1_t4, x2_s1_t4]
    ]
    [
        [ x1_s1_t2, x2_s1_t2 ], [x1_s1_t3, x2_s1_t3], [x1_s1_t4, x2_s1_t4], [x1_s1_t5, x2_s1_t5],
    ]
    [
        [ x1_s1_t3, x2_s1_t3 ], [x1_s1_t4, x2_s1_t4], [x1_s1_t5, x2_s1_t5], [x1_s1_t6, x2_s1_t6],
    ]
    [
        [ x1_s1_t4, x2_s1_t4 ], [x1_s1_t5, x2_s1_t5], [x1_s1_t6, x2_s1_t6], [x1_s1_t7, x2_s1_t7],
    ]
]

# Data structure is [ samples, time_steps, n_features]
#                   [ 4 samples, 4 time steps, 2 features ]
y_train = 
[
    [ y1_s1_t1, y1_s1_t2, y1_s1_t3, y1_s1_t4 ],
    [ y1_s1_t2, y1_s1_t3, y1_s1_t4, y1_s1_t5 ],
    [ y1_s1_t3, y1_s1_t4, y1_s1_t5, y1_s1_t6 ],
    [ y1_s1_t4, y1_s1_t5, y1_s1_t6, y1_s1_t7 ]
]


# WHAT I DON'T UNDERSTAND:
# This is fine if we are trying to predict hourly demand at one station s1 (y1_s1_t8), 
# but how would the data be structured if we were trying to predict hourly demand for several stations (y1_s1_t8, y1_s2_t8, y1_s3_t8, etc.) ?