import string
import random
from typing import List
from abc import ABC, abstractmethod


def generar_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SoporteTiquete:

    def __init__(self, cliente, tema):
        self.id = generar_id()
        self.cliente = cliente
        self.tema = tema


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def crear_orden(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def crear_orden(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        return list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def crear_orden(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def crear_orden(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleStrategy(TicketOrderingStrategy):
    def crear_orden(self, list: List[SoporteTiquete]) -> List[SoporteTiquete]:
        return []


class clienteSoporte:

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def crear_tiquete(self, cliente, tema):
        self.tickets.append(SoporteTiquete(cliente, tema))

    def proceso_tiquetes(self):
        # create the ordered list
        ticket_list = self.processing_strategy.crear_orden(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SoporteTiquete):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"cliente: {ticket.cliente}")
        print(f"tema: {ticket.tema}")
        print("==================================")


# create the application
app = clienteSoporte(RandomOrderingStrategy())

# register a few tickets
app.crear_tiquete("John Smith", "My computer makes strange sounds!")
app.crear_tiquete("Linus Sebastian", "I can't upload any videos, please help.")
app.crear_tiquete("Arjan Egges", "VSCode doesn't automatically solve my bugs.")
app.crear_tiquete("Joseph David", "Ha debugeado debugeado esto")

# process the tickets
app.proceso_tiquetes()
