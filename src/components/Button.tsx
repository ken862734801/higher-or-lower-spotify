import { cn } from "@/utils";
import React, { ButtonHTMLAttributes } from "react";

export type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  children?: React.ReactNode;
  onClick?: () => void;
  className?: string;
};

export const Button: React.FC<ButtonProps> = ({
  children,
  onClick,
  className,
}) => {
  const classes = cn("rounded-full uppercase", className);
  return (
    <button className={classes} onClick={onClick}>
      <span className="text-xl">{children}</span>
    </button>
  );
};
