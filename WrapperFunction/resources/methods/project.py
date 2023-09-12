from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def create(request:schemas.Project, db:Session):
    new_project = models.Project(
        name = request.name,
        company = request.company,
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


def destroy(id:int, db:Session):
    project=db.query(models.Project).filter(models.Project.id == id)
    data = project.first()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project does not exist."
        )

    project.delete(synchronize_session=False)
    db.commit()

    return 'Done'


def show(id:int, db:Session):
    project = db.query(models.Project).filter(models.Project.id == id).first()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Project does not exist.'
        )
    
    return project


def get_all(db:Session):
    projects = db.query(models.Project).all()
    return projects


def update(id:int, request:schemas.Project, db:Session):
    project = db.query(models.Project).filter(models.Project.id == id)

    if not project.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Project does not exist.'
        )
    
    data = {
        'message': 'Successfully updated',
        'id': id,
        'name': request.name,
        'company': request.company,
    }

    project.update(request.dict())
    db.commit()
    return data