import csv
from dataclasses import dataclass

@dataclass
class Computer():
    asset: str = ""
    name:  str = ""
    
    def getIterable(self):
        return [self.asset, self.name]
    
    def __str__(self):
        return self.asset + ": " + self.name

class Computers(list):
    
    def load(filename = "computers.csv"):
        newList = Computers() 
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                newList.append(Computer(row[0], row[1]))
            return newList
           
    def save(self, filename = "computers.csv"): 
        with open(filename, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for row in self:
                spamwriter.writerow(row.getIterable())
    
    
    def getComputer(self, text):
        for computer in self:
            if computer.asset.strip().lower() == text.strip().lower():
                return computer
            
        for computer in self:
            if computer.name.strip().lower() == text.strip().lower():
                return computer
            
            return False
    
    def add(self, asset, name):
        self.append(Computer(asset , name))     


computers = Computers.load()

while True:
    asset = input("Scan Asset Tag : ")
    computer = computers.getComputer(asset)
    if computer:
        print(computer)
    else :
        print("Not Found")
        name = input("Scan Name Tag : ")
        if(name):
            print("Saving ", asset , name) 
            computers.add(asset , name)
            computers.save()
        else :
            print("Nothing to save.")
