<div align="center">
  <h3 align="center">RPA</h3>
  <div>
  <a href="https://bgcp.vercel.app/article/fdb71409-eab4-4199-a4b2-016bab7f74f9">
  <img src="https://img.shields.io/badge/Download PDF (ENGLISH)-black?style=for-the-badge&logoColor=white&color=000000" alt="three.js" />
  </a>
  </div>
</div>

## 🚀 Introdução ao RPA de Cotação de Moedas com Python e Selenium
A automação de processos robóticos (RPA) com Selenium eleva a coleta de dados de cotações de moedas para o próximo nível. Selenium, uma ferramenta poderosa para automação de navegadores web, permite interagir com páginas da web de forma mais sofisticada que bibliotecas como Requests e BeautifulSoup. Isso é especialmente útil em páginas dinâmicas, onde os dados são carregados por JavaScript. Prepare-se para criar um bot em Python que usa o Selenium para capturar cotações de moedas em tempo real!

### 🌟 Principais Características:

- **⚡ Eficiência Aprimorada**: Ideal para páginas web dinâmicas onde o conteúdo é carregado por JavaScript.
- **🔄 Atualização em Tempo Real**: Acesso direto a dados atualizados, simulando a interação humana.
- **✔️ Fácil de Expandir**: Pode ser facilmente expandido para coletar dados de múltiplas fontes.
- **🔍 Interação Direta com o Navegador**: Simula a navegação real do usuário, proporcionando maior precisão.

## 🛠️ Instalação

### Windows, Linux e macOS:

1. **Instale o Python 3** (se ainda não estiver instalado).
2. **Instale o Selenium**:
   
   ```bash
   pip install selenium
   pip install webdriver_manager
   ```

3. **Baixe o WebDriver**:

   Você precisará do WebDriver correto para o navegador que deseja automatizar (Chrome, Firefox, etc.). Por exemplo, para o Chrome, baixe o ChromeDriver correspondente à versão do seu navegador em [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/). Salve o executável em um local conhecido no seu sistema.

## 📊 Uso Básico

### Configuração Inicial:

1. **Configurar o Selenium**:
   
   Importe o Selenium e configure o WebDriver no seu script Python:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
```

2. **Inicialize o WebDriver**:

```python
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

### Exemplo Básico:

Vamos coletar a cotação do Dólar para o Real utilizando o Selenium:

1. **Abra a URL de Cotação**:

```python
driver.get("https://www.google.com")
```

2. **Pesquise pela Cotação**:

```python
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("usd to brl")
search_box.send_keys(Keys.RETURN)
```

3. **Extraia a Cotação**:

```python
import time
time.sleep(5) # Aguarda o carregamento da página
rate = driver.find_element(By.CSS_SELECTOR, "#knowledge-currency__updatable-data-column > div.b1hJbf > div.dDoNo.ikb4Bb.gsrt.GDBPqd > span.DFlfde.SwHCTb").text
print(f"Cotação do Dólar para Real: {rate}")
```

4. **Encerre o WebDriver**:

```python
driver.quit()
```

## 📈 RPA para Monitoramento de Cotações de Moedas

### Motivo para Utilizar RPA na Cotação de Moedas:

🚀 Utilizar o Selenium permite não apenas automatizar a coleta de cotações em páginas dinâmicas, mas também interagir com elementos da web, como botões e formulários, para acessar dados que não seriam capturáveis com métodos tradicionais.

### Implementação do RPA:

O exemplo acima demonstra a base para uma implementação de RPA que pode ser expandida para monitorar diversas moedas e até mesmo automatizar a coleta de dados em intervalos regulares, utilizando agendadores de tarefa do sistema operacional.

### 🔍 Testes:

- **Verificação Manual**: Após a execução, verifique se a saída do script corresponde à cotação atual mostrada no navegador.
- **Automatização**: Use ferramentas como o cron (Linux/macOS) ou o Agendador de Tarefas (Windows) para executar o script em intervalos regulares.

## 🏆 Conclusão

Este tutorial apresentou como utilizar o Selenium junto ao Python para criar um RPA de cotação de moedas. Demonstramos como preparar o ambiente, interagir com páginas web e extrair informações em tempo real. O RPA com Selenium abre um leque de possibilidades para automação web, desde monitoramento de dados financeiros até testes de interface de usuário.

Esperamos que este guia tenha sido útil para iniciar seus projetos de automação com Selenium e Python. A capacidade de automatizar tarefas web não apenas economiza tempo, mas também abre novas oportunidades para análises e insights em tempo real. Continue explorando e expandindo seus conhecimentos em automação! 🤖💹