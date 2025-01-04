#13460
class Ball:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    def move_pos(self, new_pos_x, new_pos_y):
        self.pos_x = new_pos_x
        self.pos_y = new_pos_y
    
class SharedList:
    def __init__(self, x, y):
        self.list = [[0 for _ in range(y) for _ in range(x)]]
        self.count = 0;
        self.x = x;
        self.y = y;
        self.red_ball = Ball(-1, -1)
        self.blue_ball = Ball(-1, -1)
        self.hole = Ball(-1, -1)
        
    def set_2d_list(self, row, temp_row):
        self.list[row] = temp_row
        if 'R' or 'B' or 'O' in temp_row:
            for col in range(self.x):
                if (temp_row[col] == 'R'):
                    self.red_ball.move_pos(row, col)
                elif (temp_row[col] == 'B'):
                    self.blue_ball.move_pos(row, col)
                elif (temp_row[col] == 'O'):
                    self.hole.move_pos(row, col)
        self.list.append(row)
        
    def turn_right(self):
        if (self.red_ball.pos_y == self.blue_ball.pos_y):
            if (self.red_ball.pos_x > self.blue_ball.pos_x):
                self.red_ball.move_pos(self.red_ball.pos_x, self.red_ball.pos_y)
                self.blue_ball.move_pos(self.blue_ball.pos_x - 1, self.blue_ball.pos_y)
            else:
                self.blue_ball.move_pos(self.blue_ball.pos_x, self.blue_ball.pos_y)
                self.red_ball.move_pos(self.red_ball.pos_x - 1, self.red_ball.pos_y)
        else:
            self.red_ball.move_pos()
            self.blue_ball.move_pos()
            
    def turn_left(self):
        pass
    def turn_forward(self):
        pass        
    def turn_backward(self):
        pass
        

def check_success():
    
    if (True):
        return 1
    else:
        return 0

def test(shared_list):
    count = 0
    while (True):
        success = check_success()
        count += 1
        if (count > 10):
            return -1
        if (success):
            break
    return count

def mapping(shared_list):
    for row in range(shared_list.y):
        temp_row = input()
        shared_list.set_2d_list(row, list(temp_row))
    
def init():
    x, y = map(int, input().split())
    if (x < 3 or y > 10):
        print("Invalid input")
        return
    shared_list = SharedList(x, y)
    return shared_list

def main():
    shared_list = init()
    mapping(shared_list)
    answer = test(shared_list)
    print(answer)
    
if __name__ == '__main__':
    main()
