from pipeline_copilot.config import get_environment


def main() -> None:
    environment = get_environment()

    print("AI Data Pipeline Copilot started.")
    print(f"Environment: {environment}")


if __name__ == "__main__":
    main()