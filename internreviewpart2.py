import os
path = 'grades.csv'

checkFile = os.path.isfile(path)

         

if checkFile == True:  
    infile = open(path, 'r')
            #class list
    classList = infile.readlines()

        
    #close the file
    infile.close()
            
    gradeLength = len(classList)-1

        
        
    gpaList = ('A', 4, 'A-', 3.67, 'B+', 3.33, 'B', 3, 'B-', 2.67, 'C+', 2.33, 'C', 2, 'C-', 1.67, 'D+', 1.33, 'D', 1, 'F', 0)
    cumulativeCredits = 0
    cumulativeGPA = 0
    gradeCount = 1
    gpaCheck = 0
    processGrade = 0
         
    if gradeLength <= 0: 
        print('No grades are found, are they inputted correctly?')
        #if no grades are found under the grades section, this error will appear. Anything less than 1 grade will cause this. To test, delete all grades. 
        # this edge case checks if credits are filled out. If not, this error will appear.  
    while processGrade < gradeLength:
        numberGrade = classList[gradeCount].split(',')
        while True: 
        #split(',') splits where the commmas are found
                
         #   if numberGrade[1] != (gpaList[gpaCheck]):
             #   print('Missing or incorrect grade')
              #  break
#this edge case is suppose to check if the user input in grade section on the excel sheet. The edge case for grades is F to A+ with any letters or numbers should be thrown out. The way to test is change to (for instance) "G", which is not on the grading scale. 
                 # However, it's only reading the first letter "A" and throwing out the rest. I haven't figured out how to fix. 
                
            if numberGrade[1] == gpaList[gpaCheck]:
                print('Class:  ', numberGrade[2], '  Credits: ', numberGrade[0], '  Grade: ', numberGrade[1])
                    #individualClass (renamed to numberGrade) means the grade the person achieved in the class? 
                    #add to weighted grade
                cumulativeGPA = cumulativeGPA + gpaList[gpaCheck+1] * int(numberGrade[0])
                cumulativeCredits = cumulativeCredits + int(numberGrade[0])
                break
           
            gpaCheck = gpaCheck + 2
        gpaCheck = 0
        gradeCount = gradeCount + 1
        processGrade = processGrade + 1  
        if cumulativeCredits <= 0:
            print('Incorrect input on grades')
            break
            #this edge case checks if any negative numbers or even zero are found under credit. The program will stop. You can't divide by a zero. That's why it's the beginning of the edge case. To test, input non positive numbers in the credits. 
    
        else:
            finalGPA = str(round(cumulativeGPA/cumulativeCredits, 2))
            print ('Your Final GPA is: ', finalGPA)
         
                            #calculate the GPA
             

            

else: 
    print('File does not exist')
    print('You can restart by pressing the letter r')
        
