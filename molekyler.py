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


class Grammatikfel(Exception):
    pass



def readMolekyl(q):
    readAtom(q)
    if q.peek() == ".":
        q.dequeue()
    elif q.peek() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if q.peek() == "0":
            q.dequeue()
            raise Grammatikfel("För litet tal vid radslut")
        elif q.peek() == "1":
            first = q.dequeue()
            second = q.peek()
            if second in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                while q.peek() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    readNum(q)
            else:
                raise Grammatikfel("För litet tal vid radslutet")
    else:
        readMolekyl(q)


def readAtom(q):
    readLETTER(q)
    if q.peek() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        readLetter(q)



def readLETTER(q):
    word = q.peek()
    if word in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        q.dequeue()
        return
    raise Grammatikfel("Saknad stor bokstav vid radslutet")


def readLetter(q):
    word = q.peek()
    if word in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        q.dequeue()
        return
    raise Grammatikfel("Fel: Ska följa med liten bokstav: ")


def readNum(q):
    word = q.dequeue()
    if word in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return
    raise Grammatikfel("För litet tal vid radslutet")


def storeMolekyl(molekyl):
    q = LinkedQ()

    for letter in molekyl:

        q.enqueue(letter)
    q.enqueue(".")
    return q


def kollaGrammatiken(molekyl):
    q = storeMolekyl(molekyl)

    try:
        readMolekyl(q)
        return print("Formeln är syntaktiskt korrekt")
    except Grammatikfel as fel:
        if str(fel) in ["Saknad stor bokstav vid radslutet"]:
            print(fel, molekyl)
        else:
            print(fel)


def main():
    q = LinkedQ()
    molekyl = input()
    while molekyl != "#":
        resultat = kollaGrammatiken(molekyl)
        molekyl = input()


if __name__ == '__main__':
    main()