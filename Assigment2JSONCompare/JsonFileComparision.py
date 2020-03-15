import json
import requests
import os

class cmphttpres():
    def get_url(self, url):
        return requests.get(url).json()

    def ordered(self, data):
        if isinstance(data, dict):
            return sorted((k, self.ordered(v)) for k, v in data.items())
        else:
            return data

    def compate_requests(self, file1,file2):
        list_urls1 = []
        list_urls2 = []
        with open(file1, 'r') as fl1:
            list_urls1 = fl1.readlines()
        with open(file2, 'r') as fl2:
            list_urls2 = fl2.readlines()
        counter = min(len(list_urls1),len(list_urls2))
        for i in range(counter):
            data1 = self.get_url(list_urls1[i])
            data2 = self.get_url(list_urls2[i])
            if (self.ordered(data1) == self.ordered(data2)):
                print("%s equals %s" %(list_urls1[i].strip(), list_urls2[i].strip()))
            else:
                print("%s is not equal to %s" %(list_urls1[i].strip(), list_urls2[i].strip()))
        if len(list_urls1) > len(list_urls2):
            print("Following urls are not present in File2:\n %s" %list_urls1[counter::])
        else:
            print("Following urls are not present in File1:\n %s" %list_urls2[counter::])

obj = cmphttpres()
f1 = os.getcwd()+"/JsonFile1.txt"
f2 = os.getcwd()+"/JsonFile2.txt"
obj.compate_requests(f1, f2)