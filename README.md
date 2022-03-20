# Getting Started With Selenium 
![selenium-seeklogo com](https://user-images.githubusercontent.com/86334640/159179899-f257312f-4a6f-4fed-bc7c-6b54bcac768f.svg)

# The Guide :
<ul>
  <li><a href="#requirements-">Requirements</a></li>
  <li><a href="#installing-selenium-">Installing Selenium</a></li>
  <li><a href="#installing-webdriver-">Installing webDriver</a></li>
  <li><a href="https://www.google.com">First line of code : Getting acess to your webDriver</a></li>
  <li><a href="https://www.google.com">How do I navigate to a website using Selenium ?</a></li>
  <li><a href="https://www.google.com">How do I close the webdriver ?</a></li>
  <li><a href="https://www.google.com">How do I close the current window ?</a></li>
  <li><a href="https://www.google.com">How do I open New window ?</a></li>
</ul>

## Requirements :
<ul>
  <li>Browser : Google Chrome, Microsoft Edge, Opera GX... </li>
  <li>Python : <a href="https://www.python.org/downloads/">Just click here and download it now</a></li>
  <li>Selenium : <a href="https://www.python.org/downloads/">Install Selenium</a></li>
  <li>WebDriver : <a href="https://www.python.org/downloads/">Install Your WebDriver</a></li>
  <li>Code Editor : VScode, Pycharm</li>
</ul>

## Installing Selenium :
<ul>
  <li>1. tap the start button (or click the start icon) to open the start menu</li>
  <li>2. type cmd and tap enter</li>
  <li>3. And now type</li>
</ul>

``` 
pip install selenium 
``` 

## Installing webDriver :
##### Chrome WebDriver :
<ul>
  <li>1. <a href="https://chromedriver.chromium.org/downloads">Click to Download it</a></li>
  <li>2. choose the webDriver who has the same version as your browser</li>
  </ul>
  
  ![chrome1](https://user-images.githubusercontent.com/86334640/159185022-65badcb3-cb33-467e-9a41-a530f4420c75.PNG)
  
<ul>
  <li>3. choose your operating system</li>
</ul>

![chrome2](https://user-images.githubusercontent.com/86334640/159185041-6b5e6691-e4d2-4764-9228-e6d01d8559ba.PNG)

##### Microsoft Edge WebDriver :
<ul>
  <li>1. <a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">Click to Download it</a></li>
  <li>2. choose the webDriver who has the same version as your browser and according to your operating system</li>
</ul>

   ![edge_web_driver](https://user-images.githubusercontent.com/86334640/159184841-b7f48044-7532-436e-a7bc-83a82bd4b258.PNG)
   
## First Line Of Code : 
```
from selenium import webdriver #importing the object webdriver from selenium
# if you are using chrome webdriver
driver = webdriver.Chrome("Put the absolute path of Your webdriver example : C:\Program Files\chromedriver.exe")
# if you are using chrome webdriver
driver = webdriver.Chrome("Put the absolute path of Your webdriver example : C:\Program Files\msedgedriver.exe")
```
## How do I navigate to a website using Selenium ?
get() methode
code :
```
driver.get("write the website link example : https://www.google.com")
```
## How do I close the webdriver ?
quit() methode
code :
```
driver.quit()
```
## How do I close the current window ?
close() methode
code :
```
driver.close()
```
## How do I open New window ?
execute_script() method which is one of the ways of opening a new window than we use switch_to.window() methode to switch to a specific window
code : 
```
driver.execute_script("window.open('');")
```
example :
```
from selenium import webdriver
urlA = "https://www.google.com"
urlB = "https://www.youtube.com"
driver = webdriver.Chrome ("D:\developpement\chromedriver.exe")
driver.get(urlA)
# open new window with execute_script()
driver.execute_script("window.open('');")
# switch to new window with switch_to.window()
driver.switch_to.window(driver.window_handles[1])
driver.get(urlB)
```
## How do I find a web elements ?
these are the most used methods to find a webelements: <br>
these method will return a web element <br>
## find_element_by_id()
code:
```
driver.find_element_by_id("type the id")
```
## find_element_by_class_name() <br>
Note : this method will return the first web element who has this class name 
```
driver.find_element_by_class_name("type the class name")
```
## find_element_by_name() <br>
Note : this method will return the first web element who has this attribute name 
```
driver.find_element_by_name("type the name")
```
## find_element_by_css_selector()
```
driver.find_element_by_css_selector("type css selector")
```
to get the css selector :

<li>1. right click on the web element</li>
<li>2. hover on copy</li>
<li>3. click to "Copy selector"</li> <br> 
  
![Capture1](https://user-images.githubusercontent.com/86334640/159187768-14ff57e5-73a0-4f09-b8fc-d3bf418d0ce2.PNG)

<li>4. paste it in your code</li> <br>

## find_element_by_xpath() 
```
driver.find_element_by_xpath("type the xpath")
```
to get the css selector :

<li>1. right click on the web element</li>
<li>2. hover on copy</li>
<li>3. click to "Copy xpath"</li> <br> 

![Capture1](https://user-images.githubusercontent.com/86334640/159187768-14ff57e5-73a0-4f09-b8fc-d3bf418d0ce2.PNG)

<li>4. paste it in your code</li> <br>

## find_element_by_tag_name() <br>
Note : this method will return the first web element who has this tag
```
driver.find_element_by_tag("type the tag")
```
example : 
```


