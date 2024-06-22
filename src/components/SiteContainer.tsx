export interface SiteContainerProps {
  children?: React.ReactNode;
}
export const SiteContainer: React.FC<SiteContainerProps> = ({ children }) => {
  return (
    <main className="min-h-[100vh] text-center bg-black flex flex-col justify-center relative">
      {children}
    </main>
  );
};
