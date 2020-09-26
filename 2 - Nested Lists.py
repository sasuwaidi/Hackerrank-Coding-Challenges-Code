#initializing marksheet list (with names and scores) and score list
msL=[]
sL=[]

if __name__ == '__main__':
#itertating based on students
        for _ in range(int(input())):
#identifying student and score and inputting it into respective list
                Name = input()
                Score = float(input())
                msL+=[[Name,Score]]
                sL+=[Score]
#identifying max score and sorting students in order of name (n) and score (s)
        mScore = sorted(list(set(sL)))[1]
#identifying student(s) with the second lowest grade based on name (s) and score (s)
        for n,s in sorted(msL):
             if s == mScore:
                    print(n)
