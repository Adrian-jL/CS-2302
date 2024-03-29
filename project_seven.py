#Create on 11/12/19 by: Adrian Lopez 
#Project 7; Data Structures 2302, Instructor: Diego Aguirre, T.A: Gerardo Barraza
#Purpose: Implement the following dynamic-programming algorithm: Edit Distance

def edit_Distance(str1, str2, m , n): 
    #m and n represent the length of string 1 and 2 respectively
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
  
            # If first string is empty, only option is to insert all characters of second string 
            if i == 0: 
                dp[i][j] = j
            # If second string is empty, only option is to remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i  
            # If last characters are same, ignore last char and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            # If last character are different, consider all possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert 
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])      # Replace 
  
    return dp[m][n]