class Rectangle:

    def __init__(self, x_upper, y_upper, x_lower, y_lower):
        self.x_upper = x_upper
        self.y_upper = y_upper
        self.x_lower = x_lower
        self.y_lower = y_lower
        self.height = abs(self.y_upper - self.y_lower)
        self.width = abs(self.x_lower - self.x_upper)
    
    def __str__(self):
        res = ""
        res += "*" * self.width + "\n" # first line
        for i in range(self.height-2):
            res += "*" + " " * (self.width - 2) + "*\n" # middle lines

        res += "*" * self.width + "\n" # last line
        return res

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)
