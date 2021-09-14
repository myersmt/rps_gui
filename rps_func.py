'''
Matt Myers
09/14/2021
This is the functions for
the rps game 
'''
def results(uc, cc):
    if uc == cc:
        message = 'It\'s a tie, I would try again'
        return message
    elif uc == 'Rock':
        if cc == 'Scissors':
            message = 'You\'ve won, Congratulations!'
            u += 1
        else:
            message = 'You\'ve lost, better luck next time!'
            c += 1
        return message,u,c
    elif uc == 'Paper':
        if cc == 'Rock':
            message = 'You\'ve won, Congratulations!'
            u += 1
        else:
            message = 'You\'ve lost, better luck next time!'
            c += 1
        return message,u,c
    elif uc == 'Scissors':
        if cc == 'Paper':
            message = 'You\'ve won, Congratulations!'
            u += 1
        else:
            message = 'You\'ve lost, better luck next time!'
            c += 1
        return message,u,c
    else:
        message = 'Error'
        return message



