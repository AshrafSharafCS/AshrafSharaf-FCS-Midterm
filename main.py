import validators
#Greeting the user
print("Welcome to the advanced browser tabs simulation")

#initialize the list tabs
tabs=[]
#Function handles the main menu options
def MainMenu():
  print("\n1. Open Tab \n2. Close Tab \n3. Switch Tab\n4. Display All Tabs \n5. Open Nested Tab \n6. Clear All Tabs \n7. Save Tabs \n8. Import Tabs \n9. Exit \n- - - - - - - - - - - - - - -")

#OpenTab function takes title and URL as parameters to add the tab to the tabs list and checks if any input is invalid to return invalid otherwise
def OpenTab(title,URL):
  validate=validators.url(URL)
  if validate is True :
    dic={"Title":title , "URL":URL, "NestedTabs":[]}
    tabs.append(dic)
    return "Tab Added Successfully"
  else:
    return "Invalid URL"




#using while loop we take the users input and call the function accordingly
while True:

  MainMenu()
  choice=input("Choose an option from the menu: ")
  if choice=='1':
    title=input("Enter a title for your tab: ")
    url=input("Enter the url for your tab: ")
    print(OpenTab(title,url))