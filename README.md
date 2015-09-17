# pandoc-chem-struct: A pandoc filter for easier, more legible chemical structures

pandoc-chem-struct is a little [pandoc][] filter that converts simple chemical structures into the
proper formatting. In principle, the markdown is easier to read and longer structures are much
easier to type. The syntax is loosely based on the (infinitely more powerful) [mhchem][] LaTeX
package.

## Installation

Does assume that XeTeX is being used (required for unicode characters). Could be made to work with
strict LaTeX with minor modifications.

## Usage

Within a pandoc markdown document, chemical structures are written as `s:{formula}`. Numbers
are automatically subscripted. Charges at the end of the formula are superscripted. If the species
is multiply charged, this can be indicated with `^`.

For example:
- `s:{CH3CH2OH}` → `CH~3~CH~2~OH`
- `s:{NH4+}` → `NH~4~^+^`
- `s:{SO3^2-}` → `SO~3~^2−^`

[pandoc]: http://pandoc.org
[mhchem]: https://www.ctan.org/pkg/mhchem?lang=en