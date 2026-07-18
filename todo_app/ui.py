def print_menu(title: str, options: list[str] | None = None, width: int = 50) -> None:
    border = "=" * width
    
    print(f"\n╔{border}╗")
    print(f"║{title:^{width}}║") # The symbol ^ means center the text.

    if options:
        print(f"╠{border}╣")

        for number, option in enumerate(options, start=1):
            prefix = f" {number}. "
            print(f"║{prefix}{option:<{width - len(prefix)}}║") # The symbol < means left-align the text.

    print(f"╚{border}╝")