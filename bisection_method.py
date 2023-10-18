def bisection_method(f, a, b, tolerance, max_iterations=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Tanda fungsi f(a) dan f(b) harus berbeda.")

    iteration = 0
    while (b - a) / 2.0 > tolerance and iteration < max_iterations:
        c = (a + b) / 2.0
        if f(c) == 0:
            return round(c, 4)  # Menggunakan round() untuk membatasi angka desimal
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration += 1
        print(f"Iterasi {iteration}: a = {a:.4f}, b = {b:.4f}, c = {c:.4f}, f(c) = {f(c):.6f}")

    return round((a + b) / 2.0, 4)

# Fungsi untuk persamaan x^4 - x^3 + 2x^2 - 2x - 12
def equation(x):
    return x**4 - x**3 + 2*x**2 - 2*x - 12

a = -2.0
b = 0.0
tolerance = 0.0001

root = bisection_method(equation, a, b, tolerance)
print("Akar fungsi: {:.4f}".format(root))
