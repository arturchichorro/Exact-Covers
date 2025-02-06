export function isValidPlacement(sudokuGrid: number[][], row: number, col: number, num: number) {
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