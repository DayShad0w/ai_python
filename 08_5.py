
# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
# умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum():
    real_part: int
    complex_part: int

    def __init__(self, real, complex):
        self.complex_part = complex
        self.real_part = real

    def __add__(self, other):
        comp = self.complex_part + other.complex_part
        real = self.real_part + other.real_part
        if comp>0:
            sign = "+"
        else:
            sign = ""
        return f"{real}{sign}{comp}i"

    def __mul__(self, other):
        real = self.real_part*other.real_part - self.complex_part*other.complex_part
        comp = self.real_part*other.complex_part + self.complex_part*other.real_part
        if comp > 0:
            sign = "+"
        else:
            sign = ""
        return f"{real}{sign}{comp}i"

one_complex = ComplexNum(2, -5) # 2-5i
two_complex = ComplexNum(7, 3)  # 7+3i
print(one_complex.__add__(two_complex))
print(one_complex.__mul__(two_complex))
