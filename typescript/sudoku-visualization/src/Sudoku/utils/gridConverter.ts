export function partialSolutionToGrid(solution: Set<number>): number[][] {
    const grid = Array(9).fill(0).map(() => Array(9).fill(0));

    for (const rowId of solution) {
        const id = rowId - 1;
        const row = Math.floor(id / 81);
        const col = Math.floor((id % 81) / 9);
        const num = (id % 9) + 1;
        
        grid[row][col] = num;
    }

    return grid;
}