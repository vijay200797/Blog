import pandas as pd
dic_employee= {
    "Name" : ["Ram","Avtar", "Rahul", "VK","Sonu", "SM"],
    "Email" : ["ram@ram.com", "avtar@av.com", "rahul@rahu.com", "vk.vk.com", "sonu@sonu.com","sm@sm.com"],
    "Oct_Sal":[7000,4000,5000, 6000,None,5323],
    "Nov_Sal":[4400,2300,None, 3500,3340,5623],
    "Dec_Sal":[3433,None,4577, None,3387,5676]
    }

df = pd.DataFrame(dic_employee)
df =df.fillna(0)
# df["Total+Sal"] = df["Oct_Sal"] + df["Nov_Sal"] + df["Dec_Sal"]
# df = df.drop(df[(df["Name"]=="Ram") | (df["Name"]=="Avtar")].index)
# df = df[(df["Name"]=="Ram") | (df["Name"]=="Avtar")]
# df = df[(df["Name"]=="Ram") & (df["Nov_Sal"]>3500)]
print(df)