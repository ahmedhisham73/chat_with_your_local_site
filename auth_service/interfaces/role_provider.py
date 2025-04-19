from abc import ABC, abstractmethod
from typing import List

class RoleProvider(ABC):
    @abstractmethod
    def get_roles(self, username: str) -> List[str]:
        pass


