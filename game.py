import numpy as np

def guess_the_number(random_number: int = 1) -> int:
    """We guess a randomly guessed number using more or less information. 
    The function accepts a hidden number and outputs the number of attempts

    Args:
        number (int, optional): Random number. Defaults to 1.

       int: Number of attempts
    """
    # For guessing, we use the following algorithm: 
    # we will divide our guessing range by 2 at each iteration. 
    # Accordingly, the assumption will be equal to the minimum value of the range plus 
    # the maximum value divided in half
    
    minimum_value = 1
    maximum_value = 100
    count = 0
       
    while True:
        count += 1
        predict = (minimum_value+maximum_value) // 2
        if predict < random_number:
            minimum_value = predict
        elif predict > random_number:
            maximum_value = predict
        elif predict == random_number:
            break
            
    return count

random_number = np.random.randint(1, 101)
print(guess_the_number(random_number))

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")