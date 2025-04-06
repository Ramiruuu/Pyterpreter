## Python Website Interpreter

A simple web-based Python interpreter built with Flask, HTML, CSS, and JavaScript. Users can input Python code through a browser interface and see the output in real-time. This project is designed to be deployed on Vercel, leveraging its serverless architecture.

## Features

- Write and execute Python code directly in the browser.
- Clean, responsive UI with a code editor and output display.
- Error handling with color-coded output (black for success, red for errors).
- Deployable as a serverless application on Vercel.

## Project Structure

```
python_interpreter/
├── api/
│   └── app.py           # Flask backend logic
├── static/
│   ├── style.css        # CSS styling for the frontend
│   └── script.js        # JavaScript for frontend interactivity
├── templates/
│   └── index.html       # HTML template for the UI
├── requirements.txt     # Python dependencies
└── vercel.json          # Vercel configuration file
```

## Prerequisites

- Python 3.x
- Node.js (for Vercel CLI)
- Git
- Vercel CLI (`npm install -g vercel`)

## Local Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd python_interpreter
    ```

2. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application locally:
    ```bash
    python api/app.py
    ```

4. Open `http://localhost:5000` in your browser to test the interpreter.

## Usage

1. Type Python code in the textarea (e.g., `print("Hello, World!")`).
2. Click **Run Code** to execute it.
3. View the output or error messages below the editor.

## Deploying to Vercel

### Using Vercel CLI

1. Initialize Git (if not already done):
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

2. Deploy using Vercel CLI:
    ```bash
    vercel
    ```
    Follow the prompts to set up your project. Once deployed, Vercel will provide a live URL (e.g., `https://your-project-name.vercel.app`).

### Alternative: Deploy via GitHub

1. Push your code to a GitHub repository.
2. In the Vercel dashboard, import the repository and deploy.

## Security Note

This project uses Python's `exec()` function, which executes arbitrary code. **Do not use in production without proper sandboxing**, as it poses a security risk.

For a production-ready version, consider:
- Implementing a sandbox (e.g., PyPy sandbox).
- Adding execution time limits.
- Restricting dangerous operations.

## Enhancements

You can extend this project by:
- Adding syntax highlighting (e.g., with CodeMirror).
- Supporting user input (`input()`).
- Adding a "Save Code" feature.
- Implementing dark/light theme toggles.

## Contributing

Feel free to fork this repository, submit issues, or create pull requests with improvements!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.# Pyterpreter