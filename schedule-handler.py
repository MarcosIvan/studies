class Node:
    def __init__(self, element):
        self.title = str(element).split(": ")[0]
        self.start = str(str(element).split(": ")).split(" - ")[0].split("'")[3]
        self.end = str(element).split(" - ")[1]
        self.next = None
    
class Schedule:
    def __init__(self):
        self.head = None
    
    def append(self, element):
        new_node = Node(element)

        if self.head is None or new_node.start < self.head.start:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next is not None and current.next.start < new_node.start:
            current = current.next

        new_node.next = current.next
        current.next = new_node
    
    def search(self, start):
        node = self.head
        while node:
            if node.start == start:
                return node
            node = node.next

def scheduleHandler(schedule):
    newSchedule = Schedule()
    for i in schedule:
        newSchedule.append(i)
    
    if newSchedule.head is None:
        return "Sua agenda está vazia!"
    
    node = newSchedule.head

    while node.next:
        end1 = int(node.end.split("h")[0])+(int(node.end.split("h")[1])/60)
        start2 = int(node.next.start.split("h")[0])+(int(node.next.start.split("h")[1])/60)

        if start2 < end1:
            return f"Há conflitos na sua agenda: {node.title}: {node.start} - {node.end} // {node.next.title}: {node.next.start} - {node.next.end}. Por favor, ajuste!"
        
        node = node.next

    return "Não há conflitos na sua agenda! Pode seguir sua programação!"


teste1 = [
  "Reunião de Planejamento: 09h00 - 10h00",
  "1:1 com Gerente: 14h00 - 14h30",
  "Alinhamento com Marketing: 11h00 - 12h00",
  "Discussão de Produto: 11h30 - 12h30",
  "Revisão do Projeto: 09h30 - 10h30"
]
teste2 = [
  "Daily Standup: 08h30 - 08h45",
  "Planejamento da Sprint: 09h00 - 10h00",
  "Reunião de Design: 10h15 - 11h00",
  "Almoço com Cliente: 12h00 - 13h00",
  "Revisão Semanal: 15h00 - 16h00"
]
teste3 = []
response = scheduleHandler(teste1)
print(response)
response = scheduleHandler(teste2)
print(response)
response = scheduleHandler(teste3)
print(response)