from imp import reload
import uvicorn

if __name__=="main":
    uvicorn.run("app.app:app",host="127.0.0.1",port=8000,reload=True)



