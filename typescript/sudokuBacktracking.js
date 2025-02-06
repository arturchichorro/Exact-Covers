"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.solveSudokuBacktracking = solveSudokuBacktracking;
const sudokuHelper_1 = require("./sudokuHelper");
function solveSudokuBacktracking(sudokuGrid) {
    function backtrack(sudokuGrid) {
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {
                if (sudokuGrid[row][col] === 0) {
                    for (let num = 1; num < 10; num++) {
                        if ((0, sudokuHelper_1.isValidPlacement)(sudokuGrid, row, col, num)) {
                            sudokuGrid[row][col] = num;
                            if (backtrack(sudokuGrid))
                                return true;
                            sudokuGrid[row][col] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    backtrack(sudokuGrid);
}
