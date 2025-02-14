export const speedToDelay = (speed: number): number => {
    return Math.round(201 - (speed * 2));
};

export function shuffleArray<T>(array: T[]): T[] {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

export function deepCopy<T>(obj: T): T {
    return JSON.parse(JSON.stringify(obj));
}

export function sudokuStringToSudokuGrid(sudokuString: string): number[][] {
    const result: number[][] = [];
    let idx: number = 0;
    for (let r = 0; r < 9; r++) {
        const row: number[] = []
        for (let c = 0; c < 9; c++) {
            if (idx >= sudokuString.length) break;
            const char = sudokuString[idx++];
            row.push(char !== "." ? Number(char) : 0);
        }
        result.push(row);
    }
    return result
}