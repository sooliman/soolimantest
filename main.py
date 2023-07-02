# example()^
# counts={"s":1,
#         'p':0
#         }
# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
print("s")