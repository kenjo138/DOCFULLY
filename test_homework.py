
#    Use the list: [2,3,4,5,8,4,6,3,4,6,8,9,7,5,3,5,7,4,3,2,2,1,4,6,8,6,8,9,3]

data = [2,3,4,5,8,4,6,3,4,6,8,9,7,5,3,5,7,4,3,2,2,1,4,6,8,6,8,9,3]

# Section 4 : Q3
print(50*'-')
print("Section 4 : Q3")
print(50*'-')

#mean_function
def mean_fn(data):
    try:
        return sum(data)/len(data)
    except:
        print("Divide by 0!")
        return 0


#mode_function
def mode_fn(data):

   #Initialize variables
   most_freq=0
   count=0
   
   #Return zero if empty list
   if len(data)==0:
      return 0

   #Find the unique number in the list
   data1=set(data)

   #Count the frequency of the unique number
   #Determine the most freq
   for i in data1:
      if count<data.count(i):
          most_freq=i
          count=data.count(i)
          
   return most_freq  

#median_function
def median_fn(data):

    #Return zero if empty list
    if len(data)==0:
      return 0
    
    data.sort()

     
    #the data length is odd
    if len(data)%2 != 0:
        median_val=data[int(len(data)/2.0+0.5)]
    else:
        median_val=0.5*(data[int(len(data)/2-1)]+data[int(len(data)/2)])
    
    return median_val


#main function
print(mode_fn(data))
