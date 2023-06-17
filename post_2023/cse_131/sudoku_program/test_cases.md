# Sudoku Program Test Cases

## Requirement Test Cases
| Name | Input | Output |
| --- | --- | --- |
| Reversed Coordinates | 2B | What value goes in 2B? |
| Already in row | 2B, 2| The Number 2 is already in this row. |
| Lowercase Coordinates | b2 | What value goes in B2? |
| Already in column | b2, 5 | The number, 5 is already in this column. |
| Already in box | G3, 9 | The number, 9 is already in this box. |
| All correct inputs | B8, 8 | Displays updated board. |
| Quit | Q | Your game is saved. Thank you for playing. |

---

## Boundary Condition Test Cases
| Name | Input | Output |
| --- | --- | --- |
| Negative | C2, -1 | The value must be between 1 and 9. |
| Zero | C2, 0 | The value must be between 1 and 9. |
| 1 too high | C2, 10 | The value must be between 1 and 9. |
| Exactly 1 | C2, 1 | Displays updated board. |
| Exactly 9 | B2, 9 | Displays updated board. |

---

## Error State Test Cases
| Name | Input | Output |
| --- | --- | --- |
| > 2 char | 10gj | Can't be more than two characters long & Invalid Coordinate |
| 2 letters| gg | Invalid Coordinate |
| 2 numbers| 55 | Invalid Coordinate |
| 1 number | 1  | Invalid Coordinate |
