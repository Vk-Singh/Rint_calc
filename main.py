
import pandas as pd

my_dict = {}

f = open("D:\\IdeaProjects\\Rint_Calc\\data.txt", "r")

for x in f:

    if x == '\n':
        pass

    else:

        splitlist = x.split()
        print (splitlist)

        if splitlist[0] in my_dict:
            my_dict[splitlist[0]].append(splitlist[1])
        else:
            my_dict[splitlist[0]] = [splitlist[1]]

        #print splitlist[0]

f.close()
df=pd.DataFrame.from_dict(my_dict,orient='index').transpose()
df = df.reindex(sorted(df.columns), axis=1)
print (df)
#df.to_excel("Output.xlsx")

df.to_csv("D:\\IdeaProjects\\Rint_Calc\\Output1.csv")
