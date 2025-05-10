import { sql } from "@vercel/postgres";
import { NextRequest, NextResponse } from "next/server";

export const runtime = "nodejs";

export async function GET(request: NextRequest) {
  const { searchParams } = new URL(request.url);
  const scoreParam = searchParams.get("score");

  if (!scoreParam) {
    return NextResponse.json(
      { message: "Missing `score` query parameter." },
      { status: 400 }
    );
  }

  const score = Number(scoreParam);
  if (isNaN(score)) {
    return NextResponse.json(
      { message: "`score` must be a number." },
      { status: 400 }
    );
  }

  try {
    // count how many scores are below yours, and total rows
    const result = await sql`
      SELECT
        COUNT(*) FILTER (WHERE score < ${score})::float   AS lower_count,
        COUNT(*)::float                                   AS total_count
      FROM scores;
    `;

    const { lower_count, total_count } = result.rows[0];
    const lowerCount = Number(lower_count);
    const totalCount = Number(total_count);

    const percentile =
      totalCount > 0 ? (lowerCount / totalCount) * 100 : 0;

    return NextResponse.json(
      { percentile: Number(percentile.toFixed(2)) },
      { status: 200 }
    );
  } catch (error) {
    console.error("Error computing percentile:", error);
    return NextResponse.json(
      { message: "Error computing percentile." },
      { status: 500 }
    );
  }
}

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
    console.log(`Score: ${score} successfully added to database.`)
    return NextResponse.json(
      {
        message: `Score: ${score} successfully added to database.`,
      },
      { status: 200 }
    );
  } catch (error) {
    console.log("Error adding user score.")
    return NextResponse.json(
      { message: "Error adding user score." },
      { status: 500 }
    );
  }
}
