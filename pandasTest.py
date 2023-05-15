import pandas as pd
dic_employee= {
    "Name" : ["Ram","Avtar", "Rahul", "VK","Sonu", "SM"],
    "Email" : ["ram@ram.com", "avtar@av.com", "rahul@rahu.com", "vk.vk.com", "sonu@sonu.com","sm@sm.com"],
    "Oct_Sal":[7000,4000,5000, 6000,None,5323],
    "Nov_Sal":[4400,2300,None, 3500,3340,5623],
    "Dec_Sal":[3433,None,4577, None,3387,5676],
    "Dept_id":[1,1,2,3,3,4]
    }

df = pd.DataFrame(dic_employee)
# df = df.fillna(0)

## Create New Column
# df["Total+Sal"] = df["Oct_Sal"] + df["Nov_Sal"] + df["Dec_Sal"]

## Drop Row by Filter Condition
# df = df.drop(df[(df["Name"]=="Ram") | (df["Name"]=="Avtar")].index)

## Get Row by Filter Condition
# df = df[(df["Name"]=="Ram") | (df["Name"]=="Avtar")]
# df = df[(df["Name"]=="Ram") & (df["Nov_Sal"]>3500)]

# Get Column Value
print(df)
print(df.loc[0, ["Name","Email"]])
print(df["Email"][1])
for i in df.index:
    print(df["Name"][i])


# Insert a New Row
df.loc[df.index.max()+1] =["ABC", "ABC@abc.com",200,222,222,5]

# Update Row
df.loc[3,['Name', 'Email', 'Dec_Sal']] = ["Shyam", "shyam@sh.com", 4050]

# Short Row By Column
df = df.sort_values(by ='Name', ascending=True)
# Short Row By Multiple Column
df = df.sort_values(by =['Name', 'Email'], ascending=[True, False])

# df =df.groupby(by=['Dept_id','Name'])['Name', 'Email'].Name.count()
print(df)
