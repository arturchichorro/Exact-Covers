import React, { useState, useEffect, useCallback } from 'react';
import { SudokuCell } from './SudokuCell';

interface SudokuGridProps {
  initialGrid: number[][];
}

const PlayableSudoku: React.FC<SudokuGridProps> = ({ initialGrid }) => {
    const [grid, setGrid] = useState<number[][]>(initialGrid.map(row => [...row]));
    const [selectedCell, setSelectedCell] = useState<[number, number] | null>(null);

    const isValidMove = (row: number, col: number, value: number): boolean => {
        for (let i = 0; i < 9; i++) {
        if (i !== col && grid[row][i] === value || i !== row && grid[i][col] === value) return false;
        }
        
        const boxRow = Math.floor(row / 3) * 3;
        const boxCol = Math.floor(col / 3) * 3;
        for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (boxRow + i !== row || boxCol + j !== col) {
            if (grid[boxRow + i][boxCol + j] === value) return false;
            }
        }
        }
        return true;
    };

    const handleCellClick = (rowIndex: number, colIndex: number) => {
        if (initialGrid[rowIndex][colIndex] === 0) {
        setSelectedCell([rowIndex, colIndex]);
        }
    };

    const handleKeyPress = useCallback((e: KeyboardEvent) => {
        if (!selectedCell) return;
    
        const num = parseInt(e.key);
        if (num >= 0 && num <= 9) {
        const [row, col] = selectedCell;
        
        if (num === 0) {
            setGrid(prevGrid => {
            const newGrid = prevGrid.map(row => [...row]);
            newGrid[row][col] = 0;
            return newGrid;
            });
            return;
        }
    
        else {
            setGrid(prevGrid => {
            const newGrid = prevGrid.map(row => [...row]);
            newGrid[row][col] = num;
            return newGrid;
            });
        }
        }
    }, [selectedCell]);

    useEffect(() => {
        window.addEventListener('keydown', handleKeyPress);
        return () => window.removeEventListener('keydown', handleKeyPress);
    }, [handleKeyPress]);

    const handleReset = () => {
        setGrid(initialGrid.map(row => [...row]));
        setSelectedCell(null);
    };

    return (
        <div className="flex flex-col items-center gap-4">
        <div className="border-2 border-gray-400">
            {grid.map((row, rowIndex) => (
            <div key={rowIndex} className="flex">
                {row.map((_, colIndex) => {
                const value = grid[rowIndex][colIndex];
                const isOriginal = initialGrid[rowIndex][colIndex] !== 0;
                const boxRow = Math.floor(rowIndex / 3);
                const boxCol = Math.floor(colIndex / 3);
                const isAlternateBox = (boxRow + boxCol) % 2 === 0;
                const isSelected = selectedCell?.[0] === rowIndex && selectedCell?.[1] === colIndex;
                const isValid = value === 0 ? true : isValidMove(rowIndex, colIndex, value);

                return (
                    <SudokuCell
                    key={`${rowIndex}-${colIndex}`}
                    value={value}
                    isOriginal={isOriginal}
                    isAlternateBox={isAlternateBox}
                    borderRight={(colIndex + 1) % 3 === 0 && colIndex !== 8}
                    borderBottom={(rowIndex + 1) % 3 === 0 && rowIndex !== 8}
                    isSelected={isSelected}
                    onClick={() => handleCellClick(rowIndex, colIndex)}
                    isValid={isValid}
                    isPlayable={true}
                    />
                );
                })}
            </div>
            ))}
        </div>
        <button 
            onClick={handleReset}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
        >
            Reset Game
        </button>
        </div>
    );
};

export default PlayableSudoku;