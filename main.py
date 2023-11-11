#Greeting the user
print("Welcome to the advanced browser tabs simulation")

#initialize the list tabs
tabs=[]
#Function handles the main menu options
def MainMenu():
  print("\n1. Open Tab \n2. Close Tab \n3. Switch Tab\n4. Display All Tabs \n5. Open Nested Tab \n6. Clear All Tabs \n7. Save Tabs \n8. Import Tabs \n9. Exit \n- - - - - - - - - - - - - - -")

def OpenTab(title,URL):
    dic={"Title":title , "URL":URL, "NestedTabs":[]}
    tabs.append(dic)
    return "Tab Added Successfully"
