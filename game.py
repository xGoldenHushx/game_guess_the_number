import numpy as np

def guess_the_number(random_number: int = 1) -> int:
    """We guess a randomly guessed number using more or less information. 
    The function accepts a hidden number and outputs the number of attempts

    Args:
        number (int, optional): Random number. Defaults to 1.

       int: Number of attempts
    """
    # To guess, we use the following algorithm: 
    # we will reduce the limit of values depending on whether the 
    # number is smaller or larger.
    
    minimum_value = 1
    maximum_value = 101
    count = 0
       
    while True:
        count += 1
        predict = np.random.randint(minimum_value, maximum_value)
        if predict == random_number:
            break
        elif predict < random_number:
            minimum_value = predict
        elif predict > random_number:
            maximum_value = predict
            
    return count

def score_game(guess_the_number) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(guess_the_number(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
print('Run benchmarking for guess_the_number: ', end='')
score_game(guess_the_number)