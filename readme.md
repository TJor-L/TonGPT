### Usage

1. **Install dependencies**  
   Run the following command in the project root directory to install the dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**  
   Copy the `.env_copy_this` file and rename it to `.env`:

   ```bash
   cp .env_copy_this .env
   ```

   Then, open the `.env` file and add your `OpenAI` API key:

   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Prepare data for retrieval**  
   Place the `.md` files you want to search in the `data` folder.

4. **Generate Embeddings**  
   Run the `scripts/generate_embeddings.py` script to generate the embeddings from the `.md` files in the `data` folder. The embeddings and the mapping index files will be saved in the `embeddings` folder:

   ```bash
   python scripts/generate_embeddings.py
   ```

5. **Run tests**  
   Run the test script to verify the functionality:

   ```bash
   python scripts/test.py
   ```