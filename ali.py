class Student:
    def __init__(self, name, id):
        self.name=name
        self.id=id
        self.__grades=[]
        
    def get_grades(self):
        return self.__grades

    def add_grades(self, grades):
        for grade in grades:
            if 0 <= grade <= 100:
                self.__grades.append(grade)
            else :
                print ("Invalid grade, Grade must be betw 0 and 100")
                
                
    def calculate_grades(self):
        if not self.__grades:
            return "N/A"

        average= self.calculate_average()   

        if 90 <= average <= 100 :
            return "A"   

        elif 80 <= average <= 90 :
            return "B"
            
        elif  70 <= average <= 80 :
            return "C" 
            
        elif 60 <= average <= 70 :
            return "D"   
            
        else:
            return "F"
            
    def calculate_average(self):
        if not self.__grades:
            return 0

        return sum(self.__grades) / len(self.__grades)        
    
    
    def display_info(self):
        print("Name:", self.name)
        print(" ID:", self.id)
        print("Grades:", self.get_grades())
        print("Letter:", self.calculate_grades())
        print("Average:", self.calculate_average())   

s1 = Student("Ali Ahmed", 2501123)

s1.add_grades([150])
s1.add_grades([90])
s1.add_grades([80])
s1.add_grades([70])

s1.display_info()