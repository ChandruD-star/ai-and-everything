# 🔗 Agentic AI Workshop 

## 🚀 Setup 

### Installation

Download the course repository

```bash
# Clone the repo, cd to 'ai-agent-workshop' directory
git clone https://github.com/ChandruD-star/ai-and-everything.git
cd ./sessions/202510/ai-agent-workshop
```

### Prerequisites

- Docker Desktop or Podman Desktop installed and setup correctly (if planning to run JupyterLab as a container)
- Ensure you're using Python 3.11 - 3.13.
- Ollama installed and running with any LLM model

### 1. Ollama SETUP (post successful installation)

```bash
# Download and serve any Ollama LLM model
ollama pull <LLM_MODEL_NAME>

#Example commands:
ollama pull granite4:latest
ollama pull Smollm:latest
ollama pull qwen3:4b

# List all LLM models in your system (post installation in previous step)
ollama ls

```

### 2.1 Local Setup for JupyterLab and Python Virtual Environment (venv)

**Note: Skip this section if you'll run JupyterLab environment as a container inside Podman Desktop or Docker Desktop tool**

```bash
# If planning to start JupyterLab locally from the current directory

# Step 1 - Create the virtual environment and activate the virtual environment as per your operating system
python -m pip install venv .venv

# On macOS/Linux (Bash/Zsh)
source .venv/bin/activate 

# Windows (Command Prompt)
.venv\Scripts\activate.bat 

# Windows (PowerShell)
.venv\Scripts\Activate.ps1 


# Step 2 - Install the dependencies for the workshop using the requirements.txt file inside the "/workshop-notebooks" directory
python -m pip install -r ./workshop-notebooks/requirements.txt

# Step 3 (run this command from the root rirectory of this project folder)
jupyter lab

# Step 4 - Input the token "workshop2025" and hit ENTER which will open your JupyterLab session

```

### 2.2 Setup for JupyterLab Container

Step 1 - Build the Docker image to mount all notebooks inside the container (⚠️this command has to be run locally⚠️)

This step will create the image "student-machine:v1" and we will use this image to run the container in Step 2

- If using Podman Desktop

```bash
podman build -t student-machine:v1 .
```
- If using Docker Desktop

```bash
docker build -t student-machine:v1 .
```

Step 2 - Run the JupyterLab container and can be accessed using the URL http://localhost:9001/lab 

- If using Podman Desktop

```bash
podman run -e JUPYTER_TOKEN=workshop2025 --network workshop-network -d --rm --name student01-9001 -e CHOWN_EXTRA=""/home/jovyan/workshop"" -e CHOWN_EXTRA_OPTS='-R' --user root -p 9001:8888 student-machine:v1
```
- If using Docker Desktop

```bash
docker run -e JUPYTER_TOKEN=workshop2025 --network workshop-network -d --rm --name student01-9001 -e CHOWN_EXTRA=""/home/jovyan/workshop"" -e CHOWN_EXTRA_OPTS='-R' --user root -p 9001:8888 student-machine:v1
```
Step 3 - Input the token "workshop2025" and hit ENTER which will open your JupyterLab session




### ENVIRONMENT FILE SETUP

Make a copy of example.env in your local environment or the container environment to setup the environment file.

```bash
# Create .env file
cp example.env .env
```

# ✅ Run notebooks ✅

Great job if you reached till here! Now you're ready to run the notebooks in your preferred environment!


# 📚 Lessons
This repository contains nine short notebooks that serve as brief introductions to many of the most-used features in LangChain, starting with the new **Create Agent**.

---

### `L1_fast_agent.ipynb` - 🤖 Create Agent 🤖
- In this notebook, you will use LangChain’s `create_agent` to build an SQL agent in just a few lines of code.  
- It demonstrates how quick and easy it is to build a powerful agent. You can easily take this agent and apply it to your own project. 

---

### `L2-7.ipynb` - 🧱 Building Blocks 🧱
In Lessons 2–7, you will learn how to use some of the fundamental building blocks in LangChain. These lessons explain and complement `create_agent`, and you’ll find them useful when creating your own agents. Each lesson is concise and focused.

- **L2_messages.ipynb**: Learn how messages convey information between agent components.  
- **L3_streaming.ipynb**: Learn how to reduce user-perceived latency using streaming.  
- **L4_tools.ipynb**: Learn basic tool use to enhance your model with custom or prebuilt tools.  
- **L5_tools_with_mcp.ipynb**: Learn to use the LangChain MCP adapter to access the world of MCP tools.  
- **L6_memory.ipynb**: Learn how to give your agent the ability to maintain state between invocations.  
- **L7_structuredOutput.ipynb**: Learn how to produce structured output from your agent.  

---

### `L8-9.ipynb` - 🪛 Customize Your Agent 🤖
Lessons 2–7 covered out-of-the-box features. However, `create_agent` also supports both prebuilt and user-defined customization through **Middleware**. This section describes middleware and includes two lessons highlighting specific use cases.

- **L8_dynamic.ipynb**: Learn how to dynamically modify the agent’s system prompt to react to changing contexts.  
- **L9_HITL.ipynb**: Learn how to use Interrupts to enable Human-in-the-Loop interactions.
