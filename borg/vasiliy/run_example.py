from borg.vasiliy.china import China
from borg.vasiliy.usa import USA
from borg.vasiliy.russia import Russia
from borg.vasiliy.atmosphere import Atmosphere


if __name__ == '__main__':
    countries = [Russia(), USA(), China()]

    for i in range(2):
        for country in countries:
            country.produce_carbon_dioxide()

    a = Atmosphere()
    print(a.carbon_dioxide_level)
