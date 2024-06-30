# ao3translate
AO3 Chapter Translator is a web application built with Flask that leverages the power of Google Gemini to enhance your reading experience on AO3 (Archive of Our Own) by providing translations of fanfiction chapters into your chosen language.  

Simply input the URL of a specific chapter from AO3, select the desired language, and the app will return the translated text.   

This tool is perfect for multilingual fans who wish to enjoy fanfiction in their preferred language.  

## Features
- Chapter Translation: Translates any AO3 chapter into the language of your choice.
- Multiple Language Support: Supports a wide range of languages for translation.
- User-Friendly Interface: Easy-to-use interface for seamless translation requests.
- Accurate Translations: Utilizes advanced natural language techonology with Google's LLM Gemini 1.5 Flash to ensure high-quality translations.

- ## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/ao3translate.git
   cd ao3translate
   ```

2. **Set up a Virtual Environment (Recommended):**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Cloud Credentials:**
    - Obtain a Google Cloud API key and set it as an environment variable:
        ```bash
        export GOOGLE_API_KEY="YOUR_API_KEY"
        ```

5. **Run the Application:**
   ```bash
   flask run
   ```

6. **Access the Application:**
    - Open your web browser and navigate to `http://127.0.0.1:5000/`

## Usage

1. **Enter AO3 URL:** Paste the URL of the AO3 fanfiction chapter you want to translate.
2. **Select Target Language:** Choose the desired language for translation.
3. **Click "Traduzir":** The application will fetch the chapter content, translate it using Google Gemini Pro, and display the translated text.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
