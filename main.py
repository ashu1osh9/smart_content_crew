from dotenv import load_dotenv
from crew import run_crew

load_dotenv()

if __name__ == "__main__":
    topic = input("Enter the topic you want a blog on: ")

    print(f"\n🚀 Starting research and blog writing on '{topic}'...\n")
    result = run_crew(topic)

    print("\n✅ Blog is ready!\n")
    print(result)

    # Save to file
    with open("blog_output.md", "w", encoding="utf-8") as f:
        f.write(str(result))
    print("\n📄 Saved to blog_output.md!")
