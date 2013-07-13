This is similar to the previous code, but in python. I modified the clean.py
to be ensure the format was consistent. dict.py generates a dicionary of the
brand ids and the brand names in a csv file. 

cfilter.py is a collaborative filter that is very simialr to the code I 
wrote in R that I wrote before but works much faster. The first 
recommendation is based off of finding the percent of users that had an 
additional brand in addition to the given brand. A second method involved 
generating weights/ratings based on the number of favorited items each user 
had. The logic behind that being if only 2 brands were favorited then they 
had a high correlation. The more brands favorited the lower correlation 
between them. Thus the weights were generated using the formula 
1/(num of favorited brands) for each user. Other weighing functions could 
have been implemented. This allows us to further examine the the users and 
brands using other techniques.

The sample output is given below:

Marc by Marc Jacobs      0.586971
Christian Louboutin      0.510516
Victoria's Secret        0.504936
Prada                    0.497796
Burberry                 0.479713
Steve Madden             0.467764
Juicy Couture            0.463189
Forever 21               0.444402
Diane von Furstenberg    0.401180
MICHAEL Michael Kors     0.391208
Name: Related Ranking


Victoria's Secret       0.036682
Marc by Marc Jacobs     0.033954
Steve Madden            0.033641
Forever 21              0.033495
Juicy Couture           0.031437
GUESS                   0.031077
MICHAEL Michael Kors    0.030759
Christian Louboutin     0.029717
Prada                   0.029544
Burberry                0.026168
Name: Weighted Ranking


25.2819919586 seconds
