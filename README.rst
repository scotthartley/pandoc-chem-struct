pandoc-chem-struct: A pandoc filter for easier, more legible chemical structures
================================================================================

pandoc-chem-struct is a little `pandoc <http://pandoc.org>`__ filter
that converts simple chemical structures into the proper formatting. In
principle, the markdown is easier to read and longer structures are much
easier to type. The syntax is loosely based on the (infinitely more
powerful) `mhchem <https://www.ctan.org/pkg/mhchem?lang=en>`__ LaTeX
package.

Installation
------------

Use as any other pandoc filter (i.e.,
``pandoc --filter pandoc-chem-struct``). For LaTeX (or pdf) output, must
have mhchem installed.

Usage
-----

Within a pandoc markdown document, chemical structures are written as
``s:{formula}``. Numbers are automatically subscripted. Charges at the
end of the formula are superscripted. If the species is multiply
charged, this can be indicated with ``^``.

When converting to non-LaTeX documents, result is simply: -
``s:{CH3CH2OH}`` → ``CH~3~CH~2~OH`` - ``s:{NH4+}`` → ``NH~4~^+^`` -
``s:{SO3^2-}`` → ``SO~3~^2−^``

When converting to LaTeX documents, chemical formulas are simply typeset
with mhchem. That is: - ``s:{CH3CH2OH}`` → ``\ce{CH3CH2OH}``

Obviously, this package must be loaded in the LaTeX preamble.
