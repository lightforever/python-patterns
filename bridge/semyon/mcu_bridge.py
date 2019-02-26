from abc import ABC, abstractmethod


class Circuit(ABC):
    """
    Реализация
    """
    @abstractmethod
    def apply_current(self) -> str:
        pass


class MCU:
    """
    Абстракция
    """

    def __init__(self, circuit: Circuit):
        self.circuit = circuit

    def blink_led(self) -> str:

        return self.circuit.apply_current()


class BJTCircuit(Circuit):

    def apply_current(self):

        return 'Voltage-current converter applied. BJT is opened. LED is on.'


class MOSFETCircuit(Circuit):

    def apply_current(self):

        return 'Voltage applied to the gate pin. MOSFET is opened. LED is on.'


if __name__ == '__main__':
    bjt_led = MCU(BJTCircuit())
    print(bjt_led.blink_led())

    mosfet_led = MCU(MOSFETCircuit())
    print(mosfet_led.blink_led())