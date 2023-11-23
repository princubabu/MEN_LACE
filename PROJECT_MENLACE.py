#teachers data
AMON = {'1I','4W '}
ATUE = {'1I','2W','4W'}
BMON = {'2I','1W','5W'}
BTUE = {'4I','5I','1W'}
CMON = {'3I','4I','2W'}
CTUE = {'3I','5W'}
DMON = {'5I','3W'}
DTUE = {'2I','3W'}

#INPUTING THE TEACHERS NAME AND DAY
teacher_name = input("Enter the name of teacher")
today_date = input("Enter today's date")

#CREATING A NEW VARIABLE
LIS = teacher_name+today_date
print(LIS)



#tHE ASSIGNER 


if LIS == "AMON":
    for x in AMON:
         CLASS = x[:0] + x[0+1:] #IT SEPERATES class like = I or W from !W or 2I also works for more words for example 1 2nd C this will seperate 2nd C
         Period = x[0] # same just seperates periods like above but only first character
         
         if x not in BMON:
            print ("Assign teacher b to",CLASS,"at period",Period)   #still there is a problem where you can see that if A= [1W,4I] and B= {!I, 4W}  so it couldnt really seperate it like how teacher b will attend first period in both bacthes thats the problem i want you to solve 
         elif x not in CMON:
            print ("Assign teacher c to",CLASS,"at period",Period)

         elif x not in DMON:
            print ("Assign teacher d to",CLASS,"at period",Period)
        

elif LIS == "ATUE":
    for x in ATUE:
         CLASS = x[:0] + x[0+1:]
         Period = x[0]
         
         if x not in BTUE:
            print ("Assign teacher b to",CLASS,"at period",Period)     
         elif x not in CTUE:
            print ("Assign teacher c to",CLASS,"at period",Period)

         elif x not in DTUE:
            print ("Assign teacher d to",CLASS,"at period",Period)
    
elif LIS == "BMON":
    for x in BMON:
         CLASS = x[:0] + x[0+1:]
         Period = x[0]
         
         if x not in AMON:
            print ("Assign teacher A to",CLASS,"at period",Period)     
         elif x not in CMON:
            print ("Assign teacher C to",CLASS,"at period",Period)

         elif x not in DMON:
            print ("Assign teacher d to",CLASS,"at period",Period)
    
elif LIS =="BTUE":
    for x in BTUE:
         CLASS = x[:0] + x[0+1:]
         Period = x[0]
         
         if x not in ATUE:
            print ("Assign teacher A to",CLASS,"at period",Period)     
         elif x not in CTUE:
            print ("Assign teacher c to",CLASS,"at period",Period)

         elif x not in DTUE:
            print ("Assign teacher d to",CLASS,"at period",Period)
    

elif LIS == "CMON":
    for x in CMON:
         CLASS = x[:0] + x[0+1:]
         Period = x[0]
         
         if x not in AMON:
            print ("Assign teacher A to",CLASS,"at period",Period)     
         elif x not in BMON:
            print ("Assign teacher B to",CLASS,"at period",Period)

         elif x not in DMON:
            print ("Assign teacher d to",CLASS,"at period",Period)
    
    
elif LIS == "CTUE":
    for x in CTUE:
         CLASS = x[:0] + x[0+1:]
         Period = x[0]
         
         if x not in ATUE:
            print ("Assign teacher A to",CLASS,"at period",Period)     
         elif x not in BTUE:
            print ("Assign teacher B to",CLASS,"at period",Period)

         elif x not in DTUE:
            print ("Assign teacher d to",CLASS,"at period",Period)
    

elif LIS == "DMON":
    for x in DMON:
         CLASS = x[:0] + x[0+1:]
         Period = x[0]
         
         if x not in AMON:
            print ("Assign teacher A to",CLASS,"at period",Period)     
         elif x not in CMON:
            print ("Assign teacher c to",CLASS,"at period",Period)

         elif x not in BMON:
            print ("Assign teacher B to",CLASS,"at period",Period)
    
elif LIS == "DTUE":
    for x in DTUE:
         CLASS = x[:0] + x[0+1:]
         Period = x[0]
         
         if x not in ATUE:
            print ("Assign teacher A to",CLASS,"at period",Period)     
         elif x not in CTUE:
            print ("Assign teacher c to",CLASS,"at period",Period)

         elif x not in BTUE:
            print ("Assign teacher B to",CLASS,"at period",Period)
    

