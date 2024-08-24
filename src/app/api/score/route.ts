import { sql } from "@vercel/postgres";
import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  const body = await request.json();
  const { userId, score } = body;
  try {
    await sql`
            INSERT INTO scores (user_id, score)
            VALUES (${userId}, ${score})
            ON CONFLICT (user_id)
            DO UPDATE SET score = ${score}
        `;
    return NextResponse.json(
      {
        message: "Score successfully added to database.",
      },
      { status: 200 }
    );
  } catch (error) {
    return NextResponse.json(
      { message: "Error adding user score." },
      { status: 500 }
    );
  }
}
