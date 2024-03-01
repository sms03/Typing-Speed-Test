from time import time
import random

def calculate_mistakes_and_correct_count(actual_text, user_text):
    error_count = 0
    correct_count = 0
    for i in range(len(actual_text)):
        try:
            if actual_text[i] != user_text[i]:
                error_count += 1
            else:
                correct_count += 1
        except IndexError:
            error_count += 1
    return error_count, correct_count

def calculate_speed(start_time, end_time, user_input):
    time_delay = end_time - start_time
    time_rounded = round(time_delay, 2)
    speed = len(user_input) / time_rounded
    return round(speed)

if __name__ == "__main__":
    while True:
        user_choice = input("Ready to Type? (Y/N): ").lower()

        if user_choice == 'y':
            tests = [
                "She has seen this scene before. It had come to her in dreams many times before. She had to pinch herself to make sure it wasn't a dream again. As her fingers squeezed against her arm, she felt the pain. It was this pain that immediately woke her up.",
                "You can decide what you want to do in life, but I suggest doing something that creates. Something that leaves a tangible thing once you're done. That way even after you're gone, you will still live on in the things you created.",
                "The fog was as thick as pea soup. This was a problem. Gary was driving but couldn't see a thing in front of him. He knew he should stop, but the road was narrow so if he did, it would be right in the center of the road. He was sure that another car would end up rear-ending him, so he continued forward despite the lack of visibility. This was an unwise move."
            ]

            selected_test = random.choice(tests)

            print("Typing Speed Test")
            print(selected_test)
            print()

            while True:
                start_time = time()
                user_input = input("Enter: ")
                end_time = time()

                if user_input.strip():  # Check if the input is not empty
                    break
                else:
                    print("Invalid input. Try again.")

            errors, correct = calculate_mistakes_and_correct_count(selected_test, user_input)
            print('Speed:', calculate_speed(start_time, end_time, user_input), "word/sec")
            print("Error:", errors, "word")
            print("Correct:", correct, "word")

        elif user_choice == 'n':
            print("Thank you, visit again.")
            break

        else:
            print("Invalid Input")