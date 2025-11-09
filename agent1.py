import google.generativeai as genai


api_key = "Enter your API Key over here"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_steps(goal):
    response = model.generate_content(f"Give clear and simple steps to achieve this goal: {goal}")
    return response.text


def refine_steps(steps, feedback):
    response = model.generate_content(f"Improve these steps:\n{steps}\nUsing this feedback: {feedback}")
    return response.text

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    steps = generate_steps(goal)
    print("\nSteps:\n", steps)

    feedback = input("\nAny feedback to refine (or type 'no'): ")
    if feedback.lower() != "no":
        refined = refine_steps(steps, feedback)
        print("\nRefined Steps:\n", refined)
    else:
        print("\nFinal Steps:\n", steps)