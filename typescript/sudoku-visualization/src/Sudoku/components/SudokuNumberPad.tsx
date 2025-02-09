import React from 'react';

interface SudokuNumberPadProps {
  onNumberSelect: (num: number) => void;
  disabled?: boolean;
}

const SudokuNumberPad: React.FC<SudokuNumberPadProps> = ({ onNumberSelect, disabled = false }) => {
  const numbers = Array.from({ length: 9 }, (_, i) => i + 1);

  return (
    <div className="">
      <div className="grid grid-cols-5 gap-2 max-w-md mx-auto">
        {numbers.map((num) => (
          <button
            key={num}
            onClick={() => onNumberSelect(num)}
            disabled={disabled}
            className={`
              p-2 text-md font-semibold rounded
              ${disabled 
                ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
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
          className={`
            p-2 text-md font-semibold rounded col-span-1
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