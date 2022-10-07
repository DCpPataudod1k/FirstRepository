import matplotlib.pyplot as plt
import random as rnd
import math as mt


# Объявление класса и его методов
class Aircraft():
    # Этот метод запустится при объявлении нового объекта:
    def __init__(self, x, y, v, ta):
        self.x = x
        self.y = y
        self.v = v
        self.ta = ta*mt.pi/180

    def move(self, dt):
        self.x = self.x + self.v * mt.cos(self.ta) * dt
        self.y = self.y + self.v * mt.sin(self.ta) * dt

    def turn(self, na):
        na = na * mt.pi/180
        self.ta = self.ta + na

    def isNear(self, r_min, x2, y2):
        result = False
        dx = x2 - self.x
        dy = y2 - self.y
        r = mt.sqrt(dx * dx + dy * dy)
        if r < r_min:
            result = True
        return result

    def findDir(self, x2, y2):
        dx = x2 - self.x
        dy = y2 - self.y
        rx = dx*mt.cos(self.ta) - dy*mt.sin(self.ta)
        ry = dx*mt.sin(self.ta) + dy*mt.cos(self.ta)
        return mt.atan2(ry, rx)

    def plot(self, X, Y, lX, lY):
        plt.scatter(X, Y, linewidth = 5)
        plt.scatter(lX, lY, color = 'r', linewidth = 0.1)
        plt.plot(lX, lY, color = 'r')
        plt.grid()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.text(0, 0, 'Путь следования')
        plt.show()

    def goAlongPath(self, arrX, arrY):
        # Основное тело метода
        i = 0
        logX = [0]
        logY = [0]
        while i < len(arrX):
            while not self.isNear(100, arrX[i], arrY[i]):
                # Коррекция курса + случайный фактор
                self.ta = self.findDir(arrX[i], arrY[i]) + rnd.uniform(-1,1)*mt.pi/180 - self.ta
                self.move(1)
                logX.append(self.x)
                logY.append(self.y)
                print(self.x, self.y, self.ta*180/mt.pi)
            print('Reached the point', i, 'at', arrX[i], arrY[i])
            i = i + 1
        # Пройденный маршрут
        self.plot(arrX, arrY, logX, logY)
        print('Reached the final destination.')


# Контрольные точки
X = [1000, 2000, 3000, 2000, 2500]
Y = [0, 200, 0, 0, -300]

# Вычисления
air1 = Aircraft(0, 0, 100, 40)
air1.goAlongPath(X, Y)



