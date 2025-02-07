// import { solve, chooseRow } from "./algX";

// function _one_constraint(row: number, size: number): number {
//     return Math.floor(row / size);
// }

// function _row_constraint(row: number, size: number): number {
//     return size ** 2 + size * Math.floor(row / (size ** 2)) + (row % size);
// }

// function _col_constraint(row: number, size: number): number {
//     return 2 * (size ** 2) + (row % (size ** 2));
// }

// function _box_constraint(row: number, size: number): number {
//     const sqrtSize = Math.sqrt(size);
//     return Math.floor(3 * (size ** 2)
//         + Math.floor(row / (sqrtSize * size ** 2)) * (size * sqrtSize)
//         + (Math.floor(row / (sqrtSize * size)) % sqrtSize) * size
//         + (row % size));
// }

// function empty_sudoku_exact_cover(size: number = 9): number[][] {
//     const constraints = 4 * (size ** 2);
//     const rows = size ** 3;
//     const matrix: number[][] = [];

//     for (let r = 0; r < rows; r++) {
//         const row = new Array(constraints).fill(0);
//         const positions = [
//             _one_constraint(r, size),
//             _row_constraint(r, size),
//             _col_constraint(r, size),
//             _box_constraint(r, size)
//         ];
//         positions.forEach(pos => row[pos] = 1);
//         matrix.push([r + 1, ...row]);
//     }

//     return matrix;
// }

// function sudoku_string_to_exact_cover(sudokuString: string): [number[][], Set<number>] | undefined {
//     const size = Math.sqrt(sudokuString.length);
//     if (size !== 9) return;

//     const emptySudoku = empty_sudoku_exact_cover();
//     const partialSolution = new Set<number>();

//     for (let i = 0; i < sudokuString.length; i++) {
//         const char = sudokuString[i];
//         if (char === '.') continue;

//         const rowId = Math.floor(i / 9) * 81 + (i % 9) * 9 + parseInt(char, 10);
//         partialSolution.add(rowId);
//     }

//     let sudokuMatrix = [...emptySudoku];
//     for (const rowId of partialSolution) {
//         sudokuMatrix = chooseRow(sudokuMatrix, sudokuMatrix.findIndex(row => row[0] === rowId));
//     }

//     return [sudokuMatrix, partialSolution];
// }

// function sudoku_matrix_to_exact_cover(sudokuMatrix: number[][]): [number[][], Set<number>] | undefined {
//     if (sudokuMatrix.length !== 9 || sudokuMatrix[0].length !== 9) return;

//     const emptySudoku = empty_sudoku_exact_cover();
//     const partialSolution = new Set<number>();

//     for (let row = 0; row < 9; row++) {
//         for (let col = 0; col < 9; col++) {
//             const num = sudokuMatrix[row][col];
//             if (num === 0) continue;

//             const rowId = row * 81 + col * 9 + num;
//             partialSolution.add(rowId);
//         }
//     }

//     let sudokuExactCover = [...emptySudoku];
//     for (const rowId of partialSolution) {
//         sudokuExactCover = chooseRow(sudokuExactCover, sudokuExactCover.findIndex(row => row[0] === rowId));
//     }

//     return [sudokuExactCover, partialSolution];
// }

// function solve_sudoku_string_exact_cover(sudokuString: string): Set<number>[] {
//     const result = sudoku_string_to_exact_cover(sudokuString);
//     if (!result) return [];
//     const [sudokuMatrix, partialSolution] = result;
//     const solutions: Set<number>[] = [];
//     solve(sudokuMatrix, partialSolution, solutions);
//     return solutions;
// }

// function solve_sudoku_matrix_exact_cover(sudokuGrid: number[][]): Set<number>[] {
//     const result = sudoku_matrix_to_exact_cover(sudokuGrid);
//     if (!result) return [];
//     const [sudokuMatrix, partialSolution] = result;
//     const solutions: Set<number>[] = [];
//     solve(sudokuMatrix, partialSolution, solutions);
//     return solutions;
// }

// function translate_solution_to_sudoku(solutions: Set<number>[]): string[] {
//     return solutions.map(sol => {
//         const sortedSol = Array.from(sol).sort((a, b) => a - b);
//         let sudoString = "";
//         for (let i = 0; i < sortedSol.length; i++) {
//             sudoString += (i === 0) ? sortedSol[i].toString() : (sortedSol[i] % (9 * i) !== 0 ? (sortedSol[i] % (9 * i)).toString() : "9");
//         }
//         return sudoString;
//     });
// }

// console.log(translate_solution_to_sudoku(solve_sudoku_string_exact_cover(".4.6.8...56.9...2.19724.3...8..97..1.3.1.6..5..95.346....35.1.8....6..43.73..96.2")))