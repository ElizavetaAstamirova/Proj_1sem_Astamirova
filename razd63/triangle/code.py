import math

def triangle_perimetr():
    print("�������: 1-������ ���� ������.  2-������������ ��������� ������.")
    n = int(input("�������� ������� 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("����� ������� ���")
            n = int(input("�������� ������� 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("������� ������ a: "))
        b = int(input("������� ������ b: "))
        c = int(input("������� ������ c: "))
    else:
        a = default_a
        b = default_b
        c = default_c
    p = a + b + c
    print("�������� ������������ = ", p)


def triangle_area():
    print("�������: 1-������ ���� ������.  2-������������ ��������� ������.")
    n = int(input("�������� ������� 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("������ ������� ���")
            n = int(input("�������� ������� 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("������� ������ a: "))
        b = int(input("������� ������ b: "))
        c = int(input("������� ������ c: "))
    else:
        a = default_a
        b = default_b
        c = default_c
    pp = (a + b + c) / 2
    s = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
    print("������� ����������� = ", s)


default_a = 7
default_b = 2
default_c = 8