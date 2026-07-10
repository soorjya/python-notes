nums = [1,2,3,4,5,6,7,8,9,10] // taken by default 

# 1. Line comprehsion 
sq = [x**2 for x in nums] 

# 2. conditions
evens = [x for x in nums if x % 2 ==0]    #[2,4,6,8,10]

# 3. List comparehension with if-else
labeled = ["even" if x % 2 == 0 else "odd" for x in nums]   #["odd", "even", "odd", "even", ...]

#4. Nested list 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpod = [[row[i] for row in matrix] for i in range(3)]
#[[1,4,7],[2,5,8],[3,6,9]]
