from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class AccountType(Enum):
    savings_account = '普通口座'
    current_account = '当座'

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





def __repr__(self):
        return f'Task(id={self.id}, content={self.content}, is_done={self.is_done})'








from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum

class AccountType(str, enum.Enum):
    普通口座 = '普通口座'
    当座 = '当座'
    
class BankAccount(Base):
    __tablename__ = 'bank_account'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bank_name = Column(String, nullable=False)
    branch_name = Column(String, nullable=False)
    account_type = Column(Enum(AccountType), nullable=False)
    account_number = Column(String, nullable=False)
    account_holder = Column(String, nullable=False)

class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    name_kana = Column(String, nullable=False)
    address = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    mobile_phone = Column(String, nullable=False)
    mail = Column(String, nullable=True)
    bank_account_id = Column(Integer, ForeignKey("bank_accounts.id"), nullable=True)

    bank_account = relationship("BankAccount", back_populates="owners")


