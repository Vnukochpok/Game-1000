from logic.logic1000 import throw, Combination, check_unscore

play = True
def game(player1, player2):
    while play:
        log_p1 = player1
        log_p2 = player2

        hod_p1 = True
        hod_p2 = False

        check = Combination()
        k = 5
        while hod_p1:
            throwing = throw(k)
            unscored_cube = check_unscore(throwing)

            if check.b_strit(throwing) != 0:
                score = check.b_strit(throwing)
                hod_p1 = True

            if check.m_strit(throwing) != 0:
                score = check.b_strit(throwing)
                hod_p1 = True

            if check.triple(throwing) != 0:
                score = check.b_strit(throwing)

                dec = input("Хотите бросить еще раз?")


