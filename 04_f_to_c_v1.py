# quick component to convert degrees C to F.
# Function takes in value, does conversion and puts answer into a list


def to_f(from_f):
    celsius = (from_f - 32) * 5/9
    return celsius


# Main routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = "{} degrees F is {:.2f} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)
