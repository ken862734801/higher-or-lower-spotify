import { NextResponse } from "next/server";
import { promises as fs } from "fs";
import path from "path";

export async function GET() {
  try {
    const filePath = path.join(process.cwd(), "/data", "data.json");
    const jsonData = await fs.readFile(filePath, "utf-8");
    
    const data = JSON.parse(jsonData);

    return NextResponse.json(data, { status: 200 });
  } catch (error) {
    console.error("Error reading data.json:", error);
    return NextResponse.json({ error: "Failed to read data" }, { status: 500 });
  }
}
