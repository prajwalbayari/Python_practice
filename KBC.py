import shutil

terminal=shutil.get_terminal_size().columns
print('-'*terminal)
name=input("Welcome to Kaun Banega Karodpati.!!\n\n Enter your name: ")
print()

questions=["Question 1: Who is the only player to score a century in their 100th Test match?",
           "Question 2: Who was the first bowler to take a hat-trick in a T20 International match?",
           "Question 3: Which cricketer has scored the most runs in a single Test match?",
           "Question 4: Who holds the record for the fastest double century in Test cricket?",
           "Question 5: Which country won the ICC Cricket World Cup in 1992?",
           "Question 6: Who was the first player to score 10,000 runs in One Day Internationals?",
           "Question 7: Which bowler has taken the most wickets in the history of Test cricket?",
           "Question 8: Who is the only cricketer to have scored a triple century in a Test match twice?",
           "Question 9: Who was the first captain to win three ICC trophies (T20 World Cup, ODI World Cup, and Champions Trophy)?",
           "Question 10: What is the highest individual score in an ODI match?"]
options=[["a) Ricky Ponting","b) Hashim Amla","c) Colin Cowdrey","d) Joe Root"],
         ["a) Brett Lee","b) Lasith Malinga","c) Rashid Khan","d) Jacob Oram"],
         ["a) Brian Lara","b) Matthew Hayden","c) Virender Sehwag","d) Graham Gooch"],
         ["a) Nathan Astle","b) Virender Sehwag","c) Ben Stokes","d) Adam Gilchrist"],
         ["a) England","b) West Indies","c) Pakistan","d) Australia"],
         ["a) Sunil Gavaskar","b) Allan Border","c) Sachin Tendulkar","d) Desmond Haynes"],
         ["a) Shane Warne","b) James Anderson","c) Muttiah Muralitharan","d) Anil Kumble"],
         ["a) Don Bradman","b) Brian Lara","c) Virender Sehwag","d) Chris Gayle"],
         ["a) Ricky Ponting","b) MS Dhoni","c) Eoin Morgan","d) Clive Lloyd"],
         ["a) 264","b) 237*","c) 219","d) 209*"]]
answers=['a','a','d','a','c','c','c','c','b','a']
select=['a','b','c','d']
tot=-1
prize=[5000,10000,50000,100000,200000,400000,800000,2500000,5000000,10000000]
for x in range(0,11):
    print('-'*terminal)
    print(questions[x],"\n"," ".join(options[x]))
    ans=input("\nEnter your choice(Enter the alphabet of your choice): ")
    while(ans not in select):
        ans=input("\nInvalid option!!! Please enter your answer again: ")
    if(ans==answers[x]):
        print("Correct answer!!!\n")
    else:
        print("Incorrect answer!!!\n")
        break
    tot+=1

if (tot==-1):
    print("You could not answer any questions. Better luck next time.")
else:
    print("Congratulations {} you have won {} Rupees!!!".format(name,prize[tot]))
print('-'*terminal)