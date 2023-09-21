class AreaCalculator:

    def calculate_area(self, *args):
        if len(args) == 2 and all(type(arg) in (int, float) for arg in args):
            length, width = args
            return length * width
        elif len(args) == 1 and type(args[0]) in (int, float):
            radius = args[0]
            return 3.14 * radius**2
        elif len(args) == 3 and all(type(arg) in (int, float) for arg in args[:-1]) and args[-1] == "triangle":
            base, height = args[:2]
            return 0.5 * base * height
        else:
            raise ValueError("Invalid arguments provided")

    def get_user_input(self):
        values_list = []
        while len(values_list) < 3:
            element = input("Enter an element (or 'end' to finish): ")
            if element == 'end':
                break
            values_list.extend([element if element.lower() == 'triangle' else float(element)])
        return values_list

# Example usage
if __name__ == "__main__":
    calculator = AreaCalculator()

    value_list = calculator.get_user_input()
    area = calculator.calculate_area(*value_list)

    if len(value_list) == 1:
        print("Area of Circle:", area)
    elif len(value_list) == 2:
        print("Area of Rectangle:", area)
    elif len(value_list) == 3:
        print("Area of Triangle:", area)
