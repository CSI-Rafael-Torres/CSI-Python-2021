import random
def my_string(name,student_num,age):
    f = random.randint(22,28)
    print("Hello"+ name+ "! Your student number is "+str(f)+"-"+str(student_num)+" and you are "+str(age)+" years old.")
n = random.randint(1,100)
my_string(input("Please put in your name. "),n,input("How old are you? "))