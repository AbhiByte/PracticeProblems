def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce and bounce < 1 and window > h:
        new_height = h*bounce
        counter = 0
        if new_height > window:
            counter += 2
            return bouncing_ball(new_height, bounce, window)
        else:
            counter += 1
        return counter
    return -1


print(bouncing_ball)
