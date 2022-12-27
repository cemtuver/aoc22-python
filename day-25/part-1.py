with open("input.txt") as f:
    lines = f.read().split("\n")

snafu_decoder = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

snafu_encoder = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "="
}

def decode_snafu(snafu):
    result = 0

    for i, snafu_number in enumerate(reversed(snafu)):
        result += (5 ** i) * snafu_decoder[snafu_number]

    return result

def encode_to_snafu(number):
    snafu = ""

    while number != 0:
        decimal = ((number + 2) % 5) - 2
        snafu += snafu_encoder[decimal]
        number = (number - decimal) // 5
    
    return snafu[::-1]

total = sum(list(map(decode_snafu, lines)))
print(encode_to_snafu(total))
