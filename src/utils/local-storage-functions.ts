export const saveToLocalStorage = (name: string, data: any) => {
  localStorage.setItem(name, JSON.stringify(data));
};

export const getFromLocalStorage = (name: string) => {
  const item = localStorage.getItem(name);
  return item ? JSON.parse(item) : null;
};
