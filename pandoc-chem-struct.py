#! /usr/bin/env python3
"""Pandoc filter to format simple chemical structures.

Structures specified as in s:{CH3CH2O-}, s:{SO4^2-}
are converted to formatted structures such as CH~3~CH~2~OH^-^, 
SO~4~^2−^.

"""

from pandocfilters import toJSONFilter, Str, Subscript, Superscript
import re

# Pattern for structures in md.
ID_PAT = re.compile('(.*)s:\{(.*)\}(.*)')
# Used to identify charges at end of formula.
CHARGE_PAT = re.compile('(\w*)\^?([0-9]*[-–−+])')

def chem_struct (key, val, fmt, meta):
    if key == 'Str' and ID_PAT.match(val):
        # Store punctuation after formula in end.
        start, raw_formula, end = ID_PAT.match(val).groups()
        
        if CHARGE_PAT.match(raw_formula):
            formula, charge = CHARGE_PAT.match(raw_formula).groups()
            # Replace hyphen with minus sign
            charge = charge.replace('-', '−') 
        else:
            formula, charge = raw_formula, None

        formatted_formula = []

        for d in formula:
            if d.isdigit():
                formatted_formula.append(Subscript([Str(d)]))
            else:
                formatted_formula.append(Str(d))

        if charge:
            formatted_charge = [Superscript([Str(charge)])]
        else:
            formatted_charge = []

        formatted_start = [Str(start)]
        formatted_end = [Str(end)]

        return formatted_start + formatted_formula + formatted_charge \
               + formatted_end

if __name__ == '__main__':
    toJSONFilter(chem_struct)