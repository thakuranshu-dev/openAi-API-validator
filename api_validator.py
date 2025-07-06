import openai

def check_api_key(api_key):
    try:
        openai.api_key = api_key.strip()
        # Simple test: list models
        openai.Model.list()
        return True
    except Exception:
        print(f"Invalid API Key: {api_key.strip()}")
        return False

def main():
    with open('api.txt', 'r') as f:
        api_keys = f.readlines()

    working_keys = []
    for key in api_keys:
        if check_api_key(key):
            print(f"Working API Key: {key.strip()}")
            working_keys.append(key.strip())

    if working_keys:
        x = input("Do you want to save the working API keys? (y/n): ")
        if x.lower() == 'y':
            print("Saving working API")
            with open('working.txt', 'w') as f:
                for key in working_keys:
                    f.write(key + '\n')
            print("Working API keys saved to `working.txt`")

    print("Finished checking API keys.")
        

if __name__ == "__main__":
    main()