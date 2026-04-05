# IP Shield

**IP Shield** is an intelligent agent-based platform designed to help creators and businesses in India protect their intellectual property. It automates the process of trademark searching, similarity checking, and application drafting using Google's Gemini AI.

## Features

- **Agentic Workflow**: Uses a multi-step agent loop to analyze IP risks
- **Real-time Streaming**: See the agent "thinking" with live updates on tool calls and results
- **Mock Tools**: Integrated with mock tools for trademark search, similarity analysis, and application drafting
- **Modern UI**: Clean, responsive interface built with React and Vite
- **Fast Backend**: Built with FastAPI for high-performance API

## Architecture

```mermaid
graph TD
    User[User Query] -->|POST /api/analyze| Frontend[Frontend (React)]
    Frontend -->|SSE Stream| Backend[Backend (FastAPI)]
    Backend -->|Gemini 3.1 Flash Lite| Gemini[Google Gemini API]
    Gemini -->|Tools| Tools[Tools Module]
    Tools -->|Search| MockSearch[Mock Trademark Search]
    Tools -->|Similarity| MockSimilarity[Mock Similarity Check]
    Tools -->|Nice Class| MockClass[Mock Nice Class]
    Tools -->|Draft| MockDraft[Mock Draft Application]
    
    subgraph Frontend
        QueryInput[QueryInput Component]
        AgentTrace[AgentTrace Component]
    end
    
    subgraph Backend
        AgentLoop[Agent Loop]
        Prompts[Prompts]
        Tools[Tools Module]
    end
    
    subgraph Gemini
        GeminiAPI[Gemini API]
        SystemPrompt[System Prompt]
    end
```

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Google Gemini API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd IP-shield
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd ../frontend
   npm install
   ```

### Configuration

Create a `.env` file in the `backend/` directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Running the Application

1. **Start the backend**
   ```bash
   cd backend
   uvicorn main:app --reload
   ```
   The API will be available at `http://localhost:8000`

2. **Start the frontend**
   ```bash
   cd ../frontend
   npm run dev
   ```
   The application will open at `http://localhost:5173`

## Usage

1. Open [http://localhost:5173](http://localhost:5173) in your browser
2. Enter a query in the text area (e.g., "Protect my brand name 'Zomato' for food delivery services")
3. Click **Analyze**
4. Watch the agent work in real-time with detailed step-by-step updates

## Agent Workflow

The agent follows this process:

1. **Receive Query**: Parses the user's request
2. **Search Trademarks**: Checks for existing trademarks
3. **Check Similarity**: Evaluates phonetic and semantic matches
4. **Determine Class**: Identifies the correct Nice classification
5. **Draft Application**: Generates a draft application
6. **Final Output**: Returns risk assessment and recommendations

## Tools

The agent uses the following mock tools:

- `search_trademark`: Searches trademark databases
- `check_similarity`: Checks phonetic and semantic similarity
- `get_nice_class`: Determines Nice classification
- `draft_application`: Drafts trademark application

## Technologies Used

- **Backend**: FastAPI, Google Gemini API
- **Frontend**: React, Vite
- **Styling**: CSS (inline styles)

## License

MIT
