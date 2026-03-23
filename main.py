from dotenv import load_dotenv
from crew import run_crew

load_dotenv()

if __name__ == "__main__":
    topic = input("Kis topic par blog chahiye? ")

    print(f"\n🚀 '{topic}' par research aur blog likhna shuru...\n")
    result = run_crew(topic)

    print("\n✅ Blog ready hai!\n")
    print(result)

    # File mein save karo
    with open("blog_output.md", "w", encoding="utf-8") as f:
        f.write(str(result))
    print("\n📄 blog_output.md mein save ho gaya!")
