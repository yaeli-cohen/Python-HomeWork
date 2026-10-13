from pickletools import uint8


def func(txtUrl):
        count = 0
        with open(txtUrl, 'r', encoding='utf-8') as f:
            data = f.read()
            words = data.split()
            count += len(words)
        print("Total Words:", count)

func(r'C:\Users\User\Documents\תכנות\שנה ב\python\lesson4\myText.txt')


import csv

def func2(link):
    with open('out.csv', 'w', newline='', encoding='utf-8') as f:
        for a in link:
            writer = csv.writer(f)
            writer.writerow(a)



links = [['Nikhil', 'COE', '2', '9.0'],
         ['Sanchit', 'COE', '2', '9.1'],
         ['Aditya', 'IT', '2', '9.3'],
         ['Sagar', 'SE', '1', '9.5'],
         ['Prateek', 'MCE', '3', '7.8'],
         ['Sahil', 'EP', '2', '9.1']]

func2(links)


