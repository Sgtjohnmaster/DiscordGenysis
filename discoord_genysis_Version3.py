import requests

class DiscoordGenysis:
    """
    DiscoordGenysis: An advanced AI assistant that answers any question in English, is highly knowledgeable,
    and can access external AI services (e.g., chatgpt.com) for support. The only restriction:
    it will not show or output code.
    """

    def __init__(self, external_api_url="https://chatgpt.com/api"):
        self.external_api_url = external_api_url

    def ask(self, prompt: str) -> str:
        # Restriction: Do not show code under any circumstance
        if self._is_code_request(prompt):
            return "Sorry, I am not allowed to provide or display code."

        # Attempt to answer using external AI support
        answer = self._query_external_ai(prompt)
        return answer

    def _is_code_request(self, prompt: str) -> bool:
        # Heuristic: look for keywords and code block symbols
        code_keywords = [
            "show code", "give code", "print code", "source code", "write code",
            "output code", "sample code", "display code", "code snippet"
        ]
        if any(kw in prompt.lower() for kw in code_keywords):
            return True
        if "```" in prompt or "<code>" in prompt or "def " in prompt.lower() or "function " in prompt.lower():
            return True
        return False

    def _query_external_ai(self, prompt: str) -> str:
        data = {
            "prompt": prompt,
            "language": "en"
        }
        try:
            response = requests.post(self.external_api_url, json=data, timeout=10)
            if response.status_code == 200:
                return response.json().get("answer", "Sorry, I couldn't find an answer.")
            else:
                return "Sorry, external AI support is currently unavailable."
        except Exception as e:
            return f"Error accessing AI support: {e}"

if __name__ == "__main__":
    ai = DiscoordGenysis()
    print("Welcome to DiscoordGenysis! Ask me anything in English. (Type 'exit' to quit.)")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            break
        answer = ai.ask(user_input)
        print("DiscoordGenysis:", answer)