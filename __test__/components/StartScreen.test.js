import "@testing-library/jest-dom";
import { render, screen } from "@testing-library/react";
import { StartScreen } from "../../src/components/content/StartScreen";

describe("Start Screen", () => {
  it("correctly renders the start screen", () => {
    render(<StartScreen />);

    expect(screen.getByText(/Welcome To/i)).toBeInTheDocument();
    expect(screen.getByText(/Higher Or Lower/i)).toBeInTheDocument();
    expect(screen.getByText(/Spotify Edition/i)).toBeInTheDocument();
    expect(
      screen.getByText(/Which song has more streams this week?/i)
    ).toBeInTheDocument();

    const playButton = screen.getByRole("button", { name: /Play/i });
    expect(playButton).toBeInTheDocument();
    expect(playButton).toHaveClass("text-white");
    expect(playButton).toHaveTextContent("Play");
  });
});
