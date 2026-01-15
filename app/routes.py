from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from rag.graph import build_graph

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

rag_app = build_graph()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@router.post("/ask", response_class=HTMLResponse)
def ask(request: Request, query: str = Form(...)):
    result = rag_app.invoke({"question": query})

    return templates.TemplateResponse(
    "index.html",
    {
        "request": request,
        "query": query,
        "answer": result["answer"],
        "context": [d.page_content for d in result["docs"]],
        "confidence": result["confidence"]
    }
)

