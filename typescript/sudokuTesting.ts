import { solveSudokuBacktracking } from "./sudokuBacktracking";
import { sudokuStringToSudokuGrid, printSudokuGrid } from "./sudokuHelper";

const sudokuString = "2.6.51.7.5.87.6..94.......1.49..58..375.481..82.3.97.51..6..9....48.32..7.2.....3";
const sudokuGrid = sudokuStringToSudokuGrid(sudokuString);

printSudokuGrid(sudokuGrid);

solveSudokuBacktracking(sudokuGrid);

console.log("\n\n\n")
printSudokuGrid(sudokuGrid);