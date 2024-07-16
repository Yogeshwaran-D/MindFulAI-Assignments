from fastapi import FastAPI

app=FastAPI()

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def response(self,arr):
        self.arr=sorted([int(ele) for ele in arr.split(",")])
        asc=self.ascending()
        des=self.descending()
        return  f"Ascending : {asc} Descending : {des}"
    def ascending(self):
        self.asc_head=None
        temp=None
        for index in range(len(self.arr)):
            if self.asc_head == None:
                self.asc_head=Node(self.arr[index])
                temp=self.asc_head
            else:
                temp.next=Node(self.arr[index])
                temp=temp.next
        asc_list=""
        temp=self.asc_head
        while temp:
            asc_list+=f"{temp.val} ->"
            temp=temp.next
        return asc_list
    def descending(self):
        self.des_head=None
        temp=None
        for index in range(len(self.arr)-1,-1,-1):
            if self.des_head == None:
                self.des_head=Node(self.arr[index])
                temp=self.des_head
            else:
                temp.next=Node(self.arr[index])
                temp=temp.next
        des_list=""
        temp=self.des_head
        while temp:
            des_list+=f"{temp.val} ->"
            temp=temp.next
        return des_list

@app.get("/{arr}")
async def createList(arr:str):
    ll=LinkedList()
    res=ll.response(arr)
    return res