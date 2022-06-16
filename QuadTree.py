import tkinter
from tkinter import *


class Rectangle:
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class QuadTree:
    def __init__(self, boundary, bucket):
        self.boundary = boundary
        self.bucket = bucket
        self.arr = []
        self.NorthEast = None
        self.NorthWest = None
        self.SouthEast = None
        self.SouthWest = None
        self.divided = False

    def contains(self, point):
        if (((point.x >= self.boundary.x - self.boundary.w) and (point.x <= self.boundary.x + self.boundary.w)) and
                ((point.y <= self.boundary.y + self.boundary.h) and (point.y >= self.boundary.y - self.boundary.h))):
            return True
        return False

    def subdivide(self):
        nE = Rectangle(self.boundary.x + (self.boundary.w / 2), self.boundary.y + (self.boundary.h / 2),
                       self.boundary.w / 2, self.boundary.h / 2)
        nW = Rectangle(self.boundary.x - (self.boundary.w / 2), self.boundary.y + (self.boundary.h / 2),
                       self.boundary.w / 2, self.boundary.h / 2)
        sE = Rectangle(self.boundary.x + (self.boundary.w / 2), self.boundary.y - (self.boundary.h / 2),
                       self.boundary.w / 2, self.boundary.h / 2)
        sW = Rectangle(self.boundary.x - (self.boundary.w / 2), self.boundary.y - (self.boundary.h / 2),
                       self.boundary.w / 2, self.boundary.h / 2)
        NorthEast = QuadTree(nE, self.bucket)
        NorthWest = QuadTree(nW, self.bucket)
        SouthEast = QuadTree(sE, self.bucket)
        SouthWest = QuadTree(sW, self.bucket)

    def insert(self, point):
        if not self.contains(point):
            return False

        if len(self.arr) < self.bucket:
            self.arr.append(point)
            return True

        if not self.divided:
            self.subdivide()
            self.divided = True

        if self.NorthEast.insert(point):
            return True
        if self.NorthWest.insert(point):
            return True
        if self.SouthEast.insert(point):
            return True
        if self.SouthWest.insert(point):
            return True

        return False

    def visualize(self, pointsList):
        root = Tk()
        canvas = tkinter.Canvas()
        self.paint(canvas)
        root.mainloop()

    def paint(self, canvas):
        canvas.create_rectangle(self.boundary.x - self.boundary.w, self.boundary.y + self.boundary.h,
                                self.boundary.x + self.boundary.w, self.boundary.y - self.boundary.h)

        if self.divided:
            self.paint(self.NorthEast)
            self.paint(self.NorthWest)
            self.paint(self.SouthEast)
            self.paint(self.SouthWest)


