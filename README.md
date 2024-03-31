# ProjectEulerProblem


Alice a dessert-queen who can make exceptionally yummy chocolate chip cookies. Bob is a cookie connoisseur whose hunger rivals that of the (in)famous Cookie Monster from Sesame Street. One day, Alice and Bob decide to play a game. Bob chooses an arbitrary positive integer  k . Alice doesn't know what this number  k  is. She chooses two real numbers  a  and  b  randomly from within the interval  [0,1]  with uniform distribution. Suppose, you are acting as the referee in this game. You compute the square root of the sum  (ak+1)2+(bk+1)2  and round it to the next integer. If the result is equal to  k , Bob gets to eat  k  of Alice's cookies for free; otherwise he doesn't get to eat any cookies.

For example, if  k=6 ,  a=0.2 , and  b=0.85 , then the value that you get would be  (ak+1)2+(bk+1)2−−−−−−−−−−−−−−−−√=42.05−−−−√=6.484 . After you round it to the nearest integer it becomes  6  which is equal to  k . So, Bob will be allowed to eat  6  cookies.

# Input
You'll be given the value of  n, the number of turns of the game.

# Output
Print the expected value of the total number of cookies Bob will eat, rounded to five decimal places, if he plays  n  turns with  k=1 ,  k=2 ,  k=3 ,  … ,  k=n  (for the  1st ,  2nd ,  3rd ,  … , and  nth  turns respectively).****



# Sample Cases
Input
10

Output
10.20914

Input
73

Output
105.27674

Input
100000

Output
157055.80999

Input
69420

Output
109021.5883
