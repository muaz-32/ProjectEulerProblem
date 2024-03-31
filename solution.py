import math

####################################          I used algebric integration instead of numerical integration                 #############################################
def write_the_val(k):
    if k == 1:
        a = (k + 0.5) ** 2
        root_a = k + 0.5
        upper_limit_a = (math.sqrt(a - 1) - 1) / k
        lower_limit = 0
        arc_sin_a_upper = math.asin((k * (k * upper_limit_a + 1)) / (root_a * k))
        arc_sin_a_lower = math.asin((k * (k * lower_limit + 1)) / (root_a * k))
        val_a_upper = a * arc_sin_a_upper + (k * upper_limit_a + 1) * math.sqrt(-1 * k * upper_limit_a * (k * upper_limit_a + 2) + a - 1) - 2 * k * upper_limit_a
        val_a_lower = a * arc_sin_a_lower + (k * lower_limit + 1) * math.sqrt(-1 * k * lower_limit * (k * lower_limit + 2) + a - 1) - 2 * k * lower_limit
        val_a = (val_a_upper - val_a_lower) / (2 * (k ** 2))
        difference = val_a
        return difference * k
    a = (k + 0.5) ** 2
    b = (k - 0.5) ** 2
    root_a = k + 0.5
    root_b = k - 0.5
    upper_limit_a = (math.sqrt(a - 1) - 1) / k
    upper_limit_b = (math.sqrt(b - 1) - 1) / k
    lower_limit = 0
    arc_sin_a_upper = math.asin((k * (k * upper_limit_a + 1)) / (root_a * k))
    arc_sin_a_lower = math.asin((k * (k * lower_limit + 1)) / (root_a * k))
    arc_sin_b_upper = math.asin((k * (k * upper_limit_b + 1)) / (root_b * k))
    arc_sin_b_lower = math.asin((k * (k * lower_limit + 1)) / (root_b * k))
    val_a_upper = a * arc_sin_a_upper + (k * upper_limit_a + 1) * math.sqrt(-1 * k * upper_limit_a * (k * upper_limit_a + 2) + a - 1) - 2 * k * upper_limit_a
    val_a_lower = a * arc_sin_a_lower + (k * lower_limit + 1) * math.sqrt(-1 * k * lower_limit * (k * lower_limit + 2) + a - 1) - 2 * k * lower_limit
    val_a = (val_a_upper - val_a_lower) / (2 * (k ** 2))
    val_b_upper = b * arc_sin_b_upper + (k * upper_limit_b + 1) * math.sqrt(-1 * k * upper_limit_b * (k * upper_limit_b + 2) + b - 1) - 2 * k * upper_limit_b
    val_b_lower = b * arc_sin_b_lower + (k * lower_limit + 1) * math.sqrt(-1 * k * lower_limit * (k * lower_limit + 2) + b - 1) - 2 * k * lower_limit
    val_b = (val_b_upper - val_b_lower) / (2 * (k ** 2))
    difference = val_a - val_b
    return difference * k
def calculate_for_n():
    n = 69420
    # find the expected value
    expected_value = 0
    for k in range(1, n + 1):
        expected_value += write_the_val(k)
    return round(expected_value, 5)

print(calculate_for_n())
