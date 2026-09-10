Web_development = ["frontend","backend","full stack"]
Data_science = ["Data analyst","data scientist","data engineer"]
ui = ["ui designer","ux designer","ux resarcher"]
all_participants = [Web_development,Data_science,ui]
print(all_participants)
Web_development.append("lead developer")
print(Web_development)
Data_science.insert(1,"Business anlyst")
print(Data_science)
new_datascience = Data_science.copy()
print(new_datascience)
Data_science.clear()
print(Data_science)
print(Web_development[:2])
print("Asha" in all_participants)
first_participants = (Web_development[0],new_datascience[0],ui[0])
print(first_participants)
name_length =[len(name)for name in new_datascience]
print(name_length)
