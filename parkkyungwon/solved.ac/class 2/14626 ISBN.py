def main():
    total = 0
    switch = True

    for num in input():
        if num.isnumeric():
            total = (total + int(num) * (1 if switch else 3))
        
        else:
            target_switch = switch

        switch = not switch
        
    answer = (-total * (1 if target_switch else 7)) % 10

    print(answer)


main()
