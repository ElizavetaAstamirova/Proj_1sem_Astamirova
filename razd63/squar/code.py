def square_perimetr():
    print("�������: 1-������ ���� �������.  2-������������ ��������� �������.")
    n = int(input("�������� ������� 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("����� ������� ���")
            n = int(input("�������� ����� 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("������� ����j�� a: "))
    else:
        a = default_a
    p = a*4
    print("�������� �������� = ", p)


def square_area():
    print("�������: 1-������ ���� �������.  2-������������ ��������� �������.")
    n = int(input("�������� ������� 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("����� ������� ���")
            n = int(input("�������� ������� 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("������� ����j�� a: "))
    else:
        a = default_a
    s = a**2
    print("������� �������� = ", s)


default_a = 15