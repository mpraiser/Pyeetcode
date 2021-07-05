from enum import Enum
from typing import List, Dict, Tuple


numbers = [chr(i) for i in range(ord('0'), ord('9')+1)]
letters = [chr(i) for i in range(ord('A'), ord('Z')+1)]

atoms = set([
    "H", "He", 
    "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe",
    "Cs", "Ba", 
    "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu",
    "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
    "Fr", "Ra",
    "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr",
    "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"])


class Type(Enum):
    number = "number"
    letter = "letter"
    left_bracket = "left_bracket"
    right_bracket = "right bracket"
    atom = "atom"
    count = "count"


def check(c: str) -> Type:
    if c == '(':
        return Type.left_bracket
    elif c == ')':
        return Type.right_bracket
    elif c in numbers:
        return Type.number
    elif c.upper() in letters:
        return Type.letter


def tokenize(formula: str) -> Tuple[Type, str]:
    last_type = None
    atom = ""
    count = ""

    i = 0
    while i < len(formula):
        this_type = check(formula[i])

        if last_type == Type.number and this_type != last_type:
            yield (Type.count, int(count))
            count = ""

        if this_type == Type.left_bracket:
            yield (Type.left_bracket, formula[i])
        elif this_type == Type.right_bracket:
            yield (Type.right_bracket, formula[i])
        elif this_type == Type.letter:
            atom += formula[i]
            if atom + formula[i+1] not in atoms and atom in atoms:
                # greedy to read 1 more char
                yield (Type.atom, atom)
                atom = ""
        elif this_type == Type.number:
            count += formula[i]

        last_type = this_type
        i += 1
    
    if count != "":
        yield (Type.count, int(count))


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counters = [dict()]  # stack of counter
        formula = "(" + formula + ")"
        tokens = list(tokenize(formula))

        i = 0
        while i < len(tokens):
            (t, word) = tokens[i]

            if t == Type.left_bracket:
                counters.append(dict())

            elif t == Type.right_bracket:
                if i + 1 < len(tokens) and tokens[i+1][0] == Type.count:
                    mul = tokens[i+1][1]
                    i += 1
                else:
                    mul = 1
                counter = counters.pop()
                for atom in counter:
                    if atom not in counters[-1]:
                        counters[-1][atom] = counter[atom] * mul
                    else:
                        counters[-1][atom] += counter[atom] * mul

            elif t == Type.atom:
                if tokens[i+1][0] == Type.count:
                    count = tokens[i+1][1]
                    i += 1
                else:
                    count = 1
                if word not in counters[-1]:
                    counters[-1][word] = count
                else:
                    counters[-1][word] += count

            i += 1

        base_counter = counters[0]
        atoms = list(base_counter.keys())
        atoms.sort()
        result = ""
        for atom in atoms:
            result += atom
            count = base_counter[atom]
            if count != 1:
                result += str(base_counter[atom])
        return result



cases = ["H20", "Mg(OH)2", "K4(ON(SO3)2)2", "Be32", "(ScTh13)16Tb22C18Fl34Ag14(At41Bk4NpEsTc27Am20)3"]


for case in cases:
    # print(case)
    # for (t, word) in tokenize(case):
    #     print(t, word)
    ans = Solution().countOfAtoms(case)
    print(ans)


# ans = Solution().countOfAtoms("(ScTh13)16Tb22C18Fl34Ag14(At41Bk4NpEsTc27Am20)3")
# print(ans)