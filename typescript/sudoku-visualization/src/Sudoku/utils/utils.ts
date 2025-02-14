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