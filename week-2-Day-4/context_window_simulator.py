import tiktoken


CONTEXT_LIMIT = 500
WARNING_THRESHOLD = 0.80


class ContextWindow:
    def __init__(self, limit=CONTEXT_LIMIT):
        self.limit = limit
        self.messages = []
        self.encoding = tiktoken.get_encoding("cl100k_base")

    def count_tokens(self, text):
        return len(self.encoding.encode(text))

    def total_tokens(self):
        return sum(message["tokens"] for message in self.messages)

    def add_message(self, message):
        token_count = self.count_tokens(message)

        self.messages.append({
            "text": message,
            "tokens": token_count
        })

        self.remove_old_messages()

    def remove_old_messages(self):
        while self.total_tokens() > self.limit and self.messages:
            removed = self.messages.pop(0)

            print(
                f"\nRemoved oldest message "
                f"({removed['tokens']} tokens) to stay within the limit."
            )

    def display_status(self):
        used = self.total_tokens()
        percentage = (used / self.limit) * 100

        print("\n" + "=" * 50)
        print("CONTEXT WINDOW STATUS")
        print("=" * 50)

        print(f"Used tokens : {used}")
        print(f"Limit       : {self.limit}")
        print(f"Usage       : {percentage:.1f}%")
        print(f"Messages    : {len(self.messages)}")

        if percentage >= 100:
            print("WARNING: Context window exceeded!")

        elif percentage >= WARNING_THRESHOLD * 100:
            print("WARNING: Context window is nearly full!")

        else:
            print("Status: Context window has available space.")

        print("=" * 50)

    def display_messages(self):
        print("\nCurrent conversation:")

        for index, message in enumerate(self.messages, start=1):
            print(
                f"{index}. "
                f"[{message['tokens']} tokens] "
                f"{message['text']}"
            )


def main():
    context = ContextWindow()

    print("=" * 50)
    print("CONTEXT WINDOW SIMULATOR")
    print("=" * 50)

    print(f"Context limit: {CONTEXT_LIMIT} tokens")
    print("Type 'exit' to stop.")
    print("Type 'history' to view stored messages.")

    while True:
        message = input("\nUser: ")

        if message.lower() == "exit":
            print("Exiting simulator...")
            break

        if message.lower() == "history":
            context.display_messages()
            context.display_status()
            continue

        context.add_message(message)
        context.display_status()


if __name__ == "__main__":
    main()