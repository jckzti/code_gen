import random
import subprocess

import requests

model_name = "llama3.1:8b"  # Nome do modelo no Ollama


def _extract_code_from_response(response):
    """Extrai o código Python da resposta do LLM"""
    if "```python" in response and "```" in response:
        start = response.find("```python") + len("```python")
        end = response.rfind("```")
        return response[start:end].strip()
    else:
        return response.strip()


prompt = f"""
Gere um arquivo python com um script legal, que nunca precise passar parâmetro de entrada:

Formato do script:
```python
# Código do teste aqui
```
"""

# Fazer uma requisição para a API do Ollama
response = requests.post('http://localhost:11434/api/generate',
                         json={
                             "model": model_name,
                             "prompt": prompt,
                             "stream": False
                         })

response_json = response.json()
response_text = response_json.get('response', '')
print('response_text', response_text)

test_script = _extract_code_from_response(response_text)

random_num = random.randint(100000, 999999)
filename = f"script_{random_num}.py"

with open(filename, "w", encoding="utf-8-sig") as f:
    f.write(test_script)

print("\n--- Executando o script ---\n")
try:
    result = subprocess.run(["python", filename], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("\n--- Erro na execução ---\n")
    print(e.stderr)
