from repository import IRepository, Repository

class DBMS:
    def __init__(self, repository: IRepository):
        if not isinstance(repository, IRepository):
            raise TypeError("Repository must implement IRepository")
        self.repository = repository  
        
    def lookup(self, id=None, name=None):
        if id is not None:
            return self.repository.find_by_id(id)
        else:
            return self.repository.find_by_name(name)
            
    def add(self, id, name, age, gender):
        return self.repository.add_field(id, name, age, gender)