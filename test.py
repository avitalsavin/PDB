# i am hoping this works part 2

import argparse


def greetings(name, age):
    if (args.name):
        print("Hello " + args.name + ", you are "+ args.age + ' years old.')
    else:
        print('Please provide name')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--name', help='Please provide name')
    parser.add_argument('-a', '--age', help='Please provide age')

    args = parser.parse_args()

    greetings(args.name, args.age)



