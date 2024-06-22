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
  description: "A frustratingly addictive game of higher or lower where users guess which song has a higher weekly stream count on Spotify. Play now!",
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
