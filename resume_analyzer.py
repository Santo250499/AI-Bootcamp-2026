import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, AuthenticationError


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

if not api_key:
    raise ValueError("OPENAI_API_KEY is missing. Please add it to your .env file.")

client = OpenAI(api_key=api_key)


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None


def ask_ai(prompt):
    try:
        response = client.responses.create(
            model=model,
            instructions=(
                "You are a professional resume reviewer and career coach. "
                "Give clear, practical, beginner-friendly feedback. "
                "Focus on ATS, job matching, and professional improvement."
            ),
            input=prompt,
        )

        return response.output_text

    except AuthenticationError:
        return (
            "OpenAI API authentication error. Your API key is invalid, expired, "
            "revoked, or copied incorrectly. Please create a new API key and update your .env file."
        )

    except RateLimitError:
        return (
            "OpenAI API quota error. Please check your billing, credits, usage, and project limits."
        )

    except Exception as error:
        return f"Something went wrong: {error}"


def analyze_resume():
    resume = read_file("sample_resume.txt")
    job_description = read_file("job_description.txt")

    if not resume:
        print("sample_resume.txt not found.")
        return

    if not job_description:
        print("job_description.txt not found.")
        return

    prompt = f"""
Compare the following resume with the job description.

Resume:
{resume}

Job Description:
{job_description}

Please provide:

1. Match score out of 100
2. Best matching skills
3. Missing skills or keywords
4. Weak points in the resume
5. ATS improvement suggestions
6. Improved professional summary
7. Final recommendation

Make the answer clear and structured.
"""

    result = ask_ai(prompt)
    print("\n===== AI RESUME ANALYSIS =====\n")
    print(result)


def improve_summary():
    resume = read_file("sample_resume.txt")

    if not resume:
        print("sample_resume.txt not found.")
        return

    prompt = f"""
Improve the professional summary for this resume.

Resume:
{resume}

Write:
1. A short professional summary
2. A stronger LinkedIn-style summary
3. A more technical ICT support summary
"""

    result = ask_ai(prompt)
    print("\n===== IMPROVED SUMMARY =====\n")
    print(result)


def generate_cover_letter():
    resume = read_file("sample_resume.txt")
    job_description = read_file("job_description.txt")

    if not resume:
        print("sample_resume.txt not found.")
        return

    if not job_description:
        print("job_description.txt not found.")
        return

    prompt = f"""
Write a short professional cover letter based on this resume and job description.

Resume:
{resume}

Job Description:
{job_description}

Requirements:
- Formal but natural tone
- Short and direct
- Suitable for ICT Support Engineer role
- Do not exaggerate
"""

    result = ask_ai(prompt)
    print("\n===== COVER LETTER =====\n")
    print(result)

def rewrite_bullet_points():
    resume = read_file("sample_resume.txt")

    if not resume:
        print("sample_resume.txt not found.")
        return

    prompt = f"""
Rewrite the resume bullet points below to make them stronger, more professional, and ATS-friendly.

Resume:
{resume}

Rules:
- Use strong action verbs
- Keep the experience honest
- Do not invent fake experience
- Make it suitable for ICT Support, Cloud Support, and Microsoft 365 roles
- Improve clarity and professionalism
- Format the answer as strong resume bullet points
"""

    result = ask_ai(prompt)
    print("\n===== REWRITTEN RESUME BULLET POINTS =====\n")
    print(result)



def main():
    while True:
        print("\n===== DAY 4 AI RESUME ANALYZER =====")
        print("1. Analyze Resume Against Job Description")
        print("2. Improve Resume Summary")
        print("3. Generate Cover Letter")
        print("4. Rewrite Resume Bullet Points")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            analyze_resume()
        elif choice == "2":
            improve_summary()
        elif choice == "3":
            generate_cover_letter()
        elif choice == "4":
            rewrite_bullet_points()
        elif choice == "5":
            print("Good job. Day 4 completed.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()