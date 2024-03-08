from abc import ABC, abstractmethod

class BusinessUnitCreator(ABC):
    def __init__(self, name):
        self.name = name
        # get user confirmation here
        # add more configuration based on what and what not to create
        self.run()

    def setup_database(self):
        print(f"Setting up database for {self.name}...")
        # Call Snowflake method here

    def setup_warehouse(self):
        print(f"Setting up warehouse for {self.name}...")
        # Call Snowflake method here

    # @abstractmethod
    def setup_warehouse_access_roles(self):
        print(f"Setting up warehouse access roles for {self.name}...")
        pass

    # @abstractmethod
    def setup_database_access_roles(self):
        print(f"Setting up database access roles for {self.name}...")
        pass

    # @abstractmethod
    def setup_functional_roles(self):
        print(f"Setting up functional roles for {self.name}...")
        pass

    def run(self):
        self.setup_database()
        self.setup_warehouse()
        self.setup_warehouse_access_roles()
        self.setup_database_access_roles()
        self.setup_functional_roles()