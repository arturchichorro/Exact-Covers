"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const sudokuBacktracking_1 = require("./sudokuBacktracking");
const sudokuHelper_1 = require("./sudokuHelper");
const sudokuString = "2.6.51.7.5.87.6..94.......1.49..58..375.481..82.3.97.51..6..9....48.32..7.2.....3";
const sudokuGrid = (0, sudokuHelper_1.sudokuStringToSudokuGrid)(sudokuString);
(0, sudokuHelper_1.printSudokuGrid)(sudokuGrid);
(0, sudokuBacktracking_1.solveSudokuBacktracking)(sudokuGrid);
console.log("\n\n\n");
(0, sudokuHelper_1.printSudokuGrid)(sudokuGrid);
