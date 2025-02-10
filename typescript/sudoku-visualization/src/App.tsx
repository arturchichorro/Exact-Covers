import './App.css'
import SudokuBacktrack from './Sudoku/components/SudokuBacktrack'
import SudokuAlgX from './Sudoku/components/SudokuAlgX';
import SudokuComparison from './Sudoku/components/SudokuComparison';
import PlayableSudoku from './Sudoku/components/PlayableSudoku';

const initialGrid: number[][] = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9],
];

const grid2: number[][] = [
  [0, 0, 0, 0, 9, 0, 4, 1, 2],
  [0, 0, 0, 4, 7, 0, 0, 0, 0],
  [0, 0, 6, 5, 0, 2, 9, 0, 0],
  [4, 0, 0, 7, 0, 0, 0, 2, 0],
  [0, 0, 0, 0, 0, 8, 7, 0, 0],
  [5, 8, 0, 0, 0, 0, 6, 0, 0],
  [0, 2, 0, 0, 0, 5, 0, 0, 0],
  [8, 0, 0, 0, 0, 0, 0, 0, 1],
  [6, 0, 0, 2, 0, 0, 0, 3, 0],
];

const grid3: number[][] = [
  [0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 0, 0, 4],
  [6, 0, 0, 0, 0, 0, 9, 0, 0],
  [0, 0, 0, 0, 0, 0, 2, 8, 0],
  [7, 0, 0, 9, 0, 2, 0, 3, 6],
  [0, 8, 0, 7, 0, 0, 4, 0, 0],
  [0, 0, 0, 0, 6, 0, 5, 1, 8],
  [0, 0, 2, 0, 0, 0, 0, 0, 0],
  [0, 7, 0, 0, 3, 5, 0, 0, 0],
]

const solutionGrid: number[][] = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9],
];

function App() {

  return (
    <>
      <div className="flex">
        <SudokuBacktrack initialGrid={initialGrid}/>
        <SudokuAlgX initialGrid={initialGrid} />
      </div>
      <div>
        <SudokuComparison initialGrid={initialGrid} />
      </div>
      <div>
        <PlayableSudoku initialGrid={initialGrid} solutionGrid={solutionGrid}/>
      </div>
      <div>
      <SudokuBacktrack initialGrid={grid2}/>
        <SudokuAlgX initialGrid={grid2} />
        <SudokuAlgX initialGrid={grid3} />
      </div>
    </>
  )
}

export default App
