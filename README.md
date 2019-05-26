# pastebin.sniffer
A python program that automatically saves every paste to a file.

This is a small project of mine, the program saves the link of the latest paste uploaded to the site from the archive. Then it goes to the http://pastebin.com/raw/<link> and saves the text to a file.

In the future I am planning to add a find feature, which will only create the new file if any of the keywords are found.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
 1) Download the repository
```
 git clone https://github.com/goddarkhun/pastebin.sniffer.git
```
 2) Install the requests library 
```
 sudo pip install requests
```
### Installing

1) Navigate to the folder 
```
 cd pastebin.sniffer/
```
2) Make the program executable 
```
 sudo chmod +x pastebin_sniffer.py
```
3) Run the program
```
 ./pastebin_sniffer
```
 
  
## Last words


The program will start creating new files numbered from 1 every 7 seconds. You can change the freqvency by changing "time.sleep(7)" to "time.sleep( <feqvency(seconds)> )". I found that 7 seconds is the avarage posting speed on pastebin. 
