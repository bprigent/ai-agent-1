import uvicorn

if __name__ == "__main__":
    print("Starting the API...")
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True) 