import pandas as pd
import numpy as np
df=pd.read_csv("prac9/prac9.csv")
print(df)


# calculate prior probabilities

# calculate total number of yes and no

total_yes=len(df[df['Play_Tennis']=='yes'])
total_no=len(df[df['Play_Tennis']=='no'])
print("total_yes=",total_yes,"total_no=",total_no)

# calculate prior probabilities

prior_yes=total_yes/len(df)
prior_no=total_no/len(df)
print("prior_yes=",prior_yes,"prior_no=",prior_no)

#calculate likelihood

#calculate likelihood of outlook

#calculate total number of rain

total_rain=len(df[df['Outlook']=='rain'])
print("total_rain=",total_rain)

#calculate likelihood of rain
likelihood_rain=total_rain/len(df)
print("likelihood_rain=",likelihood_rain)


# calculate likelihood of temprature

# calculate total number of cool

total_cool=len(df[df['Temprature']=='cool'])
print("total_cool=",total_cool)

# calculate likelihood of cool

likelihood_cool=total_cool/len(df)
print("likelihood_cool=",likelihood_cool)

# calculate likelihood of humidity

# calculate total number of high 

total_high=len(df[df['Humidity']=='high'])
print("total_high=",total_high)


# calculate likelihood of high 

likelihood_high=total_high/len(df)
print("likelihood_high=",likelihood_high)

# calculate likelihood of wind

# calculate total number of weak 

total_weak=len(df[df['wind']=='weak'])
print("total_weak=",total_weak)

# calculate likelihood of weak 

likelihood_weak=total_weak/len(df)
print("likelihood_weak=",likelihood_weak)

# calculate posterior probabilities

# calculate posterior probabilities of yes

posterior_yes=likelihood_rain*likelihood_cool*likelihood_high*likelihood_weak*prior_yes
print("posterior_yes=",posterior_yes)

# calculate posterior probabilities of no

posterior_no=likelihood_rain*likelihood_cool*likelihood_high*likelihood_weak*prior_no
print("posterior_no=",posterior_no)

# predict the class of the case

if posterior_yes>posterior_no:
    print("the class of the case is yes")
else:
    print("the class of the case is no")



