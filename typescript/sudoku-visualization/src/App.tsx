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
        <PlayableSudoku initialGrid={initialGrid}/>
      </div>
    </>
  )
}

export default App
