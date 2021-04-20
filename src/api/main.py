from fastapi import FastAPI, Form, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from src.utils.tasks import (
    start_subscription,
    stop_subscription,
    subscription_confirmation,
)

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")


class FormData(BaseModel):
    email: str


@app.post("/confirmation/subscribe")
def subscribe(request: Request, email: str = Form("body")):
    return RedirectResponse(
        f"/confirmation/subscribe/{email}", status_code=status.HTTP_303_SEE_OTHER
    )


@app.get("/confirmation/{confirmation_type}/{email}")
async def read_item(request: Request, confirmation_type: str, email: str):
    """
    Takes the email - and calls stop_subscription
    """
    if confirmation_type == "subscribe":
        start_subscription(email)
        message = "You have been successfully subscribed. Check your email and click the confirmation link."
    elif confirmation_type == "unsubscribe":
        stop_subscription(email)
        message = "You have been successfully unsubscribed."
    elif confirmation_type == "confirm":
        subscription_confirmation(email)
        message = "You have been successfully confirmed. Your first email will arrive tomorrow."
    return templates.TemplateResponse(
        "confirmation.html",
        {
            "request": request,
            "confirmation_type": confirmation_type,
            "message": message,
        },
    )


@app.get("/donate")
async def donate(request: Request):
    return templates.TemplateResponse("donate.html", {"request": request})


@app.get("/")
async def landing_page(request: Request):
    return templates.TemplateResponse("landing_page.html", {"request": request})
