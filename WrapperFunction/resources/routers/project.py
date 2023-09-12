from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import models, database, schemas, oauth2
from ..methods import project
from sqlalchemy.orm import Session
from typing import List


get_db = database.get_db

router = APIRouter(
    prefix = '/project',
    tags = ['Projects']
)


@router.post(
        '/',
        status_code=status.HTTP_201_CREATED,
        response_model=schemas.Project
)
def create(
    request:schemas.Project,
    db:Session = Depends(get_db)
):
    return project.create(request, db)


@router.delete(
        '/{id}',
        status_code=status.HTTP_204_NO_CONTENT
)
def destroy(id:int, db:Session = Depends(get_db)):
    return project.destroy(id, db)


@router.get(
        '/{id}',
        response_model=schemas.ShowProject
)
def show(id:int, db:Session = Depends(get_db)):
    return project.show(id, db)


@router.get(
        '/'
)
def all(
    db: Session = Depends(get_db),
    get_current_user:schemas.TeamMember = Depends(oauth2.get_current_user)
):
    return project.get_all(db)


@router.put(
        '/{id}',
        status_code=status.HTTP_202_ACCEPTED
)
def update(id:int, request:schemas.Project, db:Session = Depends(get_db)):
    return project.update(id, request, db)