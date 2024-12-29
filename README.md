# LangChain Assignment

## Objective
Develop a script to extract structured details about characters from stories in a provided dataset and output the required details in JSON format. The goal is to transform unstructured narrative data into a structured format using embeddings and processing techniques.

## Requirements

1. **Implementation**
   - The task is to develop a script to extract structured details about a character from the stories.
   - The script should leverage embeddings for information retrieval and processing.
   - The JSON output must be accurate and adhere to the specified format.
   - Use MistralAI with LangChain for this assignment.
   - Dataset repository: LangChain Assignment Dataset.

2. **Desired Behaviour**
   - Dataset Structure: The dataset will contain multiple files, each representing a single story.
   - CLI Command 1: `compute-embeddings`
     - This command should take all story files as input.
     - It will compute the embeddings for the stories and persist the data into a vector database.
     - Use FAISS as the vector database.
   - CLI Command 2: `get-character-info`
     - This command should take a character name as input and return the relevant structured details in JSON format.
     - It should search through the processed embeddings and provide details for the specified character.
     - Input: A character name.
     - Output: A JSON object with the following keys:
       - `name`: Name of the character.
       - `storyTitle`: Title of the character's story.
       - `summary`: A brief summary of the character's story.
       - `relations`: The character's relationships with other characters in the story.
       - `characterType`: The character's role (e.g., protagonist, villain, side character).

3. **Edge Case Handling**
   - Ensure the script gracefully handles edge cases (e.g., The input character name is not found in any story).

## Development Environment

- You can use Python for development.

## GitHub Repository

- Create a public GitHub repository for your project.
- Include a README.md file that provides detailed instructions on how to run the demo.

## Resources

- LangChain Documentation: [Python](https://python.langchain.com/)
- LangChain RAG Documentation: [Python](https://python.langchain.com/docs/rag)
- LangChain Vector DB Documentation: [Python](https://python.langchain.com/docs/vector_db)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <your-github-repo-url>
   cd <your-repo-directory>

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/SmitRamteke999/LangChain-Assignment.git
   cd LangChain-Assignment
   
