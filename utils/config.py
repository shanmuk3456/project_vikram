# --ollama pull deepseek-coder:6.7b 
# ollama pull qwen2.5-coder:7b 
# # ollama run gemma 
# # ollama run gemma:2b 
# ollama run deepseek-r1:8b (not for coding but for intelligence good for first step and reviews)
# ollama run gemma3:12b 
# ollama pull qwen3:8b 
# ollama pull deepseek-coder-v2:16b (best only for coding)
# ollama pull qwen3-coder:30
OLLAMA_URL="http://localhost:11434/api/generate"

DEFAULT_CHAT_MODEL="qwen3:8b"

DEFAULT_CODER_MODEL="deepseek-coder-v2:16b"

DEFAULT_CONTROLLER_MODEL="gemma:2b"