import type { Metadata } from "next";
import { Figtree } from "next/font/google";
import "./globals.css";
import { Analytics } from "@vercel/analytics/react"

const figTree = Figtree({
  subsets: ["latin"],
  weight: "400",
  variable: "--figtree",
});

export const metadata: Metadata = {
  title: "Higher or Lower: Spotify Edition",
  description: "Which song has a higher weekly stream count on Spotify? A simple game of higher or lower based on Spotify's weekly chart. Play now!",
  keywords: ["higher or lower", "Spotify"]
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={figTree.variable}>
      <body>{children}</body>
      <Analytics/>
    </html>
  );
}
