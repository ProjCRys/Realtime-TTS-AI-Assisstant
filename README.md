# Realtime TTS Assistant

This project is a real-time Text-to-Speech (TTS) assistant powered by OpenAI's GPT-3 model and a local inference server. It converts text input into speech output as you type, making it an interactive and hands-free tool.

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x
- Required Python packages (install via `pip`):
  - `openai`
  - `pyttsx3`
  - `nltk`
- LM Studio
  
## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/Realtime-TTS-Assistant.git](https://github.com/ProjCRys/Realtime-TTS-Assisstant.git
   cd Realtime-TTS-Assistant
   ```

2. Configure OpenAI API settings or you can use local host for local language models in the script:

   - Set the API base and key in the script:

   ```python
   openai.api_base = 'http://localhost:1234/v1'  # Update with your API endpoint
   openai.api_key = 'YOUR_API_KEY'  # Replace with your API key or simply leave it emoty for local language models
   ```

3. Create a `context.txt` file and provide system prompt for the assistant.

4. Customize prompt format by modifying the `prefix` and `suffix` variables as needed.

5. Run the script:

   ```bash
   python lmStudio_to_TTS.py
   ```

## Usage

1. Run the script and interact with the assistant in your terminal. Type your input, and the assistant will respond with speech output in real-time.

2. To exit the program, type 'exit' and press Enter.

## Features

- Real-time text-to-speech conversion.
- Customizable prompt format.
- Sentence-based TTS for natural conversation flow.

## Sample Video
https://m.youtube.com/watch?v=TrOsG4jnSNw&t=5s 

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for the GPT-3 model.
- Python community and open-source contributors.

For inquiries or support, please contact [your@email.com](mailto:your@email.com).

---

Make sure to replace the placeholders with your specific information and customize the README as needed. Once your GitHub repository is set up, you can commit and push your code to make it accessible to others.
