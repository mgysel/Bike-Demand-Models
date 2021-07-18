# Say we are trying to predict the hourly bike counts y at stations s1, s2, and s3 at time t. 
# The hourly bike count at station s1 at time t1 would be denoted y_s1_t1.
# Say there are two independent variables, x1 and x2.
# x1 and x2 at station s1 at time t1 would be denoted x1_s1_t1 and x2_s1_t1.

# We have data for x1, x2, and y at stations s1, s2, and s3 and at times t1, t2, t3, and t4. 
# We are trying to predict the bike counts at station s1, s2, and s3 at time t4
# Let us also use time_steps = 4 for the model.


# Shape of the input feature (X_train): L×𝐻𝑖𝑛, 
#   L is the sequence length (time steps), L=4, 
#   𝐻𝑖𝑛 equals number of features times number of stations (2×number of stations)

X_train = 
[
    [ x1_s1_t1, x1_s2_t1, x2_s1_t1, x2_s2_t1, x1_s3_t1, x2_s3_t1 ], 
    [ x1_s1_t2, x1_s2_t2, x2_s1_t2, x2_s2_t2, x1_s3_t2, x2_s3_t2 ], 
    [ x1_s1_t3, x1_s2_t3, x2_s1_t3, x2_s2_t3, x1_s3_t3, x2_s3_t3 ], 
    [ x1_s1_t4, x1_s2_t4, x2_s1_t4, x2_s2_t4, x1_s3_t4, x2_s3_t4 ], 
]

y_train = 
[
    [ y_s1_t5, y_s2_t5, y_s3_t5 ]
]