import validators
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import os.path
#Greeting the user
print("Welcome to the advanced browser tabs simulation")

#initialize the list tabs
tabs=[]
#Function handles the main menu options
def MainMenu():
  print("\n1. Open Tab \n2. Close Tab \n3. Switch Tab\n4. Display All Tabs \n5. Open Nested Tab \n6. Clear All Tabs \n7. Save Tabs \n8. Import Tabs \n9. Exit \n- - - - - - - - - - - - - - -")

#function to validate the url
def validateURL(url):
  validate=validators.url(url)
  if validate is True:
    return True
  else:
    return False




#OpenTab function takes title and URL as parameters to add the tab to the tabs list and checks if any input is invalid to return invalid otherwise
def OpenTab(title,URL):
  if validateURL(url) is True :
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
    else:
      url=str(tabs[-1]["URL"])
      page = urlopen(url)
      soup = BeautifulSoup(page, "html.parser")
      print(soup.prettify)   

#open nested tab function takes an index from the user and opens  nested tab with the given index
def OpenNestedTab(index,title,url):
  if len(tabs)==0:
    return "No Tabs Found"
  else:
    if 1<=index<=len(tabs) and validateURL(url) is True :
      dic={"Title":title , "URL":url}
      tabs[index-1]["NestedTabs"].append(dic)
      return "Nested Tab Added Successfully"
    else:
      return "Invalid Input"

#ClearAllTaps function, cears all tabs in the tabs list
def ClearAllTabs():
  if len(tabs)==0:
    print("No Tabs Found")
  else:
    tabs.clear()
    print("Tabs Cleared Successfuly")

#savetaps function save the tabs in the list to a json file

#i used these websites to help me with the json conversion and path existence:
#https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/?ref=header_search
#https://www.freecodecamp.org/news/how-to-check-if-a-file-exists-in-python/

def SaveTaps(path):
  if len(tabs)==0:
    print("No Tabs Found")
  else:
    checkpath=os.path.exists(path)
    if checkpath is True:
      json_object=json.dumps(tabs)
      with open(path,"w") as outfile:
        outfile.write(json_object)
        print("Tabs saved successfuly")
    else:
      print("Path does not exist")

#import function takes a path as an input and reads the tabs int the json file
def ImportTabs(path):
  if len(tabs)==0:
      print("No Tabs Found")
  else:
    with open(path, 'r') as openfile:
      checkpath=os.path.exists(path)
      if checkpath is True:
        json_object = json.load(openfile)
        print(json_object)
      else: 
        print("Path does not exist")
        
    

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
  elif choice=='5':
    index=int(input("Enter the index of the tab where you want to add the nested tab : "))
    title=input("Enter a title for your nested tab: ")
    url=input("Enter the url for your nested tab: ")
    print(OpenNestedTab(index,title,url))
  elif choice=='6':
    ClearAllTabs()
  elif choice=='7':
    path=input("Enter a file path to save the current open tabs: ")
    SaveTaps(path)
  elif choice=='8':
    path=input("Enter a file path to save the current open tabs: ")
    ImportTabs(path)
 