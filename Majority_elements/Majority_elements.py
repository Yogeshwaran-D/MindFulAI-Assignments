from fastapi import FastAPI

app=FastAPI()

class MajorityElement:
    @staticmethod
    def majorityElement(arr):
        arr=[int(ele) for ele in arr.split(",")]
        count={}
        maxEle=[0,0]
        for ele in arr:
            count[ele]=count.get(ele,0)+1
            if count.get(ele) > maxEle[1]:
                maxEle=[ele,count.get(ele)]
        return f"{maxEle[0]}"

@app.get("/{arr}")
async def maxElement(arr:str):
    return MajorityElement.majorityElement(arr)