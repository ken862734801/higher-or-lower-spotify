import "@testing-library/jest-dom";
import { render, screen, fireEvent } from "@testing-library/react";
import {EndScreen} from "../../src/components/content/EndScreen";

describe("End Screen", () => {
  const mockScores = { score: 5, highScore: 10 };
  const mockRestartGame = jest.fn();

  beforeEach(() => {
    render(<EndScreen scores={mockScores} restartGame={mockRestartGame} />);
  });

  it("displays the final score", () => {
    const scoreElement = screen.getByText("5");
    expect(scoreElement).toBeInTheDocument();
  });

  it('displays the "Game Over" heading', () => {
    const gameOverHeading = screen.getByText("Game Over");
    expect(gameOverHeading).toBeInTheDocument();
  });

  it("calls restartGame when Play Again button is clicked", () => {
    const playAgainButton = screen.getByRole("button", { name: /Play Again/i });
    fireEvent.click(playAgainButton);
    expect(mockRestartGame).toHaveBeenCalled();
  });
});
