from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import models, database, schemas
from ..methods import teamMember
from sqlalchemy.orm import Session
from typing import List

get_db = database.get_db

router = APIRouter(
    prefix = '/teamMember',
    tags = ['Team Member']
)

@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.ShowTeamMember
)
def create(request:schemas.TeamMember, db:Session = Depends(get_db)):
    return teamMember.create(request, db)


@router.get(
    '/',
    response_model=List[schemas.ShowTeamMember]
)
def all(db:Session = Depends(get_db)):
    return teamMember.get_all(db)


@router.delete(
    '/',
    status_code=status.HTTP_204_NO_CONTENT
)
def destroy(id:int, db:Session = Depends(get_db)):
    return teamMember.destroy(id, db)


@router.get(
    '/{id}',
    response_model=schemas.ShowTeamMember
)
def show(id:int, db:Session = Depends(get_db)):
    return teamMember.show(id, db)


@router.put(
    '/{id}',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=schemas.UpdateMember
)
def update(id:int, request:schemas.UpdateMember, db:Session = Depends(get_db)):
    return teamMember.update(id, request, db)