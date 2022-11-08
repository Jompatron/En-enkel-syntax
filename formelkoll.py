# Syntax:
#<formel>::= <mol> \n
#<mol>   ::= <group> | <group><mol>
#<group> ::= <atom> |<atom><num> | (<mol>) <num>
#<atom>  ::= <LETTER> | <LETTER><letter>
#<LETTER>::= A | B | C | ... | Z
#<letter>::= a | b | c | ... | z
#<num>   ::= 2 | 3 | 4 | ...

period = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si",
        "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni",
        "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo",
        "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba",
        "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
        "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po",
        "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf",
        "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn",
        "Fl", "Lv"]

small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def __add__(self, other):
        self.stack.append(other)
        self.size = self.size + 1

    def remove(self):
        last = self.stack[(len(self.stack))]
        self.stack.remove(len(self.stack))
        self.size = self.size - 1
        return last


class Grammatikfel(Exception):
    pass


def readFormel(q):
    if q.peek() == ".":
        q.dequeue()
    else:
        readGroup(q)


def readMolekyl(q):
    q.dequeue()
    readAtom(q)
    readGroup(q)


def readGroup(q):
    if q.peek() in big or small:
        readAtom(q)
    elif q.peek() == "(":
        readMolekyl(q)
    elif q.peek() in number:
        if q.peek() == "0":
            q.dequeue()
            raise Grammatikfel("För litet tal vid radslutet")
        elif q.peek() == "1":
            first = q.dequeue()
            second = q.peek()
            if second in number:
                while q.peek() in number:
                    readNum(q)
            else:
                raise Grammatikfel("För litet tal vid radslutet")
    else:
        readGroup(q)


def readAtom(q):
    if q.peek() in period:
        first = q.dequeue()
        if q.peek() in small:
            if first + q.peek() in period:
                readLetter(q)
            else:
                raise Grammatikfel("okänt grundämne")

    else:
        first = q.dequeue()
        if first + q.peek() in period:
            readLetter(q)
        elif first in small:
            raise Grammatikfel("Saknad stor bokstav vid radslutet")
        else:
            raise Grammatikfel("okänt grundämne")


#def readLETTER(q):
    #word = q.peek()
    #if word in big:
        #q.dequeue()
        #return
    #raise Grammatikfel("Saknad stor bokstav vid radslutet")


def readLetter(q):
    word = q.peek()
    if word in small:
        q.dequeue()
        return
    raise Grammatikfel("Fel: Ska följa med liten bokstav: ")


def readNum(q):
    word = q.dequeue()
    if word in number:
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
    molekyl = molekyl + "."

    try:
        readFormel(q)
        return "Formeln är syntaktiskt korrekt"
    except Grammatikfel as fel:
        if str(fel) == "Saknad stor bokstav vid radslutet":
            return str(fel) + " " + molekyl[:len(molekyl)-1]
        elif molekyl[1] in small:
            return str(fel) + " " + molekyl[3:len(molekyl)-1]
        else:
            return str(fel) + " " + molekyl[2:len(molekyl)-1]


def main():
    q = LinkedQ()
    molekyl = input()
    while molekyl != "#":
        resultat = kollaGrammatiken(molekyl)
        print(resultat)
        molekyl = input()


if __name__ == '__main__':
    main()