"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.isValidPlacement = isValidPlacement;
exports.sudokuStringToSudokuGrid = sudokuStringToSudokuGrid;
exports.printSudokuGrid = printSudokuGrid;
function isValidPlacement(sudokuGrid, row, col, num) {
    if (sudokuGrid[row].includes(num)) {
        return false;
    }
    for (let i = 0; i < 9; i++) {
        if (sudokuGrid[i][col] == num) {
            return false;
        }
    }
    const startRow = Math.floor(row / 3) * 3;
    const startCol = Math.floor(col / 3) * 3;
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (sudokuGrid[startRow + i][startCol + j] === num) {
                return false;
            }
        }
    }
    return true;
}
function sudokuStringToSudokuGrid(sudokuString) {
    let result = [];
    let idx = 0;
    for (let r = 0; r < 9; r++) {
        let row = [];
        for (let c = 0; c < 9; c++) {
            if (idx >= sudokuString.length)
                break;
            let char = sudokuString[idx++];
            row.push(char !== "." ? Number(char) : 0);
        }
        result.push(row);
    }
    return result;
}
function printSudokuGrid(sudokuGrid) {
    for (const [i, row] of sudokuGrid.entries()) {
        const formattedRow = Array.from({ length: 3 }, (_, j) => row.slice(j * 3, j * 3 + 3)
            .map(num => num !== 0 ? num.toString() : '.')
            .join('')).join(' | ');
        console.log(formattedRow);
        if (i % 3 === 2 && i < 8) {
            console.log("-".repeat(15));
        }
    }
}
