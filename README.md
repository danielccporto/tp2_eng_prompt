# TP2 - Prompt Engineering

This project is a modular application that utilizes generative AI for text analysis and tourism insights generation. It combines various functionalities to explore the capabilities of the Gemini 1.5 model from Google Generative AI.

## Features

### 1. **Tourism Itinerary**
- Generates tourism insights for cities specified in a YAML file (`roteiro.yaml`).
- Visualizes tourist attractions with annual visitor numbers in an interactive chart.
- Converts textual visitor data into processable numerical values.

### 2. **News Summarization**
- Summarizes news articles, extracting key information such as entities involved, location, date, and main events.
- Identifies potential individuals, public entities, and companies mentioned in the news.

### 3. **Token Calculation**
- Evaluates the number of tokens used in extensive prompts to optimize the Gemini API usage.

## Project Files

- **`roteiro.py`**: Script for generating tourism insights and creating visualizations based on YAML data.
- **`resumo_noticia.py`**: Script for summarizing and analyzing news using AI.
- **`tokens.py`**: Script for token counting in prompts and content generation using the Gemini model.
- **`roteiro.yaml`**: Configuration file for tourism-related prompts.
- **`requirements.txt`**: Dependencies required to run the project.

## Technologies Used

- [Google Generative AI](https://cloud.google.com/genai): For content generation using the **Gemini 1.5** model.
- **Python**: Main programming language for the scripts.
- **YAML**: For tourism prompt configuration.
- **Matplotlib**: For data visualization through charts.
- **Pandas**: For data manipulation and analysis.

## Setup and Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/danielccporto/tp2_eng_prompt.git
   cd tp2_eng_prompt
2. Install the dependencies:
   pip install -r requirements.txt
3. Configure your Gemini API key:
   export API_KEY=<YOUR_API_KEY>
4. Run the desired scripts:
   - Tourism itinerary generation: python roteiro.py
   - News summarization: python resumo_noticia.py
   Token counting: python tokens.py
