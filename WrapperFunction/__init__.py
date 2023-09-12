from fastapi import FastAPI, Depends, HTTPException
from resources import schemas, models, database
from sqlalchemy.orm import Session
from resources.routers import project, teamMember, auth
import azure.functions as func

app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(project.router)
app.include_router(teamMember.router)
app.include_router(auth.router)