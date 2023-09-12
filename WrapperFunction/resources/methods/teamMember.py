from sqlalchemy.orm import Session
from .. import models, schemas, hashing
from fastapi import HTTPException, status



def get_project_id(project_name:str, db:Session):
    project_id = db.query(models.Project).filter(models.Project.name == project_name)
    
    if not project_id.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Please first create the project and then assign it to a member.'
        )
    
    return project_id.first().id


def create(request:schemas.TeamMember, db:Session):

    project_id = get_project_id(request.project_name, db)

    teamMember = models.TeamMember(
        name = request.name,
        email = request.email,
        role = request.role,
        password = hashing.hash(request.password),
        project_id = project_id
    )

    db.add(teamMember)
    db.commit()
    db.refresh(teamMember)

    return teamMember


def destroy(id:int, db:Session):
    teamMember = db.query(models.TeamMember).filter(models.TeamMember.id == id)
    data = teamMember.first()

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail = f'Member with id {id} is not part of the organization'
        )

    teamMember.delete(synchronize_session = False)
    db.commit()

    return 'Done'


def get_all(db:Session):
    members = db.query(models.TeamMember).all()

    return members


def show(id:int, db:Session):
    member = db.query(models.TeamMember).filter(models.TeamMember.id == id).first()

    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Member with id {id} is not part of the organization.'
        )
    
    return member


def update(id:int, request:schemas.UpdateMember, db:Session):
    member = db.query(models.TeamMember).filter(models.TeamMember.id == id)

    project_id = get_project_id(request.project_name, db)
    
    if not member.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Member with id {id} is not part of the organization.'
        )
    
    data = {
        'id': id,
        'name': request.name,
        'email': request.email,
        'role': request.role,
        'project_id': project_id
    }
    
    member.update(data)
    db.commit()
    return request