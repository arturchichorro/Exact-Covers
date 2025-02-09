import React from 'react';

interface SudokuNumberPadProps {
  onNumberSelect: (num: number) => void;
  onReset: () => void;
  disabled?: boolean;
  isCorrect?: boolean;
}

const SudokuNumberPad: React.FC<SudokuNumberPadProps> = ({ onNumberSelect, onReset, disabled = false, isCorrect = false }) => {
  const numbers = Array.from({ length: 9 }, (_, i) => i + 1);

  return (
    <div className="">
        {isCorrect && (
        <div className={'text-center p-2 rounded bg-green-100 text-green-800 border border-green-200'}>
            'Congratulations! Puzzle solved correctly!'
        </div>
      )}
      <div className="grid grid-cols-3 gap-2 max-w-md">
        <button 
                onClick={onReset}
                className="col-span-3 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
            >
                Reset Game
        </button>
        {numbers.map((num) => (
          <button
            key={num}
            onClick={() => onNumberSelect(num)}
            disabled={disabled}
            className={`w-12 h-12
              p-2 text-md font-semibold rounded
              ${disabled 
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed border-gray-300'
                : 'bg-white border-2 border-gray-300 hover:bg-gray-100 active:bg-gray-200'
              }
              focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50
            `}
          >
            {num}
          </button>
        ))}
        <button
          onClick={() => onNumberSelect(0)}
          disabled={disabled}
          className={`w-12 h-12
            p-2 text-md font-semibold rounded col-start-2
            ${disabled
              ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
              : 'bg-red-100 border-2 border-red-300 hover:bg-red-200 active:bg-red-300'
            }
            focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-opacity-50
          `}
        >
          ⌫
        </button>
      </div>
    </div>
  );
};

export default SudokuNumberPad;