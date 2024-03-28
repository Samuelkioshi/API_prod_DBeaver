from sqlalchemy.orm import Session


from db.models import Usuarios

class UsuarioRepository:
    @staticmethod

    def find_all(db: Session) -> list[Usuarios]:
        return db.query(Usuarios).all()

    @staticmethod
    def save(db: Session, usuario: Usuarios) -> Usuarios:
        if usuario.id:

            db.merge(usuario)
        else:
            db.add(usuario)

        db.commit()
        return usuario


    @staticmethod

    def find_by_id(db: Session, id: int) -> Usuarios:

        return db.query(Usuarios).filter(Usuarios.id == id).first()
 

    @staticmethod

    def find_by_nome_item(db: Session, nome_item: str) -> Usuarios:

        return db.query(Usuarios).filter(Usuarios.item == nome_item).first()


    @staticmethod

    def exists_by_id(db: Session, id: int) -> bool:

        return db.query(Usuarios).filter(Usuarios.id == id).first() is not None


    @staticmethod

    def delete_by_id(db: Session, id: int) -> None:

        usuario = db.query(Usuarios).filter(Usuarios.id == id).first()

        if usuario is not None:
            db.delete(usuario)

            db.commit()