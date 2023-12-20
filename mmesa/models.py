from mmesa import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Client(db.Model):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    street_address: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    city_address: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    state_address: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    email: Mapped[str] = mapped_column(String)
    def __init__(self, name, street_address, city_address, state_address, email) -> None:
        self.name = name
        self.street_address = street_address
        self.city_address = city_address
        self.state_address = state_address
        self.email = email

class Equipament(db.Model):
    __tablename__ = "equipamentos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    model: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    manufacturer: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    equipment_type_id: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    problem_description: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    input_date: Mapped[str] = mapped_column(String)
    output_date: Mapped[str] = mapped_column(String)
    repair_description: Mapped[str] = mapped_column(String, unique=False, nullable=False)
    owner: Mapped[int] = mapped_column(Integer, ForeignKey('client.id'), nullable=False)


    def __init__(self, name, model, manufacturer, equipment_type_id, problem_description, input_date, output_date, repair_description) -> None:
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.equipment_type_id = equipment_type_id
        self.problem_description = problem_description
        self.input_date = input_date
        self.output_date = output_date
        self.repair_description = repair_description

class EquipmentType(db.Model):
    __tablename__ = "Tipo_equipamentos"

    id :  Mapped[int]= mapped_column(Integer, primary_key=True)
    type_name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description:  Mapped[str] = mapped_column(String, nullable=False, unique=True)
  
    def __init__(self, type_name, description) -> None:
        self.type_name = type_name
        self.description = description

