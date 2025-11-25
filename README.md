# Integrantes
- Felipe Cesar Ferreira de Figueiredo
- Felipe Viana Batista dos Santos
- Gabriel Da Silva Farias de Andrade
- Gabriel Lobo Tavares Pinto
- Marcos Vinicius dos Santos
- Nataly Rodrigues de Meneses
- Ramon Cardoso Vasconcelos
- Sandro Araujo da Silva

# Prova de Conceito
- Decidimos por manter o projeto conforme a primeira entrega por estar conciso e alinhado com o objrtivo do Projeto entregador

  # 🛒 Sistema de Fidelização de Cliente em Supermercado

## 🎯 Objetivo
- Validar a viabilidade do sistema de fidelização inteligente para supermercados, mostrando como o uso de dados de compras pode gerar:
- Campanhas personalizadas  
- Cupons de desconto  
- Comunicação eficiente com clientes via WhatsApp e Telegram  

## 📌 Escopo da Prova de Conceito
A Prova de conceito terá como foco um fluxo mínimo funcional, suficiente para demonstrar o valor da solução sem exigir a implementação completa do sistema.  

Inclui:  
- 📝 **Cadastro simplificado**: inserção de CPF e telefone no momento da compra  
- 💾 **Registro automático da compra**: simulação de integração com o sistema de caixa (PDV)  
- 📊 **Perfil de consumo**: armazenamento de dados básicos (produto comprado e frequência)  
- 📲 **Comunicação personalizada**: envio de mensagem simulada via WhatsApp com promoção ou cupom  
- 🖥️ **Painel administrativo**: protótipo simples exibindo dados coletados e campanhas criadas  

## 📌 Justificativa
A Prova de Conceito demonstrará que:  
- ✅ O cadastro rápido é viável e não gera barreiras para o cliente  
- 📈 O sistema transforma dados de compra em informações estratégicas  
- 🔔 A comunicação personalizada aumenta a relevância das promoções e engajamento  

## 🧩 Cenário de Demonstração
1. Cliente realiza uma compra e informa CPF e telefone no caixa  
2. O sistema registra a compra e vincula ao perfil do cliente  
3. O cliente recebe uma mensagem de boas-vindas no WhatsApp  
4. Após a compra, é enviada uma promoção personalizada (exemplo: *“Na compra de 1 pacote de biscoito, leve outro grátis”*)  
5. O painel administrativo exibe o histórico de compras e a campanha enviada  

## 🚀 Resultados Esperados
- 👤 **Clientes**: percepção imediata de valor ao receber ofertas relevantes e cupons exclusivos  
- 🏬 **Supermercado**: comprovação de que a personalização aumenta engajamento e pode elevar a taxa de recompra  
- 🎓 **Equipe acadêmica**: validação prática da proposta central do projeto, mostrando que o conceito é viável e escalável  

# 🧭 Tutorial

## 🧱 Criando ambiente virtual

```bash
python -m venv env
```

---

## 💻 Acessando ambiente virtual

### 🔹 No Windows:
```bash
env\Scripts\activate
```

### 🔹 No macOS / Linux:
```bash
source env/bin/activate
```

---

## 📦 Instalando dependências

```bash
pip install -r requirements.txt
```

---

## 🚀 Executando o servidor local

```bash
fastapi dev main.py
```

## Para acessar a documentação acesse:
http://localhost:8000/redoc

##Prova de Conceito

