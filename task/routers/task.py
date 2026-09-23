from fastapi import APIRouter, HTTPException, status
from models.task import TaskInsert, Task

task_router = APIRouter()

datas = [
  { "id": 0, "text": "Visit Kafka Museum", "done": True },
  { "id": 1, "text": "Watch a puppet show", "done": False },
  { "id": 2, "text": "Lennon Wall pic", "done": False },
]

tasks = [Task(**task) for task in datas]

# 전체조회, 수정(put, patch), 삭제, 추가

@task_router.get("", response_model=list[Task])
async def get_tasks():
    return tasks


# client 수정 done
# client 수정 text
@task_router.put("/{id}", response_model=Task)
async def put_tasks(id:int, update_task:Task):
    for task in tasks:
        if task.id == id:
            task.done = update_task.done
            task.text = update_task.text
            return task

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="해당하는 task 가 없습니다.")


@task_router.delete("/{id}", response_model=list[Task])
async def delete_tasks(id:int):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            return tasks

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="해당하는 task 가 없습니다.")


@task_router.post("", response_model=Task)
async def post_tasks(data:TaskInsert):
    new_id = max(t.id for t in tasks) + 1
    task = Task(id=new_id, text=data.text, done=data.done)
    tasks.append(task)
    return task