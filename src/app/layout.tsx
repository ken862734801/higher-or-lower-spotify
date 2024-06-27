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
  description: "An addictive game of higher or lower. Guess which song has more weekly streams on Spotify.",
  keywords: ["higher or hower", "Spotify"]
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
