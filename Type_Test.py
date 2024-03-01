from time import *
import random as rd

def mistake(para_test, user_test):
    error_count = 0
    for i in range(len(para_test)):
        try:
            if para_test[i] != user_test[i]:
                error_count = error_count + 1
        except:
            error_count = error_count + 1
    return error_count

def speed_time(time_Start, time_End, user_input):
    time_Delay = time_End - time_Start
    time_Roundoff = round(time_Delay, 2)
    speed = len(user_input)/time_Roundoff
    return round(speed)

if __name__ == "__main__":
    while True:
        chk = input("Ready to Type? (Y/N): ")
        if chk == 'Y' or chk == 'y':
#print(time())

            test=["She has seen this scene before. It had come to her in dreams many times before. She had to pinch herself to make sure it wasn't a dream again. As her fingers squeezed against her arm, she felt the pain. It was this pain that immediately woke her up.",
                "You can decide what you want to do in life, but I suggest doing something that creates. Something that leaves a tangible thing once you're done. That way even after you're gone, you will still live on in the things you created.",
                "The fog was as thick as pea soup. This was a problem. Gary was driving but couldn't see a thing in front of him. He knew he should stop, but the road was narrow so if he did, it would be right in the center of the road. He was sure that another car would end up rear-ending him, so he continued forward despite the lack of visibility. This was an unwise move."]

            test1= rd.choice(test)

            print("Typing Speed Test")
            print(test1)

            print() # for break line
            print() # for break line

            time_1 = time()

            test_input = input("Enter: ")

            time_2 = time()

            print('Speed: ', speed_time(time_1, time_2, test_input), "word/sec")
            print("Error: ", mistake(test1, test_input), "word")

        elif chk == 'N' or chk == 'n':
            print("Thank you visit again.")
            break

        else:
            print("Invalid Input")