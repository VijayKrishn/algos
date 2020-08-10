class Robot:
    def __init__(self):
        self.startmsg = "Command the robot with:\n  L - turn left\n  R - turn right\n  M - move forward\n  ? - print this message\n  Q - quit"
        print("Hello! Robot coming online.")
        print(self.startmsg)
        self.posx = 0
        self.posy = 0
        self.dirs = {'North':(0,1),'South':(0,-1),'West':(-1,0),'East':(1,0)}
        self.dirmap = {0:'North', 1:'East', 2:'South', 3:'West'}

    def start(self):
        count = 0
        while True:
            inp = str(input())
            if(inp == '?'):
                print(self.startmsg)
            elif(inp == 'M'):
                dir = self.dirmap[count]
                dx, dy = self.dirs[dir]
                self.posx += dx
                self.posy += dy
                print('Robot at (%d, %d) facing %s' %(self.posx, self.posy, dir))
            elif(inp == 'R'):
                count += 1
                count %= 4
                dir = self.dirmap[count]
                print('Robot at (%d, %d) facing %s' % (self.posx, self.posy, dir))
            elif(inp == 'L'):
                count += 3
                count %= 4
                dir = self.dirmap[count]
                print('Robot at (%d, %d) facing %s' % (self.posx, self.posy, dir))
            elif(inp == 'Q'):
                break
            else:
                print(self.startmsg)

r = Robot()
r.start()