"""Pandoc filter to format simple chemical structures.

Structures specified as in s:{CH3CH2O-}, s:{SO4^2-}
are converted to formatted structures such as CH~3~CH~2~OH^-^,
SO~4~^2−^. For LaTeX-based conversions, the mhchem package is used.

"""

from pandocfilters import toJSONFilter, Str, Subscript, Superscript, RawInline
import re

# Pattern for structures in md.
ID_PAT = re.compile('(s:\{[^\s\}]*\})')
# Pattern to separate formula from "s:{}" label.
STRUCT_PAT = re.compile('s:\{([^\s\}]*)\}')
# Used to identify charges at end of formula.
CHARGE_PAT = re.compile('(\w*)\^?([0-9]*[-–−+])')


def chem_struct (key, val, fmt, meta):
    if key == 'Str' and ID_PAT.search(val):

        new_val = []
        for s in ID_PAT.split(val):
            if STRUCT_PAT.match(s):
                clean_s = STRUCT_PAT.match(s).groups()[0]  # Remove "s:{}" tags

                if fmt in ['latex','pdf']: # Use mhchem package for latex
                    new_val += [RawInline(fmt, "\ce{" + clean_s + "}")]

                elif fmt == 'beamer':
                    new_val += [RawInline('latex', "\ce{" + clean_s + "}")]

                else:
                    if CHARGE_PAT.match(clean_s):
                        formula, charge = CHARGE_PAT.match(clean_s).groups()
                        # Replace hyphen with minus sign
                        charge = charge.replace('-', '−')
                    else:
                        formula, charge = clean_s, None

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

                    new_val += formatted_formula + formatted_charge
            else:
                new_val += [Str(s)]

        return new_val


def main():
    toJSONFilter(chem_struct)


if __name__ == '__main__':
    main()
