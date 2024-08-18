# AiDishwasher

AiDishwasher is an AI-powered assistant that helps you choose and start a dishwasher program based on user input. It leverages the `langchain_openai` framework and integrates with OpenAI's GPT-4 model to process natural language commands and return appropriate dishwasher settings.

## Features

- **AI-Powered Decision Making:** Uses GPT-4 to process user input and select the appropriate dishwasher program.
- **Session History:** Maintains conversation history using `InMemoryChatMessageHistory` to ensure context is retained throughout the session.
- **Customizable System Prompt:** Allows the system prompt to be set via environment variables for tailored interactions.
- **JSON Output:** Saves the selected dishwasher program configuration to a JSON file.

## Requirements

- Python 3.7+
- OpenAI API key
- Required Python packages (listed in `requirements.txt`):
    - `langchain_openai`
    - `langchain_core`
    - `python-dotenv`

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/RochuOfficial/OpenAiAssistant.git
    cd AiDishwasher
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API key and system prompt to the `.env` file:
      ```
      OPENAI_API_KEY=your_openai_api_key_here
      SYSTEM_PROMPT="Your custom system prompt here"
      ```
    - Refer to the `system_prompt_example.txt` file in this repository for an example of how to structure your system prompt.

4. **Run the application:**
    ```bash
    python main.py
    ```

## Usage

- When you run the application, you'll be prompted to enter the name of a dishwasher program.
- The AI assistant will interpret your input and suggest a suitable program.
- The selected program will be saved to `./output/output.json`.
- To stop the program, enter "koniec" or "wyłącz się".

## Example

```bash
$ python main.py
Jaki program mam włączyć ?: Jaki program polecasz aby skończyć zmywanie jeśli za 15 min mam gości ?
{
  "program": "quick",
  "answer": "Proponuję uruchomić program szybki, który pozwoli na szybkie umycie lekko zabrudzonych naczyń przed przyjściem gości."
}
