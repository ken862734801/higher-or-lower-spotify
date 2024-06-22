import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px'
    },
    extend: {
      fontFamily: {
        figtree: ["var(--figtree)"],
      },
      colors: {
        citrus: "#CDF564",
        fuchsia: "#F037A5",
        spearmint: "#4B917D"
      },
    },
  },
  plugins: [],
};
export default config;
