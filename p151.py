# import random
# import requests

# # Function to fetch a random easy question for kids
# def fetch_random_question():
#     # Use the Open Trivia Database API with "easy" difficulty
#     url = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=multiple"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         question = data['results'][0]['question']
#         correct_answer = data['results'][0]['correct_answer']
#         return question, correct_answer
#     else:
#         return None, None

# # Main loop
# for i in range(1, 6):
#     # Fetch and ask a random question
#     question, correct_answer = fetch_random_question()
#     if question:
#         print("\nQuestion:", question)
#         user_answer = input("Your answer: ")
#         if user_answer.strip().lower() == correct_answer.lower():
#             print("Correct! 🎉\n")
#         else:
#             print(f"Wrong! The correct answer is: {correct_answer}\n")
#     else:
#         print("Failed to fetch a question. Please try again.\n")