def calculate_cost(
    input_tokens,
    output_tokens,
    input_price_per_million,
    output_price_per_million
):
    input_cost = (input_tokens / 1_000_000) * input_price_per_million
    output_cost = (output_tokens / 1_000_000) * output_price_per_million

    total_cost = input_cost + output_cost

    return input_cost, output_cost, total_cost


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value < 0:
                print("Please enter a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():

    print("=" * 50)
    print("TOKEN COST CALCULATOR")
    print("=" * 50)

    input_tokens = get_positive_number(
        "\nInput token count: "
    )

    output_tokens = get_positive_number(
        "Output token count: "
    )

    input_price = get_positive_number(
        "Input price ($ per 1M tokens): "
    )

    output_price = get_positive_number(
        "Output price ($ per 1M tokens): "
    )

    input_cost, output_cost, total_cost = calculate_cost(
        input_tokens,
        output_tokens,
        input_price,
        output_price
    )

    print("\n" + "=" * 50)
    print("COST ESTIMATE")
    print("=" * 50)

    print(f"Input tokens       : {input_tokens:,.0f}")
    print(f"Output tokens      : {output_tokens:,.0f}")

    print(f"Input price        : ${input_price:.2f} / 1M tokens")
    print(f"Output price       : ${output_price:.2f} / 1M tokens")

    print(f"\nInput cost         : ${input_cost:.4f}")
    print(f"Output cost        : ${output_cost:.4f}")
    print(f"Estimated total    : ${total_cost:.4f}")

    print("=" * 50)


if __name__ == "__main__":
    main()