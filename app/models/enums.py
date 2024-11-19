from enum import Enum

class AccountType(str, Enum):
    ORDINARY = "普通口座"
    CHECKING = "当座"
