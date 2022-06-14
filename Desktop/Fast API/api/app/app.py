from fastapi import FastAPI
app=FastAPI()


# minimal app-get request
@app.get("/",tags=['Root'])
async def root() ->dict:
    return {"day":"Monday"}

@app.get('/todo',tags=['todos'])
async def get_todo() -> dict:
    return{"data":todos}


@app.post("/todo",tags=["todos"])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return{
        "data":"A todo has been added"
    }



todos=[
    {
        "id":"1",
        "Activity":" I am starting at 7:00"
    },

    {
        "id":"2",
        "Activity":"Lunch"
    }

] 