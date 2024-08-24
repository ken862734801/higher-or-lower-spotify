import { sql } from "@vercel/postgres";
import { NextApiRequest, NextApiResponse } from "next";

export default async function POST(
  request: NextApiRequest,
  response: NextApiResponse
) {
  if (request.method === "POST") {
    const { userId, highScore } = request.body;
    try {
      await sql`
            INSERT INTO scores (user_id, high_score)
            VALUES (${userId}, ${highScore})
            ON CONFLICT (user_id)
            DO UPDATE SET high_score = GREATEST(scores.high_score, EXCLUDED.high_score)
        `;
      return response
        .status(200)
        .json({ message: "Score successfully added to database." });
    } catch (error) {
      return response.status(500).json({ message: "Error adding user score." });
    }
  } else {
    response.setHeader("Allow", ["POST"]);
    response.status(405).end(`Method ${request.method} Not Allowed.`);
  }
}
