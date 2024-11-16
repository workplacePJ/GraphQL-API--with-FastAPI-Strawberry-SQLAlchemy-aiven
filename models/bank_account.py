from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class AccountType(Enum):
    Savings account = 'STARTED'
    Checking account = 'ACCEPTED'

class BankAccount(Base):
    __tablename__ = 'bank_account'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    bank_name = Column(String)
    branch_name = Column(String)
    account_type = Column(Enum(AccountType), nullable=False)
    account_number = Column(String)
    account_name = Column(String)
    account_name_kana = Column(String)
    
    owner_id = Column(Integer, ForeignKey('owner.id'))
    owner = relationship('Owner', back_populates='bank_accounts')




  
    scaler_id = Column(Integer, ForeignKey("scaler.id"))
    scaler = relationship("Scaler", back_populates="model", uselist=False)





    id = Column(Integer, primary_key=True)
    content = Column(String)
    is_done = Column(Boolean, default=False)

    def __repr__(self):
        return f'Task(id={self.id}, content={self.content}, is_done={self.is_done})'
