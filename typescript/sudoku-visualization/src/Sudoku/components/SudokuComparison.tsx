import React, { useState, useRef } from 'react';
import { SudokuGrid } from './SudokuGrid';
import { SudokuControls } from './SudokuControls';
import { createBacktrackingSolver } from '../utils/sudokuSolver';
import { createAlgorithmXSolver } from '../utils/sudokuSolverAlgX';
import type { SolverRef } from '../utils/types';
import { speedToDelay } from '../utils/utils';

interface SudokuComparisonProps {
  initialGrid: number[][];
}

const SudokuComparison: React.FC<SudokuComparisonProps> = ({ initialGrid }) => {
  const [speed, setSpeed] = useState(50); // Default speed of 50%
  const [solving, setSolving] = useState(false);
  
  const [backtrackGrid, setBacktrackGrid] = useState<number[][]>(
    JSON.parse(JSON.stringify(initialGrid))
  );
  const [algXGrid, setAlgXGrid] = useState<number[][]>(
    JSON.parse(JSON.stringify(initialGrid))
  );

  const solverRef = useRef<SolverRef>({
    pause: false,
    abort: false,
    currentDelay: speedToDelay(50) // Initialize with default speed
  });

  async function solveWithBothAlgorithms() {
    setSolving(true);
    solverRef.current.abort = false;
    solverRef.current.currentDelay = speedToDelay(speed);

    await Promise.all([
      (async () => {
        const backtrackSolver = createBacktrackingSolver(setBacktrackGrid, solverRef);
        await backtrackSolver(JSON.parse(JSON.stringify(initialGrid)));
      })(),
      (async () => {
        const algXSolver = createAlgorithmXSolver(setAlgXGrid, solverRef);
        await algXSolver(initialGrid);
      })()
    ]);

    if (!solverRef.current.abort) {
      setSolving(false);
    }
  }

  const toggleSolving = () => {
    if (solving) {
      solverRef.current.pause = !solverRef.current.pause;
    } else {
      solverRef.current.pause = false;
      solveWithBothAlgorithms();
    }
  };

  const resetGrids = () => {
    solverRef.current.abort = true;
    solverRef.current.pause = false;
    setBacktrackGrid(JSON.parse(JSON.stringify(initialGrid)));
    setAlgXGrid(JSON.parse(JSON.stringify(initialGrid)));
    setSolving(false);
  };

  const handleSpeedChange = (newSpeed: number) => {
    setSpeed(newSpeed);
    solverRef.current.currentDelay = speedToDelay(newSpeed);
  };

  return (
    <div className="p-6">
      <div className="mb-6">
        <SudokuControls
          solving={solving}
          isPaused={solverRef.current.pause}
          speed={speed}
          onToggleSolving={toggleSolving}
          onReset={resetGrids}
          onSpeedChange={handleSpeedChange}
        />
      </div>

      <div className="flex gap-8 items-start">
        <div className="flex-1">
          <div className="bg-white rounded-lg shadow-md p-6 max-w-fit mx-auto">
            <SudokuGrid grid={backtrackGrid} initialGrid={initialGrid} />
          </div>
        </div>

        <div className="flex-1">
          <div className="bg-white rounded-lg shadow-md p-6 max-w-fit mx-auto">
            <SudokuGrid grid={algXGrid} initialGrid={initialGrid} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default SudokuComparison;