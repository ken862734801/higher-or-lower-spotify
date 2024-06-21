export const getRandomIndex = (data: any) => {
  const len = data.length;
  const firstIndex = Math.floor(Math.random() * len);
  let secondIndex = Math.floor(Math.random() * len);
  while (secondIndex === firstIndex) {
    secondIndex = Math.floor(Math.random() * len);
  }
  return { firstIndex, secondIndex };
};
