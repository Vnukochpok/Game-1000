from logic.logic1000 import throw, get_normal_score

play = True
def game(player1, player2):
    total_score_p1 = 0
    total_score_p2 = 0
    while play:
        log_p1 = player1
        log_p2 = player2

        hod_p1 = True
        hod_p2 = False

        k = 5

        while hod_p1:
            print("---------ХОД ИГРОКА №1---------")
            throwing = throw(k)
            print(throwing)
            list_res = get_normal_score(throwing)
            print(list_res)
            score = list_res[0]
            reroll_dice = list_res[1]

            #[0, 5] [0, 2]
            if score == 0 and (reroll_dice == 5 or reroll_dice < 5):
                print(f"\n{total_score_p1} - счет")
                print("\n\n\nНичего не выпало, ход передается следующему игроку\n ---------------------------------")
                hod_p1 = False
                hod_p2 = True
                break

            #[20, 2]
            elif score != 0 and reroll_dice < 5:
                total_score_p1 += score
                decis = input("Хотите кинуть кубики еще раз? (Y/N)")
                if decis == 'Y':
                    k = reroll_dice
                elif decis == 'N':
                    print(f"\n{total_score_p1} - счет")
                    print("\n\n\nХод передается следующему игроку\n ---------------------------------")
                    hod_p1 = False
                    hod_p2 = True
                    break
                else:
                    print("Wrong answer >:(")
                    pass

            #[55, 0]
            elif score != 0 and reroll_dice == 0:
                total_score_p1 += score
                decis = input("Хотите кинуть кубики еще раз? (Y/N)")
                if decis == 'Y':
                    k = 5

                elif decis == 'N':
                    print(f"\n{total_score_p1} - счет")
                    print("\n\n\nХод передается следующему игроку\n ---------------------------------")
                    hod_p1 = False
                    hod_p2 = True
                    break

                else:
                    print("Wrong answer >:(")
                    pass

            else:
                print("Ошибка")


        while hod_p2:
            print("---------ХОД ИГРОКА №2---------")
            throwing = throw(k)
            list_res = get_normal_score(throwing)
            score = list_res[0]
            reroll_dice = list_res[1]

            if score == 0 and (reroll_dice == 5 or reroll_dice < 5):
                print(f"\n{total_score_p2} - счет")
                print("\n\n\nНичего не выпало, ход передается следующему игроку\n ---------------------------------")
                hod_p2 = False
                hod_p1 = True
                break

            elif score != 0 and reroll_dice < 5:
                total_score_p2 += score
                decis = input("Хотите кинуть кубики еще раз? (Y/N)")
                if decis == 'Y':
                    k = reroll_dice
                elif decis == 'N':
                    print(f"\n{total_score_p2} - счет")
                    print("\n\n\nХод передается следующему игроку\n ---------------------------------")
                    hod_p2 = False
                    hod_p1 = True
                    break
                else:
                    print("Wrong answer >:(")
                    break

            elif score != 0 and reroll_dice == 0:
                total_score_p2 += score
                decis = input("Хотите кинуть кубики еще раз? (Y/N)")
                if decis == 'Y':
                    k = 5

                elif decis == 'N':
                    print(f"\n{total_score_p2} - счет")
                    print("\n\n\nХод передается следующему игроку\n ---------------------------------")

                    hod_p2 = False
                    hod_p1 = True
                    break

                else:
                    print("Wrong answer >:(")
                    break

            else:
                print("Ошибка")

game("andrey", "polya")