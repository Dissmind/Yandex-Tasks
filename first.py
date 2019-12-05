def algorithm(input):
    checkString = "aeiou"
    counter     = 0

    iteration   = 0
    flag        = 0

    for i in input:
        iteration += 1
        for j in checkString:
            if i == j:
                flag += 1

            if i == "$" or iteration == len(input) - 1:
                if flag == 1:
                    counter += 1
                    flag = 0
                else:
                    flag = 0

    return counter

def unitTest(input, testName, correctAnswer):

    counter = algorithm(input)

    if counter == correctAnswer:
        print(testName + ": Пройден")
    else:
        print(testName + ": Не пройден" + " [" + str(correctAnswer) + " != " + str(counter) + "]")

unitTest("Yandex$lyceum$is$awesome", "First", 1)
unitTest("Say$yes$to$python", "Second", 4)

