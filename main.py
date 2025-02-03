"""General operations"""
from fastapi import FastAPI

app = FastAPI(debug=True)

@app.post("/process")
def summing():
    """This method is for sum"""
    return 1+2

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)    
    