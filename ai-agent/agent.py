from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def run_agent(prompt):
    try:
        system_prompt = """
        Kamu adalah AI asisten kantin sekolah.
        Tugasmu:
        - Memberikan rekomendasi menu
        - Menjawab dengan singkat dan jelas
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"