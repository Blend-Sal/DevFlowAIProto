from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from model import TaskInput
from ai import prioritize_tasks

app = FastAPI(title="DevFlowAI")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

TASKS = []

DEFAULT_WEIGHTS = {
    "deadline": 0.4,
    "importance": 0.3,
    "risk": 0.2,
    "effort": -0.1
}


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": None}
    )


@app.post("/add-task", response_class=HTMLResponse)
async def add_task(request: Request):
    form = await request.form()

    task = TaskInput(
        title=form.get("title"),
        description=form.get("description"),
        deadline=form.get("deadline"),
        importance=int(form.get("importance")),
        effort=int(form.get("effort"))
    )

    TASKS.append(task)

    prioritized = prioritize_tasks(TASKS, DEFAULT_WEIGHTS)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": prioritized}
    )


@app.post("/load-demo", response_class=HTMLResponse)
def load_demo(request: Request):
    TASKS.clear()
    TASKS.extend([
        TaskInput(
            title="Fix login bug",
            description="Critical security bug causing login crash",
            deadline="2026-01-11",
            importance=5,
            effort=2
        ),
        TaskInput(
            title="API refactoring",
            description="Refactor and cleanup legacy code",
            deadline="2026-01-18",
            importance=3,
            effort=4
        ),
        TaskInput(
            title="Update documentation",
            description="Improve README and documentation",
            deadline="2026-01-25",
            importance=2,
            effort=1
        )
    ])

    prioritized = prioritize_tasks(TASKS, DEFAULT_WEIGHTS)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "tasks": prioritized}
    )
