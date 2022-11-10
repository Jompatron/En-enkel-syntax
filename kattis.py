import string
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

    def store(self, other):
        self.stack.append(other)
        self.size = self.size + 1

    def remove(self):
        last = self.stack.pop()
        self.size = self.size - 1
        return last


class Grammatikfel(Exception):
    pass


def readMolekyl(q, z):
    readGroup(q, z)
    if q.peek() == ".":
        return
    elif q.peek() == ")":
        if z.size < 1:
            raise Grammatikfel("Felaktig gruppstart vid radslutet")
        else:
            return
    else:
        readMolekyl(q, z)


def readGroup(q, z):
    if q.peek() == ".":
        raise Grammatikfel("Felaktig gruppstart vid radslutet")
    elif q.peek() in number:
        raise Grammatikfel("Felaktig gruppstart vid radslutet")
    elif q.peek().isalpha():
        readAtom(q)
        if q.peek() == ".":
            return
        elif q.peek in number:
            readNum(q)
        else:
            return
    elif q.peek() == "(":
        z.store(q.dequeue())
        readMolekyl(q, z)
        if q.peek() != ")":
            raise Grammatikfel("Saknad högerparentes vid radslutet")
        if q.peek() == ".":
            raise Grammatikfel("Saknad siffra vid radslutet")
        else:
            z.remove()
            q.dequeue()
            if q.peek() == ".":
                raise Grammatikfel("Saknad siffra vid radslutet")
            readNum(q)
    else:
        raise Grammatikfel("Felaktig gruppstart vid radslutet")


def readAtom(q):
    if q.peek() in period:
        first = q.dequeue()
        if q.peek() in small:
            if first + q.peek() in period:
                readLetter(q)
                if q.peek() in number:
                    readNum(q)
            else:
                q.dequeue()
                raise Grammatikfel("Okänd atom vid radslutet ")
        elif q.peek() in number:
            readNum(q)
        else:
            return
    elif q.peek() in small:
        raise Grammatikfel("Saknad stor bokstav vid radslutet")
    else:
        first = q.dequeue()
        if first + q.peek() in period:
            readLetter(q)
        elif first in small:
            raise Grammatikfel("Saknad stor bokstav vid radslutet")
        elif q.peek() in small:
            q.dequeue()
            raise Grammatikfel("Okänd atom vid radslutet")
        else:
            raise Grammatikfel("Okänd atom vid radslutet")


def readLetter(q):
    word = q.peek()
    if word in small:
        q.dequeue()
        return
    raise Grammatikfel("Fel: Ska följa med liten bokstav: ")


def readNum(q):
    if q.peek() == "0":
        q.dequeue()
        raise Grammatikfel("För litet tal vid radslutet")
    elif q.peek() == "1":
        first = q.dequeue()
        second = q.peek()
        if second in number:
            num = ""
            while q.peek() in number:
                num = num + q.dequeue()
            return
        else:
            raise Grammatikfel("För litet tal vid radslutet")
    elif q.peek() in number:
        while q.peek() in number:
            q.dequeue()
        return
    raise Grammatikfel("Saknad siffra vid radslutet")


def storeMolekyl(molekyl):
    q = LinkedQ()

    for letter in molekyl:

        q.enqueue(letter)
    return q


def kollaGrammatiken(molekyl):
    molekyl = molekyl + "."
    q = storeMolekyl(molekyl)
    z = Stack()
    try:
        readMolekyl(q, z)
        return "Formeln är syntaktiskt korrekt"
    except Grammatikfel as fel:
        return str(fel) + printRest(q)


def printRest(q):
    rest = " "
    while not q.isEmpty():
        sak = q.dequeue()
        if sak != ".":
            rest = rest + sak
    return rest


def main():
    q = LinkedQ()
    molekyl = input()
    while molekyl != "#":
        resultat = kollaGrammatiken(molekyl)
        print(resultat)
        molekyl = input()


if __name__ == '__main__':
    main()