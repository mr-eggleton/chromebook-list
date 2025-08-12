import csv
import re
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
    def load(filename="computers.csv"):
        newList = Computers()
        with open(filename, newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                newList.append(Computer(row[0], row[1]))
            return newList

    def save(self, filename="computers.csv"):
        with open(filename, 'w', newline='') as csv_file:
            spam_writer = csv.writer(csv_file)
            for row in self:
                spam_writer.writerow(row.getIterable())

    def summarize(self):
        summary = {}
        for computer in self:
            trolley = re.sub('\\d', '', computer.name.strip().upper())
            # print(trolley, summary)
            if (trolley not in summary):
                # print("if(trolley not in self)")
                summary[trolley] = 0
            summary[trolley] += 1
        print("Summary", summary)
        print("Target  {'OLP-CR-EN': 1, 'INCLUSION': 15, 'HEALTH': 20,"
              + " 'OLP-CR-CON': 8, 'SPORT': 26, 'OLP-CR-SP': 26}")
        print("Total", len(self))

    def getComputer(self, text):
        for computer in self:
            if computer.asset.strip().upper() == text.strip().upper():
                return computer

        for computer in self:
            if computer.name.strip().upper() == text.strip().upper():
                return computer

        return False

    def add(self, asset, name):
        self.append(Computer(asset.strip().upper(), name.strip().upper()))
        return self.getComputer(asset)

    def updateComputer(self, asset, name):
        for computer in self:
            if computer.asset.strip().upper() == asset.strip().upper():
                computer.name = name
                return computer

        return False


computers = Computers.load()
computers.summarize()
next_is_broken = False
next_is_missing = False

while True:
    asset = input("Scan Asset Tag : ")
    computer = computers.getComputer(asset)

    if computer:
        print(computer)
        status = False

        if next_is_broken:
            status = "Broken:"
            next_is_broken = False

        if next_is_missing:
            status = "Missing:"
            next_is_missing = False

        if status:
            updated_computer = computers.updateComputer(asset, status
                                                        + computer.name)
            print("Saving ", updated_computer)

            computers.save()
            computers.summarize()
            next_is_broken = False
    elif asset.lower().strip() == "br":
        next_is_broken = True
        print("Next Scanned item will be marked as broken")

    elif asset.lower().strip() == "mi":
        next_is_missing = True
        print("Next Scanned item will be marked as missing")

    else:
        print("Not Found")
        name = input("Scan Name Tag : ")
        if (name and name.strip().upper() != "ERROR"):
            newComputer = computers.add(asset, name)
            print("Saving ", newComputer)
            computers.save()
        else:
            print("Nothing to save.")
