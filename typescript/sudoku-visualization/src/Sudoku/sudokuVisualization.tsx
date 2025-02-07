import React, { useState, useRef } from 'react';

interface SudokuProps {
    initialGrid: number[][];
}

const Sudoku: React.FC<SudokuProps> = ({ initialGrid }) => {
  const [grid, setGrid] = useState<number[][]>(JSON.parse(JSON.stringify(initialGrid)));
  const [solving, setSolving] = useState(false);
  const [delay, setDelay] = useState(100); // Default 100ms
  const solverRef = useRef<{ 
    pause: boolean; 
    abort: boolean;
    currentDelay: number;
  }>({ 
    pause: false, 
    abort: false,
    currentDelay: delay 
  });

  const isValidPlacement = (grid: number[][], row: number, col: number, num: number): boolean => {
    for (let x = 0; x < 9; x++) {
      if (grid[row][x] === num || grid[x][col] === num) return false;
    }

    const boxRow = Math.floor(row / 3) * 3;
    const boxCol = Math.floor(col / 3) * 3;
    for (let i = 0; i < 3; i++) {
      for (let j = 0; j < 3; j++) {
        if (grid[boxRow + i][boxCol + j] === num) return false;
      }
    }
    return true;
  };

  async function solveSudokuBacktracking() {
    setSolving(true);
    solverRef.current.abort = false;
    solverRef.current.currentDelay = delay;
    const sudokuGrid = JSON.parse(JSON.stringify(grid));
    
    async function backtrack(sudokuGrid: number[][]): Promise<boolean> {
      if (solverRef.current.abort) return false;

      if (solverRef.current.pause) {
        await new Promise<void>((resolve) => {
          const checkPause = () => {
            if (solverRef.current.abort || !solverRef.current.pause) resolve();
            else setTimeout(checkPause, 100);
          };
          checkPause();
        });
      }

      for (let row = 0; row < 9; row++) {
        for (let col = 0; col < 9; col++) {
          if (sudokuGrid[row][col] === 0) {
            for (let num = 1; num < 10; num++) {
              if (solverRef.current.abort) return false;

              if (isValidPlacement(sudokuGrid, row, col, num)) {
                sudokuGrid[row][col] = num;
                await new Promise(resolve => setTimeout(resolve, solverRef.current.currentDelay));
                if (!solverRef.current.abort) {
                  setGrid(JSON.parse(JSON.stringify(sudokuGrid)));
                }
                
                if (await backtrack(sudokuGrid)) return true;
                if (solverRef.current.abort) return false;
                
                sudokuGrid[row][col] = 0;
                await new Promise(resolve => setTimeout(resolve, solverRef.current.currentDelay));
                if (!solverRef.current.abort) {
                  setGrid(JSON.parse(JSON.stringify(sudokuGrid)));
                }
              }
            }
            return false;
          }
        }
      }
      return true;
    }
    
    await backtrack(sudokuGrid);
    if (!solverRef.current.abort) {
      setSolving(false);
    }
  }

  const toggleSolving = () => {
    if (solving) {
      solverRef.current.pause = !solverRef.current.pause;
    } else {
      solverRef.current.pause = false;
      solveSudokuBacktracking();
    }
  };

  const resetGrid = () => {
    solverRef.current.abort = true;
    solverRef.current.pause = false;
    setGrid(JSON.parse(JSON.stringify(initialGrid)));
    setSolving(false);
  };

  const handleDelayChange = (newDelay: number) => {
    setDelay(newDelay);
    solverRef.current.currentDelay = newDelay;
  };

  const renderCell = (row: number, col: number) => {
    const value = grid[row][col];
    const isOriginal = initialGrid[row][col] !== 0;
    const boxRow = Math.floor(row / 3);
    const boxCol = Math.floor(col / 3);
    const isAlternateBox = (boxRow + boxCol) % 2 === 0;

    return (
      <div
        key={`${row}-${col}`}
        className={`
          w-12 h-12 flex items-center justify-center
          border border-gray-200 text-xl
          ${isAlternateBox ? 'bg-gray-50' : 'bg-white'}
          ${isOriginal ? 'font-bold text-black' : 'text-blue-600'}
          ${(col + 1) % 3 === 0 && col !== 8 ? 'border-r-2 border-r-gray-400' : ''}
          ${(row + 1) % 3 === 0 && row !== 8 ? 'border-b-2 border-b-gray-400' : ''}
        `}
      >
        {value !== 0 ? value : ''}
      </div>
    );
  };

  const renderGrid = () => {
    return grid.map((row, rowIndex) => (
      <div key={rowIndex} className="flex">
        {row.map((_, colIndex) => renderCell(rowIndex, colIndex))}
      </div>
    ));
  };

  return (
    <div className="p-6 bg-white rounded-lg shadow-md max-w-fit">
      <div className="flex gap-4 mb-6">
        <button
          onClick={toggleSolving}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
        >
          {solving ? (solverRef.current.pause ? 'Resume' : 'Pause') : 'Start'}
        </button>
        <button
          onClick={resetGrid}
          className="px-4 py-2 border border-gray-300 rounded hover:bg-gray-50 transition-colors"
        >
          Reset
        </button>
        <div className="flex items-center gap-2">
          <span className="text-sm text-gray-500">Delay:</span>
          <input
            type="range"
            min="1"
            max="200"
            value={delay}
            onChange={(e) => handleDelayChange(parseInt(e.target.value))}
            className="w-24"
          />
        </div>
      </div>
      <div className="border-2 border-gray-400">
        {renderGrid()}
      </div>
    </div>
  );
};

export default Sudoku;