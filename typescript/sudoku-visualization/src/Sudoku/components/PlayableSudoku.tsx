import React, { useState, useEffect, useCallback, useRef } from 'react';
import { SudokuCell } from './SudokuCell';
import SudokuNumberPad from './SudokuNumberPad';

interface SudokuGridProps {
  initialGrid: number[][];
  solutionGrid: number[][];
}

const PlayableSudoku: React.FC<SudokuGridProps> = ({ initialGrid, solutionGrid }) => {
    const [grid, setGrid] = useState<number[][]>(initialGrid.map(row => [...row]));
    const [selectedCell, setSelectedCell] = useState<[number, number] | null>(null);
    const [isCorrect, setIsCorrect] = useState<boolean>(false);
    const gridRef = useRef<HTMLDivElement>(null);
    const padRef = useRef<HTMLDivElement>(null);

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

    const checkCompletion = useCallback((currentGrid: number[][]) => {
        const complete = currentGrid.every(row => row.every(cell => cell !== 0));
        if (!complete) return;

        if (complete) {
            const correct = currentGrid.every((row, i) =>
                row.every((val, j) => val === solutionGrid[i][j])
            );
            setIsCorrect(correct)
        }

    }, [solutionGrid])

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

    const handleClickOutside = useCallback((event: MouseEvent) => {
        if (
            gridRef.current 
            && !gridRef.current.contains(event.target as Node)
            && padRef.current 
            && !padRef.current.contains(event.target as Node)
        ) {
            setSelectedCell(null);
        }
    }, []);

    useEffect(() => {
        window.addEventListener('keydown', handleKeyPress);
        document.addEventListener('mousedown', handleClickOutside);
        return () => { 
            window.removeEventListener('keydown', handleKeyPress); 
            document.removeEventListener('mousedown', handleClickOutside);
        }
    }, [handleKeyPress, handleClickOutside]);

    useEffect(() => {
        checkCompletion(grid);
    }, [grid, checkCompletion]);

    const handleReset = () => {
        setGrid(initialGrid.map(row => [...row]));
        setSelectedCell(null);
    };

    const handleNumberSelect = (num: number) => {
        if (!selectedCell) return;
        
        const [row, col] = selectedCell;
        if (initialGrid[row][col] === 0) {
          setGrid(prevGrid => {
            const newGrid = prevGrid.map(row => [...row]);
            newGrid[row][col] = num;
            return newGrid;
          });
        }
    };

    return (
        <div className="flex flex-row justify-center items-center gap-4">
        <div ref={gridRef} className="border-2 border-gray-400">
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
        <SudokuNumberPad 
            onNumberSelect={handleNumberSelect}
            onReset={handleReset}
            disabled={!selectedCell}
            isCorrect={isCorrect}
            padRef={padRef}
        />
        </div>
    );
};

export default PlayableSudoku;