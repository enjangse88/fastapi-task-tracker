from fastapi import FastAPI , HTTPException

app = FastAPI()

tasks = []

@app.post("/tasks/")
def create_task(task: dict):
    tasks.append(task)
    return task

@app.get("/tasks/")
def get_all_tasks():
    return tasks 

@app.get("/tasks/{task_id}/")
def update_task(task_id: int, updated_task: dict):
  if task_id < 0 or task_id >= len(tasks):
     raise HTTPException(status_code=404, detail="Task not found")
  tasks[task_id].update(updated_task)
  return tasks[task_id]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
   if task_id < 0 or task_id >= len(tasks):
      raise HTTPException(status_code=404, detail="Task not found")
   delete_task = tasks.pop(task_id)
   return {"message":"Task delete succesfully", "deleted_task": deleted_task}