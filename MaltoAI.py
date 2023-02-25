#Malto : One assist towards efficiency
print("Hello!! My name is Malto and I am here to assist you in your tasks")
name = input("What is your name : ")
print("Nice to meet you {} How can I help you..".format(name))
Task = (input("What is your first task : ")).lower()
if Task == "calculator" :
    print("Opening calculator.....")
    A=int(input("Enter a value A : "))
    B=int(input("Enter a value B :  "))
    Task1=(input("What you want to do : "))
    if Task1=="add":
        add=A+B
        print("Here your answer is :" ,add)
        
    if Task1=="divide":
        divide=A/B
        print("Here your answer is :" ,divide)
        
    if Task1=="multiply":
        multiply=A*B
        print("Here your answer is :" ,multiply)
        
    if Task1=="substract":
        substract=A-B
        print("Here your answer is :" ,substract)
      
#NextCalc = input("Do you  want any more calculation : ")
#if NextCalc == "yes":
#    continue
#if NextCalc == "no":
#  break
if Task == "friend" :
    print("Opening friend.....")
    L1=(input("Hello there I am Malto \n Will you be my Best friend : ")).lower()
    if L1=="yes" :
      print("Cool from now Malto and {} is best friends".format(name))
    L2=(input("Do you want to hear a joke from me : ")).lower()
    if L2=="yes" :
        print("Why are snails slow? Because they’re carrying a house on their back. :D")
    else :
        print("No problem I understand *_*")
      
if Task == "table" :
    print("Opening Table counter...")
    T = int(input("Enter the number you want Table of : "))
    print("The required table :")
    for count in range(1, 11):
      print(T, 'x', count, '=', T * count)
#Task2 = input("Do you have any other task for me : ")
#if Task2 == "yes":
  #Task = (input("What is your first task : "))
if Task == "notepad":
  print("Opening notepad...")
  x = input("Type from here : ")
  y = input("Do you want to save the text you write : ").lower()
  if y=="no":
   print("Page deleted")
   print("Closing Notepad...")
  if y=="yes":
   print("Page saved")
   print("Closing Notepad...")
if Task == "quiz":
  print("Opening Quiz...")
  s = input("Are you ready for the quiz : ").lower()
  if s=="yes":
     print("Starting Quiz......")
  q1 = int(input("2+2+2-8/9×0 : "))
  q2 = input("Capital of Sri Lanka : ").lower()
  q3 = input("Complete the pattern × + × + × : ")
  q4 = int(input("What number should come next 36, 34, 30, 28, 24, ? : "))
  q5 = input("The red colour of blood is because of the presence of : ").lower()
  if (q1==0,q2=="columbia",q3=="+",q4==22,q5=="rbc"):
    print("Great Job!!! you have answered all the questions correct.")
    print("Closing Quiz...")
  else:
   print("Wrong answer..:(")
   print("Try next time")
   print("Closing Quiz")
  
if Task == "even counter":
   V1=int(input("Enter the intial range :"))
   V2=int(input("Enter the final range : "))
   for w in range (V1,V2,2):
    print("The values are : ",w)
if Task == "odd counter":
   V1=int(input("Enter the intial range :"))
   V2=int(input("Enter the final range : "))
   for w in range (V1,2*V2+1):
     print("The values are : ",w)

     