import validators
from urllib.request import urlopen
from bs4 import BeautifulSoup
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

#close tab function takes an index from the user and removes the cooresponing tab from the list
def CloseTab(index):
  if len(tabs)==0:
    return "No Tabs Found to close"
  else:
    if 1<=int(index)<=len(tabs):
      tabs.pop(index-1)
      return "Tab Closed Successfully"
    else:
      tabs.pop()
      return "Last tap opened is closed"


#display all tabs function displays all the tabs in the list including nested lists
def DisplayAllTabs(list):
  if len(list)==0:
    print("No Tabs Found")
  else:
    for i in range(len(list)):
      print(i+1,list[i]["Title"])
      for j in range(len(list[i]["NestedTabs"])):
           print("\t",j+1,list[i]["NestedTabs"][j]["Title"])

#switch tab function takes an index form the user and prints the html content for the tab with the given index
#https://www.datacamp.com/tutorial/web-scraping-using-python
def SwitchTab(index):
  if len(tabs)==0:
    return "No Tabs Found"
  else:
    if 1<=index<=len(tabs):
      url=str(tabs[index-1]["URL"])
      page = urlopen(url)
      soup = BeautifulSoup(page, "html.parser")
      print(soup.prettify)   

        
#using while loop we take the users input and call the function accordingly
while True:

  MainMenu()
  choice=input("Choose an option from the menu: ")
  if choice=='1':
    title=input("Enter a title for your tab: ")
    url=input("Enter the url for your tab: ")
    print(OpenTab(title,url))
  elif choice=='2':
    index=int(input("Enter the index of the tab you want to close or press enter to close the last opened tab: "))
    print(CloseTab(index))
  elif choice=='3':
    index=int(input("Enter the index of the tab you want to switch : "))
    SwitchTab(index)
  elif choice=='4':
    DisplayAllTabs(tabs)