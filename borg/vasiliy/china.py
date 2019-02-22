from .atmosphere import Atmosphere

__all__ = ['China']


class China:
    def __init__(self):
        self.atmosphere = Atmosphere()
        self.carbon_dioxide_production = 300

    def produce_carbon_dioxide(self):
        self.atmosphere.carbon_dioxide_level += self.carbon_dioxide_production
