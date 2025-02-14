import React, { useEffect, useState } from "react";
import { generateSudoku } from "../utils/generateSudoku";
import { SudokuGrid } from "./SudokuGrid"; // Make sure the path is correct

const TestSudoku: React.FC = () => {
  const [sudokuGrid, setSudokuGrid] = useState<number[][] | null>(null);

  useEffect(() => {
    const grid = generateSudoku();
    setSudokuGrid(grid);
  }, []);

  return (
    <div>
      <h1>Generated Sudoku Grid</h1>
      {sudokuGrid ? (
        <SudokuGrid
          grid={sudokuGrid}
          initialGrid={sudokuGrid}
          isPlayable={false} // Make it non-playable for testing purposes
        />
      ) : (
        <div>Loading...</div>
      )}
    </div>
  );
};

export default TestSudoku;
