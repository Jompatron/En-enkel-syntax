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
    readAtom(q)
    if q.peek() == ".":
        q.dequeue()
    else:
        readLETTER(q)
        readLetter(q)

def readAtom(q):
    readLETTER(q)
    readLetter(q)
    readNum(q)

def readLETTER(q):
    word = q.dequeue()
    if word == "[A-Z]": #reguljärt uttryck?
        return
    raise Grammatikfel("Fel stor bokstav: " + word)

def readLetter(q):
    word = q.dequeue()
    if word == "[a-z]": #reguljärt uttryck?
        return
    raise Grammatikfel("Fel liten bokstav: " + word)

def readNum(q):
    word = q.dequeue()
    if word == "[0-9]":  #reguljärt uttryck?
        return
    raise Grammatikfel("Fel siffra: " + word)

# Lägger in molekyl"delarna" i kön
def storeMolekyl(molekyl):
    q = LinkedQ()
    string = molekyl

    for letter in string:
        print(letter) # Bara för att kunna kolla i framtiden
        q.enqueue(letter)
    q.enqueue(".")
    return q


def kollaGrammatiken(molekyl):
    q = storeMolekyl(molekyl)

    try:
        readMolekyl(q)
        return "Följer syntaxen!"
    except Grammatikfel as fel:
        return str(fel) + " före " + str(q)


def main():
    q = LinkedQ()
    molekyl = input("Skriv en molekyl: ")
    resultat = kollaGrammatiken(molekyl)
    print(resultat)

if __name__ == '__main__':
    main()