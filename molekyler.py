import re
# Syntax:
#< molekyl >: := < atom > | < atom > < num >
#< atom >: := < LETTER > | < LETTER > < letter >
#< LETTER >: := A | B | C | ... | Z
#< letter >: := a | b | c | ... | z
#< num >: := 2 | 3 | 4 | ...


class LinkedQ:

    class Node:
        #Bestämmer vart de olika pekarna pekar
        def __init__(self, element, _next):
            self._next = _next
            self.element = element

    #Bestämmer ordningen på noderna
    def __init__(self):
        self._first = None
        self._last = None
        self.size = 0

    def __str__(self):
        return self._first.element

    #Returnerar storleken på den länkade listan
    def __len__(self):
        return self.size

    #Tar bort det element som är först i listan
    def dequeue(self):
        result = self._first.element
        self._first = self._first._next #ändrar pekaren till att nästa element blir det första
        self.size -= 1
        if self.isEmpty():
            self._last = None
        return result

    # Lägger till det element som varit först i listan sist istället
    def enqueue(self, element):
        new = self.Node(element, None)  # Skapar ny nod med element pekar på None
        if self.isEmpty():
            self._first = new  # om kön är tom blir nya noden första noden
        else:
            self._last._next = new  # om det finns i kön läggs noden till sist
        self._last = new
        self.size += 1

    #Kollar om kön är tom
    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if not self.isEmpty():
            return self._first.element
        else:
            return None

# Är det såhär man ska göra på punkt 3?
class Grammatikfel(Exception):
    pass

def readMolekyl(q):
    if q.size == 2:
        readLETTER(q)
        q.dequeue()

    elif q.size == 3:
        readLETTER(q)
        if q.peek() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            readLetter(q)

        elif q.peek() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            readNum(q)

    else:
        readLETTER(q)
        if q.peek() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            while q.peek() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                readNum(q)
            if q.peek() == ".":
                q.dequeue()
        else:
            readLetter(q)
            readNum(q)
            while q.peek() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                readNum(q)

            if q.peek() == ".":
                q.dequeue()


def readAtom(q):
    readLETTER(q)
    readLetter(q)
    readNum(q)


def readLETTER(q):
    word = q.dequeue()
    if word in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        return
    raise Grammatikfel("Saknad stor bokstav vid radslutet")

def readLetter(q):
    word = q.dequeue()
    if word in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        return
    raise Grammatikfel("Fel: Ska följa med liten bokstav: " + word)

def readNum(q):
    word = q.dequeue()
    if word in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:  #reguljärt uttryck?
        return
    raise Grammatikfel("För litet tal vid radslutet" + word)

# Lägger in molekyl"delarna" i kön
def storeMolekyl(molekyl):
    q = LinkedQ()

    for letter in molekyl:
        #print(letter) # Bara för att kunna kolla i framtiden
        q.enqueue(letter)
    q.enqueue(".")
    return q


def kollaGrammatiken(molekyl):
    q = storeMolekyl(molekyl)

    try:
        readMolekyl(q)
        return "Följer syntaxen!"
    except Grammatikfel as fel:
        return str(fel) + str(q)


def main():
    q = LinkedQ()
    molekyl = input()
    while molekyl != "#":
        resultat = kollaGrammatiken(molekyl)
        print(resultat + " " + molekyl)
        molekyl = input()


if __name__ == '__main__':
    main()