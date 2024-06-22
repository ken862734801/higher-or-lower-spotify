import { Scores } from "@/app/page";
import { memo } from "react";

export interface HeaderProps {
  scores: Scores;
}

export const Header: React.FC<HeaderProps> = memo(({ scores }) => {
  return (
    <header className="absolute top-0 bottom-0 h-10 w-full text-citrus">
      <div className="md:w-4/5 w-11/12 mx-auto flex justify-between text-lg px-4 py-2 uppercase">
        <span>High Score: {scores.highScore}</span>
        <span>Score: {scores.score}</span>
      </div>
    </header>
  );
});

Header.displayName = "Header";